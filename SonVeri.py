#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd


# In[33]:


import numpy as np


# In[34]:


from pandas import DataFrame


# In[35]:


from datetime import datetime


# In[36]:


df=pd.read_csv("veriseti.txt",skiprows=14, sep=" ", usecols=[0,2,7])   #veriyi çekiyoruz
df.head(50)
df[2450:2490]


# In[37]:


df.info()   #bilgileri alır.






# In[38]:


df.isnull().sum()   #toplam kaç kayıp veri olduğunu gösterir.


# In[39]:


df.dropna(axis=0, how='all',inplace=True) #boşlukları sildik 
df.head(50)
df[2360:2390]


# In[40]:


#SAAT kolonundaki boş indexleri siliyoruz
df.dropna(subset=['SAAT'],inplace=True)
df.head(50)
df[2250:2320]


# In[41]:


# 'unnamed' kolonunda Min ve Maxlı indexleri siliyoruz
filt=df['Unnamed: 0']=='Min'  
filt|=df['Unnamed: 0']=='Max'
df.drop(index=df[filt].index, inplace=True)
df[100:160]
df[2250:2320]


# In[42]:


tarih=pd.DataFrame({"Tarih":df['Unnamed: 0']})  #tarih sütunu
tarih.head()
df[2250:2320]


# In[43]:


tarih['Tarih']=pd.to_datetime(tarih.Tarih,infer_datetime_format=True
)
tarih[3100:3200]


# In[44]:


tarih.dtypes


# In[45]:


saat=pd.DataFrame({"Saat":df['TARIH']})  #saat sütunu
saat.head(50)

 


# In[46]:


saat.dtypes


# In[47]:


saat.head(50)
for i in range(len('Saat')):
    i = i + 30
    saat['Saat'].replace('00:00','23:59',inplace=True)
    
    


# In[48]:


saat.head(50) 
saat.tail(50)


# In[49]:


seviye=pd.DataFrame({"Seviye":df['SAAT']})   #seviye sütunu
seviye.head()


# In[50]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[51]:


seviye.value_counts()


# In[52]:


seviye.plot.hist()


# In[53]:


#Diyagramda gördüğümüz üzere bu datamızda aykırı değer yoktur 
sns.distplot(seviye)


# In[54]:


a=seviye.sort_values("Seviye")
a


# In[55]:


a.dropna()


# In[56]:


sonveri=pd.concat([ tarih,saat,seviye],axis=1)
sonveri[26500:26550]


# In[57]:


sonveri[2270:2300]


# In[58]:


sonveri=sonveri[((sonveri['Seviye']<4 ))]


# In[59]:


plt.plot(sonveri.Tarih,sonveri.Seviye,'o')


# In[60]:


sonveri[2270:2300]


# In[61]:


#sonveri.to_csv(r'C:\Users\HP\Desktop\export_dataframe.csv',index=False,header=True)


# In[62]:


df1=pd.read_csv("veriseti1.txt",skiprows=14, sep=" ", usecols=[0,2,7])   #veriyi çekiyoruz
df1.head(50)


# In[63]:


df1.info()   #bilgileri alır.


# In[64]:


df1.isnull().sum()   #toplam kaç kayıp veri olduğunu gösterir.


# In[65]:


df1.dropna(axis=0, how='all',inplace=True) #boşlukları sildik 
df1.head(50)


# In[66]:


#SAAT kolonundaki boş indexleri siliyoruz
df1.dropna(subset=['SAAT'],inplace=True)
df1.head(50)


# In[67]:


# 'unnamed' kolonunda Min ve Maxlı indexleri siliyoruz
filt=df1['Unnamed: 0']=='Min'  
filt|=df1['Unnamed: 0']=='Max'
df1.drop(index=df1[filt].index, inplace=True)
df1.head()


# In[68]:


tarih1=pd.DataFrame({"Tarih":df1['Unnamed: 0']})  #tarih sütunu
tarih1.head()


# In[69]:


tarih1['Tarih']=pd.to_datetime(tarih1.Tarih,infer_datetime_format=True
)
tarih1[500:520]


# In[70]:


saat1=pd.DataFrame({"Saat":df1['TARIH']})  #saat sütunu
saat1.head(50)




for i in range(len('Saat')):
    i = i + 21
    saat1['Saat'].replace('00:00','23:59',inplace=True)
    


# In[71]:


saat1.head(50)
saat1.tail(50)


# In[72]:


seviye1=pd.DataFrame({"Seviye":df1['SAAT']})   #seviye sütunu
seviye1.head()


# In[73]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[74]:


seviye1.value_counts()


# In[75]:


seviye1.plot.hist()


# In[76]:


b=seviye1.sort_values("Seviye")
b


# In[77]:


b.dropna()


# In[78]:


sonveri1=pd.concat([ tarih1,saat1,seviye1],axis=1)
sonveri1


# In[79]:


sonveri1=sonveri1[((sonveri1['Seviye']<4 ))]


# In[80]:


plt.plot(sonveri1.Tarih,sonveri1.Seviye,'b')


# In[81]:


#sonveri1.to_csv(r'C:\Users\HP\Desktop\export_dataframe1.csv',index=False,header=True)


# In[82]:


df2=pd.read_csv("veriseti2.txt",skiprows=14, sep=" ", usecols=[0,2,7])   #veriyi çekiyoruz
df2.head(50)


# In[83]:


df2.info()   #bilgileri alır.


# In[84]:


df2.isnull().sum()   #toplam kaç kayıp veri olduğunu gösterir.


# In[85]:


df2.dropna(axis=0, how='all',inplace=True) #boşlukları sildik 
df2.head(50)


# In[86]:


#SAAT kolonundaki boş indexleri siliyoruz
df2.dropna(subset=['SAAT'],inplace=True)
df2.head(50)


# In[87]:


# 'unnamed' kolonunda Min ve Maxlı indexleri siliyoruz
filt=df2['Unnamed: 0']=='Min'  
filt|=df2['Unnamed: 0']=='Max'
df2.drop(index=df2[filt].index, inplace=True)
df2[100:160]


# In[88]:


saat2=pd.DataFrame({"Saat":df2['TARIH']})  #saat sütunu
saat2.head(50)


# In[89]:


for i in range(len('Saat')):
    i = i + 24
    saat2['Saat'].replace('00:00','23:59',inplace=True)


# In[90]:


saat2.head(50)
saat2.tail(50)


# In[91]:


tarih2=pd.DataFrame({"Tarih":df2['Unnamed: 0']})  #tarih sütunu
tarih2.head()


# In[92]:


tarih2['Tarih']=pd.to_datetime(tarih2.Tarih,infer_datetime_format=True
)
tarih2.head(10)


# In[93]:


seviye2=pd.DataFrame({"Seviye":df2['SAAT']})   #seviye sütunu
seviye2.head()


# In[94]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[95]:


seviye2.value_counts()


# In[96]:


seviye2.plot.hist()


# In[97]:


c=seviye2.sort_values("Seviye")
c


# In[98]:


c.dropna()


# In[99]:


sonveri2=pd.concat([ tarih2,saat2,seviye2],axis=1)
sonveri2


# In[100]:


sonveri2=sonveri2[((sonveri2['Seviye']<1.8 ))]


# In[101]:


plt.plot(sonveri2.Tarih,sonveri2.Seviye,'o')


# In[102]:


#sonveri2.to_csv(r'C:\Users\HP\Desktop\export_dataframe2.csv',index=False,header=True)


# In[103]:


df3=pd.read_csv("D01A052.csv",skiprows=0, usecols=[0,1,2])   #veriyi çekiyoruz
df3.head(100)


# In[104]:


df3.head(50)


# In[105]:


df3.tail(50)


# In[106]:


df3.info()   #bilgileri alır.


# In[107]:


df3.isnull().sum()   #toplam kaç kayıp veri olduğunu gösterir.


# In[108]:


df3.dropna(axis=0, how='all',inplace=True) #boşlukları sildik 
df3.head(50)


# In[109]:


tarih3=pd.DataFrame({"Tarih":df3['Tarih']}) #tarih sütunu 
tarih3.head()


# In[110]:


saat3=pd.DataFrame({"Saat":df3['Saat']})  #saat sütunu
saat3.head()


# In[111]:


seviye3=pd.DataFrame({"Seviye":df3['Seviye']})  #seviye sütunu
seviye3.head(10)


# In[112]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[113]:


seviye3.value_counts()


# In[114]:


seviye3.plot.hist()


# In[115]:


#tarih3['Tarih']=pd.to_datetime(tarih3.Tarih,format="%Y%m%d",dayfirst=True)
#tarih3['Tarih']=tarih3['Tarih'].dt.strftime("%Y/%m/%d")                                                                           
#tarih3['Tarih']=pd.to_datetime(tarih3.Tarih,format="%m/%d/%Y %I:%M:%S %p")
df3['Tarih']=pd.to_datetime(df3.Tarih,infer_datetime_format=True)
#import datetime 
#datetime.datetime.strptime(tarih3['Tarih'], '%Y.%m.%d')
df3.head(50)     
      


#tarih3[100:150]
#onuncuay=tarih3.loc[2:1036]
#onuncuay.head(100)
#x=pd.to_datetime(onuncuay.Tarih,infer_datetime_format=True)
#x.head(50)





# In[116]:


sonveri3=pd.concat([ tarih3,saat3,seviye3],axis=1)
sonveri3


# In[117]:


sonveri3=sonveri3[((sonveri3['Seviye']<2 ))]


# In[118]:


plt.plot(sonveri3.Tarih,sonveri3.Seviye,color='grey')


# In[119]:


#sonveri3.to_csv(r'C:\Users\HP\Desktop\aleyna_dataframe3.csv',index=False,header=True)


# In[120]:


df4=pd.read_csv("veriseti4.txt",skiprows=14, sep=" ", usecols=[0,2,7])   #veriyi çekiyoruz
df4.head(50)


# In[121]:


df4.info()   #bilgileri alır.


# In[122]:


df4.isnull().sum()   #toplam kaç kayıp veri olduğunu gösterir.


# In[123]:


df4.dropna(axis=0, how='all',inplace=True) #boşlukları sildik 
df4.head(50)


# In[124]:


#SAAT kolonundaki boş indexleri siliyoruz
df4.dropna(subset=['SAAT'],inplace=True)
df4.head(50)


# In[125]:


# 'unnamed' kolonunda Min ve Maxlı indexleri siliyoruz
filt=df4['Unnamed: 0']=='Min'  
filt|=df4['Unnamed: 0']=='Max'
df4.drop(index=df4[filt].index, inplace=True)
df4.head(100)


# In[126]:


saat4=pd.DataFrame({"Saat":df4['TARIH']})  #saat sütunu
saat4.head(50)


# In[127]:


for i in range(len('Saat')):
    i = i + 19
    saat4['Saat'].replace('00:00','23:59',inplace=True)


# In[128]:


saat4.head(50)


# In[129]:


tarih4=pd.DataFrame({"Tarih":df4['Unnamed: 0']})  #tarih sütunu
tarih4.head()


# In[130]:


tarih4['Tarih']=pd.to_datetime(tarih4.Tarih,infer_datetime_format=True
)
tarih4[232:285]


# In[131]:


seviye4=pd.DataFrame({"Seviye":df4['SAAT']})   #seviye sütunu
seviye4.head()


# In[132]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[133]:


seviye4.value_counts()


# In[134]:


seviye4.plot.hist()


# In[135]:


e=seviye4.sort_values("Seviye")
e


# In[136]:


e.dropna()


# In[137]:


sonveri4=pd.concat([ tarih4,saat4,seviye4],axis=1)
sonveri4


# In[138]:


sonveri4=sonveri4[((sonveri4['Seviye']<4 ))]


# In[139]:


plt.plot(sonveri4.Tarih,sonveri4.Seviye,'g')


# In[140]:


#sonveri4.to_csv(r'C:\Users\HP\Desktop\export_dataframe4.csv',index=False,header=True)


# In[191]:


fig=plt.figure(figsize=(12,4)) 
plt.plot(sonveri.Tarih,sonveri.Seviye,color="blue") 
plt.plot(sonveri2.Tarih,sonveri2.Seviye,'r')
#plt.plot(sonveri3.Tarih,sonveri3.Seviye,color='grey') 
plt.grid(True,color='k',linestyle=':')
plt.title('Su Seviyesi Oranları') 
plt.xlabel('Tarih')
plt.xlim('2017-10-31','2018-04-18') 
plt.ylabel('Seviye')
plt.ylim(0.5,3)


# In[142]:


import pandas as pd


# In[144]:


ayvacik=pd.read_csv('D01M014_AYVACIK.csv',header=0)
print(len(ayvacik))
ayvacik.head()


# In[145]:


#Eksik rowları oluşturuyoruz
datas= {
    'TARİH':['02/28/2018','03/1/2018','03/1/2018','03/1/2018','03/1/2018','03/1/2018','03/1/2018','03/1/2018','03/1/2018','03/1/2018'],
    'SAAT':['11:00:00 PM','12:00:00 AM','1:00:00 AM','2:00:00 AM','3:00:00 AM','4:00:00 AM',
    '5:00:00 AM','6:00:00 AM','7:00:00 AM','8:00:00 AM'],
            
    'Saatlik Yağış':['0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0']
     }
        
eklenecekler=pd.DataFrame(datas)
eklenecekler


# In[146]:


#Oluşturduklarımızı ayvacık verisetine ekliyoruz
ayvacik=ayvacik.append(eklenecekler,ignore_index = True)
ayvacik.info()
len(ayvacik)


# In[147]:


#TARİH VE SAAT KOLONUNU BİRLEŞTİRİYORUZ
ayvacik['TARİH']=ayvacik['TARİH']+' '+ayvacik['SAAT']

ayvacik.head()


# In[148]:


#SAAT KOLONUNU SİLİYORUZ
ayvacik.drop('SAAT',axis=1,inplace=True)
ayvacik.head()


# In[149]:


#TARİH KOLONUNU DÜZELTİYORUZ
#ayvacik['TARİH']=pd.to_datetime(ayvacik.TARİH,format="%m/%d/%Y %I:%M:%S %p")

ayvacik['TARİH']=pd.to_datetime(ayvacik.TARİH,infer_datetime_format=True)
ayvacik.head()


# In[150]:


#Eklediğimiz veriler en sona geldiği için sırasını düzeltmemize gerek
ayvacik.iloc[-1]


# In[151]:


ayvacik=ayvacik.sort_values(by=['TARİH'])      #verileri tarihe göre sıraladım
ayvacik.head()
ayvacik.iloc[-1]


# In[152]:


ayvacik.tail(10)


# In[155]:


beyazkoy=pd.read_csv('D01M004_BEYAZKOY.csv',header=0)
beyazkoy.head()


# In[156]:


#TARİH VE SAAT KOLONUNU BİRLEŞTİRİYORUZ
beyazkoy['TARİH']=beyazkoy['TARİH']+' '+beyazkoy['SAAT']

beyazkoy.head()


# In[157]:


#SAAT KOLONUNU SİLİYORUZ
beyazkoy.drop('SAAT',axis=1,inplace=True)
beyazkoy.head()


# In[158]:


#BEYAZKOY TARİH KOLONUNU DÜZELTİYORUZ
beyazkoy['TARİH']=pd.to_datetime(beyazkoy.TARİH,infer_datetime_format=True)
beyazkoy.head()


# In[159]:


beyazkoy.head(50)


# In[160]:


#SIRA GELDİ AYVACIK VE BEYAZKOYU BİRLEŞTİRMEYE
koyler=pd.merge( 
    ayvacik, 
    beyazkoy,
    on='TARİH',
    how='inner' )
#COLUMNLERİN İSMİNİ DEĞİŞTİRİYORUZ A_YAGIS= AYVACIK     B_YAGIS=BEYAZKOY
koyler=koyler.rename(columns={'Saatlik Yağış':'AYVACIK_YAGIS','YAĞIŞ':'BEYAZKOY_YAGIS'} )
koyler.head()




# In[161]:


D01A031=pd.read_csv('D01A031.csv')
D01A033=pd.read_csv('D01A033.csv')
D01A052=pd.read_csv('D01A052.csv')
print(D01A031.info(),D01A033.info(),D01A052.info())




# In[162]:


#Tarihleri filtreledim
D01A031=D01A031[ (D01A031['Tarih']>="2017-10-31") & (D01A031['Tarih']<"2018-04-19")]
D01A033=D01A033[ (D01A033['Tarih']>="2017-10-31") & (D01A033['Tarih']<"2018-04-19")]
D01A052=D01A052[ (D01A052['Tarih']>="2017-10-31") & (D01A052['Tarih']<"2018-04-19")]


# In[163]:


D01A031.tail(10)


# In[164]:


D01A033.tail(10)


# In[165]:


D01A052.head(10)


# In[166]:


D01A031.info()
D01A031['Tarih']=D01A031['Tarih']+' '+D01A031['Saat']
D01A031.drop(['Saat'],axis=1,inplace=True)
D01A031=D01A031.rename(columns={'Tarih':'TARİH'})
D01A031


# In[167]:


D01A031['TARİH']=pd.to_datetime(D01A031['TARİH'])   
D01A031.info()


# In[168]:


D01A033.info()
D01A033['Tarih']=D01A033['Tarih']+' '+D01A033['Saat']
D01A033.drop(['Saat'],axis=1,inplace=True)
D01A033=D01A033.rename(columns={'Tarih':'TARİH'})
D01A033


# In[169]:


D01A033['TARİH']=pd.to_datetime(D01A033['TARİH'])
D01A033.info()


# In[170]:


D01A052.info()
D01A052['Tarih']=D01A052['Tarih']+' '+D01A052['Saat']
D01A052.drop(['Saat'],axis=1,inplace=True)
D01A052=D01A052.rename(columns={'Tarih':'TARİH'})
D01A052


# In[171]:


D01A052['TARİH']=pd.to_datetime(D01A052.TARİH,infer_datetime_format=True)


# In[172]:


D01A052['TARİH']=pd.to_datetime(D01A052['TARİH'])
D01A052.info()


# In[173]:


koyler.TARİH.astype('datetime64[ns]') 
D01A031['TARİH']=pd.to_datetime(D01A031['TARİH'])
koyler.info()
D01A031.info()


# In[174]:


SonVeri=pd.merge(
    koyler,
    D01A031,
    on='TARİH',
    how='inner',
)


SonVeri


# In[175]:


SonVeri=SonVeri.rename(columns={'Seviye':"D01A031'in seviyesi"})
SonVeri


# In[176]:


D01A033['TARİH']=pd.to_datetime(D01A033['TARİH'])
koyler.info()
D01A033.info()


# In[177]:


SonVeri=pd.merge(
    SonVeri,
    D01A033,
    on='TARİH',
    how='inner',
)


SonVeri


# In[178]:


SonVeri=SonVeri.rename(columns={'Seviye':"D01A033'un seviyesi"})
SonVeri


# In[179]:


D01A052['TARİH']=pd.to_datetime(D01A052['TARİH'])
SonVeri=pd.merge(
    SonVeri,
    D01A052,
    on='TARİH',
    how='inner',
)


SonVeri


# In[180]:


SonVeri=SonVeri.rename(columns={'Seviye':"D01A052'nin seviyesi"})
SonVeri


# In[184]:


SonVeri.to_csv(r'C:\Users\Mr Bcan\Desktop\SonVeri.csv',index=False,header=True)


# In[186]:


SonVeri=SonVeri.rename(columns={"D01A031'in seviyesi":"D01A031"})
SonVeri=SonVeri.rename(columns={"D01A033'un seviyesi":"D01A033"})
SonVeri=SonVeri.rename(columns={"D01A052'nin seviyesi":"D01A052"})
SonVeri


# In[188]:


fig=plt.figure(figsize=(12,4)) 
plt.plot(SonVeri.TARİH,SonVeri.D01A031,color="blue") 
plt.plot(SonVeri.TARİH,SonVeri.D01A033,'r')
plt.plot(SonVeri.TARİH,SonVeri.D01A052,color='grey') 
plt.grid(True,color='k',linestyle=':')
plt.title('AGİ-TARİH') 
plt.xlabel('Tarih')
plt.xlim('2017-10-31','2018-04-18') 
plt.ylabel('Seviye')
plt.ylim(0.5,3)
plt.show()


# In[193]:


fig=plt.figure(figsize=(12,4)) 
plt.plot(SonVeri.TARİH,SonVeri.AYVACIK_YAGIS,color="blue") 
plt.plot(SonVeri.TARİH,SonVeri.BEYAZKOY_YAGIS,'r')
 
plt.grid(True,color='k',linestyle=':')
plt.title('MGİ-TARİH') 
plt.xlabel('Tarih')
plt.xlim('2017-10-31','2018-04-18') 
plt.ylabel('MGİ')
plt.ylim(0,10)


# In[ ]:




