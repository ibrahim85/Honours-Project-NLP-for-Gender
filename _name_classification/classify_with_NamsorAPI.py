# classify names using http://www.namsor.com/

import urllib2
import base64
import Namsor
from io import open
import re
from collections import Counter, defaultdict
import os
from pprint import pprint


api_client = Namsor.swagger.ApiClient(api_server="https://api.namsor.com/onomastics/api/json")

first_name = "John"  # Firstname
last_name = "Smith"  # Lastname
country_iso2 = ""  # Countryiso2
x_client_version = "namsor_restunited_v0.21.x"  # Library Version (Client)
x_channel_secret = "63m6Yx0zLNAM33krdm3SORekGn8CFB"  # Your API Key (Secret)
x_channel_user = "namsor.com/com.ramona@yahoo.com/612002"  # Your API Channel (User)

gendre_api = Namsor.GendreApi(api_client)

    
    # return Genderize (model)
        

    # To display structured information of a variable, please use var_dump: pip install var_dump
    # from var_dump import var_dump
    # var_dump(response)
    # print(response.gender, response.scale)

machine_females = open(os.path.join(os.environ["AAN_DIR"],"machine_femalesNAM.txt"),"w", encoding="utf-8")
machine_males = open(os.path.join(os.environ["AAN_DIR"],"machine_malesNAM.txt"),"w", encoding="utf-8")
result_unknown = open(os.path.join(os.environ["AAN_DIR"],"NAM_UNK"),"w", encoding="utf-8")

with open(os.path.join(os.environ["AAN_DIR"],"machine_unknown4.txt"),"r", encoding="utf-8") as f:
    unknown_names = set(map(lambda x: x.strip(), f.read().split("\n")))
    males=0
    females=0
    regex = re.compile(r"\w+\.", re.IGNORECASE)
    new_unk = set()
    for name in unknown_names:
        name = name.strip()
        try:
            fn = name.split(",")[1].strip().split()[0]
            ln = name.split(",")[0].strip()
            no_initials = regex.sub("",fn).strip()
            response = gendre_api.extract_gender(no_initials, ln, country_iso2, x_client_version, x_channel_secret, x_channel_user)
            g = response.gender
            p = float(response.scale)
            print(name,g,p)
            if abs(p) < 0.8:
                new_unk.add(name)
                continue
            if g == "male":
                males += 1
                machine_males.write(name + "; " + p + "\n")
                #print(name," M ",p)
            elif g == "female":
                females +=1
                machine_females.write(name + "; " + p + "\n")
                #print(name,"F ",p)
            else:
                print(name," UNK ",p)
                #new_unk.add(name)
        except:
            new_unk.add(name)

    #result_unknown.write("\n".join(new_unk))
    #print(males,females,len(new_unk), len(list(unknown_names)))


