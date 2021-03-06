#!/usr/bin/env python
#coding: utf8 
"""
WordAPI.py
Copyright 2014 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *


class GendreListApi(object):

    def __init__(self, api_client):
      self.apiClient = api_client

    

    def extract_gender_list(self, body, x_client_version, x_channel_secret, x_channel_user, **kwargs):
        """
         
        Genderize a list of names. For each name, passing a country ISO2 code for local context is optional but helps improve precision.

        Args:
            body, GenderizerList: {'names':[{'firstName':'andrea','lastName':'parker','id':1},{'firstName':'andrea','lastName':'rossini','id':2},{'firstName':'jean','lastName':'marchand','id':3},{'firstName':'jean','lastName':'weston','id':4},,{'firstName':'jean','lastName':'martin','countryIso2':'FR','id':5}]} (required)

            x_channel_secret, str: Your API Key (Secret) (required)

            x_channel_user, int: Your API Channel (User) (required)

            x_client_version, str: Library Version (Client) (required)

            

        Returns: GenderizerList
        """

        allParams = ['body', 'x_channel_secret', 'x_channel_user', 'x_client_version']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method extract_gender_list" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/gendreList'
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        bodyParam = None

        headerParams['Content-Type'] = 'application/json'

        if ('x_client_version' in params):
            headerParams['X-Client-Version'] = params['x_client_version']
        if ('x_channel_secret' in params):
            headerParams['X-Channel-Secret'] = params['x_channel_secret']
        if ('x_channel_user' in params):
            headerParams['X-Channel-User'] = params['x_channel_user']
        if ('body' in params):
            bodyParam = params['body']
        postData = (formParams if formParams else bodyParam)

        # authentication setting
        requireAuth = False

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, requireAuth)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'GenderizerList')
        return responseObject
        

        

    




