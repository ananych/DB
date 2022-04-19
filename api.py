
#%%
import pymongo
import pandas as pd
from flask import Flask ,jsonify ,request ,render_template
# from flask_jwt_extended import jwt_required
from datetime import date, datetime
from bson.objectid import ObjectId
# from mongodb_config import mongo_db
from flask_restful import Resource, reqparse, fields, marshal_with, abort
import json
# Requires the PyMongo package.
# https://api.mongodb.com/python/current


#%%


class api:
  def __init__(self, username, password):
    self.username=username
    self.password=password
    self.myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                               username=self.username,
                               password=self.password)
  def api1(self,sex,dist):
    if sex == '男':
      filter1={        'gender':"限男生"      }
    elif sex == '女':
      filter1={        'gender':"限女生"      }
    else:
      print("請輸入男/女")

    filter2={        'gender':"不限"      }
    if dist == 'tp' or dist == 'nt':
      pass
    else:
      print('請輸入tp/nt')

    result1 = self.myclient['testMongoDB'][dist].find(filter=filter1)
    result2 = self.myclient['testMongoDB'][dist].find(filter=filter2)


    df1=pd.Series(result1)
    df2=pd.Series(result2)
    df1.append(df2)
    return df1
  def api2(self,tel):

    
    filter1={        'tel':tel      }
    result1 = self.myclient['testMongoDB']['nt'].find(filter=filter1)
    result2 = self.myclient['testMongoDB']['tp'].find(filter=filter1)
    
    df1=pd.Series(result1)
    df2=pd.Series(result2)
    df1.append(df2)
    return df1
  def api3(self,identity):
    
    filter1={        'identity':identity      }
    result1 = self.myclient['testMongoDB']['nt'].find(filter=filter1)
    result2 = self.myclient['testMongoDB']['tp'].find(filter=filter1)
    df1=pd.Series(result1)
    df2=pd.Series(result2)
    df1.append(df2)
    return df1
  def api4(self,sex,identity,name):
    if sex =='男':
      ind=['先生']
    elif sex == '女':
      ind=['太太','小姐']
    filter1={        'identity':identity     }
    result1 = self.myclient['testMongoDB']['tp'].find(filter=filter1)
    df1=pd.Series(result1)
    re=[]
    for i in range(len(df1)):
      if df1[i]["name"][0]==name:
        if df1[i]["name"][1:2] in ind:
          re.append(df1[i])
    return re



    



