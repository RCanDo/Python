#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:34:11 2020

@author: arek

sources:
    - link: https://requests.readthedocs.io/en/master/user/quickstart/
    - link: https://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python
"""

#%%
import requests as req
import json

#%%
dir(req)

# 
r = req.get(url='https://api.companieshouse.gov.uk/company/00000006', 
            auth=('nfnbczpTDQOH6ep5_oKxqSSZo0t2XYhFFMp1-iM4',''))
r
dir(r)
r.ok     # True == 
r.status_code   # 200

#%%
if(r.ok):  # True -- (r.status_code == 200)
    # further processing of
    print(r.headers['content-type'])
    print(r.content)
    print('\n')
    r_dict = json.loads(r.content.decode('utf-8'))
    print(r_dict)
    print('\n')
    print(r.json())
    print('\n')
    print(json.dumps(r.json(), indent=4, sort_keys=True))
    
else:
    r.raise_for_status()  # will help you fetch the http code that is returned from the API.
    
#%%
type(json.loads(r.content.decode('utf-8')))
    
r.text
r.url
r.encoding

r.json()
type(r.json())   # dict

#%%
#%%
r = req.get(url='https://api.companieshouse.gov.uk/search',
            data={'q':'Carluccio'},
            auth=('nfnbczpTDQOH6ep5_oKxqSSZo0t2XYhFFMp1-iM4',''))

#%%
if(r.ok):  # True -- (r.status_code == 200)
    dic = r.json()
    print(r.headers['content-type'])
    print(json.dumps(r.json(), indent=4, sort_keys=True))
    
#%%
dic.keys()    
dic['items'][0]['company_number']

#%%
r = req.get(url='https://api.companieshouse.gov.uk/company/02001576',
            auth=('nfnbczpTDQOH6ep5_oKxqSSZo0t2XYhFFMp1-iM4',''))
    
#%%
if(r.ok):  # True -- (r.status_code == 200)
    dic = r.json()
    print(r.headers['content-type'])
    print(json.dumps(r.json(), indent=4, sort_keys=True))
else:
    r.raise_for_status()     
    
#%%
#%%
r = req.get(url='https://api.companieshouse.gov.uk/search',
            data={'q':"Gold's Gym"},
            auth=('nfnbczpTDQOH6ep5_oKxqSSZo0t2XYhFFMp1-iM4',''))

#%%
if(r.ok):  # True -- (r.status_code == 200)
    dic = r.json()
    print(r.headers['content-type'])
    print(json.dumps(r.json(), indent=4, sort_keys=True))
    
#%%
dic.keys()    
company_key = dic['items'][0]['company_number']

#%%
r = req.get(url='https://api.companieshouse.gov.uk/company/' + company_key,
            auth=('nfnbczpTDQOH6ep5_oKxqSSZo0t2XYhFFMp1-iM4',''))
    
#%%
if(r.ok):  # True -- (r.status_code == 200)
    dic = r.json()
    print(r.headers['content-type'])
    print(json.dumps(r.json(), indent=4, sort_keys=True))
else:
    r.raise_for_status()     

#%%
#%%
r = req.get(url='https://api.companieshouse.gov.uk/search',
            data={'q':"Avianca"},
            auth=('nfnbczpTDQOH6ep5_oKxqSSZo0t2XYhFFMp1-iM4',''))


#%%
