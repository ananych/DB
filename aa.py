#%%
import pandas as pd
import numpy as np

df_a=pd.read_csv('a_lvr_land_a.csv')[1:]
df_b=pd.read_csv('b_lvr_land_a.csv')[1:]
df_e=pd.read_csv('e_lvr_land_a.csv')[1:]
df_f=pd.read_csv('f_lvr_land_a.csv')[1:]
df_h=pd.read_csv('h_lvr_land_a.csv')[1:]

df_all=pd.concat([df_a,df_b,df_e,df_f,df_h])

df_all=df_all[(df_all['主要用途']=='住家用') & 
(df_all['建物型態']=='住宅大樓(11層含以上有電梯)') ]

ind=np.zeros(len(df_all))
for i in range(len(df_all)):
    if len(df_all['總樓層數'].iloc[i])>2 :
        if df_all['總樓層數'].iloc[i] == '十一層':
            ind[i]=0
        else:
            if df_all['總樓層數'].iloc[i] == '十二層':
                ind[i]=0
            else:
                df_all['總樓層數'].iloc[i]
                ind[i]=1
    else:
        ind[i]=0



filter_a=df_all[ind==1]


df_a=pd.read_csv('a_lvr_land_a.csv')[1:]
df_b=pd.read_csv('b_lvr_land_a.csv')[1:]
df_e=pd.read_csv('e_lvr_land_a.csv')[1:]
df_f=pd.read_csv('f_lvr_land_a.csv')[1:]
df_h=pd.read_csv('h_lvr_land_a.csv')[1:]

df_all=pd.concat([df_a,df_b,df_e,df_f,df_h])
count=0
total=0
total_car=0
for i in range(len(df_all)):
    count+=int(df_all['交易筆棟數'].iloc[i][-1])
    total+=int(df_all["總價元"].iloc[i])
    total_car+=int(df_all["車位總價元"].iloc[i])

filter_b=pd.DataFrame()
filter_b["總件數"]=len(df_all)
filter_b["總車位數"]=count
filter_b["平均總價元"]=total/len(df_all)
filter_b["平均車位總價元"]=total_car/count

filter_b = {
    "name": ["總件數", "總車位數", "平均總價元", "平均車位總價元"],
    "valius": [len(df_all), count, total/len(df_all), total_car/count]
}
filter_b = pd.DataFrame(filter_b)

filter_a.to_csv('filter_a.csv')

filter_b.to_csv('filter_b.csv')