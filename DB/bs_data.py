#%%
import numpy as np
import pandas as pd
import pymongo

####data  process
name_nt = np.array(pd.read_csv('2nt_name.csv'))[1:]
rule_nt = np.array(pd.read_csv('2nt_rule.csv'))[1:]
tel_nt = np.array(pd.read_csv('2nt_tel.csv'))[1:,1]
typ_nt = np.array(pd.read_csv('2nt_typ.csv'))[1:,1]
typ2_nt = np.array(pd.read_csv('2nt_typ2.csv'))[1:,1]

name_tp = np.array(pd.read_csv('1tp_name.csv'))[1:]
rule_tp = np.array(pd.read_csv('1tp_rule.csv'))[1:]
tel_tp = np.array(pd.read_csv('1tp_tel.csv'))[1:,1]
typ_tp = np.array(pd.read_csv('1tp_typ.csv'))[1:,1]
typ2_tp = np.array(pd.read_csv('1tp_typ2.csv'))[1:,1]
#len(name)
def create_table(name,rule,tel,typ,typ2):
    # name = np.array(pd.read_csv('1tp_name.csv'))[1:]
    # rule = np.array(pd.read_csv('1tp_rule.csv'))[1:]
    # tel = np.array(pd.read_csv('1tp_tel.csv'))[1:,1]
    # typ = np.array(pd.read_csv('1tp_typ.csv'))[1:,1]
    # typ2 = np.array(pd.read_csv('1tp_typ2.csv'))[1:,1]    
    a=[]
    b=[]
    c=[]
    ###
    d=[]
    e=[]
    f=[]
    for i in range(len(name)):

        # name
        for j in range(20):
            if name[i,1][j]==":":
                a.append(name[i,1][:j])
                b.append(name[i,1][(j+2):(j+5)])
                break
        
        if '限' in rule[i,1] :
            for j in range(20):
                if rule[i,1][j]=="限":
                    c.append(rule[i,1][j:j+3])
                    break
        else:
            c.append("不限")

        if '最短' in typ2[i]:
            typ2[i]='車位'
    all=np.concatenate([a,b,tel,typ,typ2,c])
    all=all.reshape((-1,6), order='F')
    return all

nt_table=create_table(name_nt, rule_nt, tel_nt, typ_nt, typ2_nt)
tp_table=create_table(name_tp, rule_tp, tel_tp, typ_tp, typ2_tp)


#%%

##mongo data insert
myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                               username='admin',
                               password='123456',)
mydb = myclient["testMongoDB"]
dblst = myclient.list_database_names()
if "testMongoDB" in dblst:
  print("testMongoDB已存在！")
nt = mydb["nt"]
tp = mydb["tp"]
collst = mydb.list_collection_names()


for i in range(len(nt_table)):
    mytestData = { "identity": nt_table[i,0], "name": nt_table[i,1], 
    "tel": nt_table[i,2],"typ1": nt_table[i,3],"typ2": nt_table[i,4], "gender": nt_table[i,5]}
    x = nt.insert_one(mytestData)
x = nt.find_one()
print(x)
for i in range(len(tp_table)):
    mytestData = { "identity": tp_table[i,0], "name": tp_table[i,1], 
    "tel": tp_table[i,2],"typ1": tp_table[i,3],"typ2": tp_table[i,4], "gender": tp_table[i,5]}
    x = tp.insert_one(mytestData)
x = tp.find_one()
print(x)
# %%
