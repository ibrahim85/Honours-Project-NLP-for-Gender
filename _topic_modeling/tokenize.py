"""
Tokenize acl.train_files and saves tokenized document matrix in ./docs.pkl

"""
import re
from metadata.metadata import ACL_metadata
import logging
import _pickle as pkl
from tqdm import tqdm
import numpy as np
import spacy

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.handlers = [logging.StreamHandler()]

np.random.seed(18101995)
nlp = spacy.load('en')


# Remove hyphens from words, to solve cases like he-llo
def dehyphenate(s):
    return s.replace('-\n', '').lower()


acl = ACL_metadata()

# Get all document texts and their corresponding IDs.
docs = []
doc_ids = []
for file in acl.train_files:
    doc_ids.append(acl.get_id(file))
    with open(file, errors='ignore', encoding='utf-8') as fid:
        txt = fid.read()
        # Replace any whitespace (newline, tabs, etc.) by a single space.
        txt = re.sub('\s', ' ', txt)
        txt = dehyphenate(txt)
        docs.append(txt)

processed_docs = []
for doc in nlp.pipe(tqdm(docs), n_threads=4, batch_size=100):
    # Process document using Spacy NLP pipeline.

    ents = doc.ents  # Named entities.

    # Keep only words (no numbers, no punctuation).
    # Lemmatize tokens, remove punctuation and remove stopwords.
    doc = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop and len(token) >= 3]

    # Remove common words from a stopword list.
    # doc = [token for token in doc if token not in STOPWORDS]

    # Add named entities, but only if they are a compound of more than word.
    doc.extend([str(entity) for entity in ents if len(entity) > 1])

    processed_docs.append(doc)

docs = processed_docs
del processed_docs

with open("docs.pkl", "wb") as f:
    pkl.dump(docs, f)