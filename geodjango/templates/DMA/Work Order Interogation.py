import pandas as pd

wd = r'C:\Users\Joshua.Pocock\Documents'

fp = wd + '\WorkOrders.csv'
df_WO = pd.read_csv(fp, sep = ',', encoding = "ISO-8859-1")

fp = wd + '\WorkRequests.csv'
df_WR = pd.read_csv(fp, sep = ',', encoding = "ISO-8859-1")

print(list(df_WO))
print(list(df_WR))

df_WO = df_WO[['WORK_ORDER','WO_DESC','WO_TYPE','WORK_GROUP','REQUEST_ID']]
df_WR = df_WR[['REQUEST_ID','SHORT_DESC_1','WORK_GROUP']]

df_WO['REQUEST_ID'] = df_WO['REQUEST_ID'].astype(str).astype(int)

print(df_WO.dtypes)
print(df_WR.dtypes)


#df_join = pd.DataFrame.join(df_WO,df_WR, on = 'REQUEST_ID', how = {'left'})

print("break")
