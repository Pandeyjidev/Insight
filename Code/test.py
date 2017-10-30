# Read data
with open('cm_test.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content] 
# print(content[0])

# Put everything in the Dictionary
df = {}
ZIP_CODE={}
TRANSACTION_DT={}
TRANSACTION_AMT={}
OTHER_ID={}
for line in content:
    x = line.split('|')
    # print(x[13:14])
    ZIP_CODE[x[0]] = x[9:10]
    TRANSACTION_DT[x[0]] = x[12:13]
    TRANSACTION_AMT[x[0]] = x[13:14]
    OTHER_ID[x[0]] = x[14:15]
    # df[x[0]] = x[1:]
    # N,ZIP_CODE,TRANSACTION_DT,TRANSACTION_AMT,OTHER_ID = x[0][0], x[0][9], x[0][12],x[0][13],x[0][14] 
keys = df.keys()
print("\n")
print("\n")
print("\n")
print("\n")
# print(CMTE_ID)
print(ZIP_CODE)
# print(TRANSACTION_DT)
# print(TRANSACTION_AMT)
# print(OTHER_ID)

# print(df)

#print(df['C00436725'])
# print(keys)
# print(x)
print("\n")
print("\n")
# # Data filtering
#  df_u ={}
# print(df[keys[0]])
for row in x:
    # print(row[2])
    print("\n")
    # N,ZIP_CODE,TRANSACTION_DT,TRANSACTION_AMT,OTHER_ID = df[row][0], df[row][9], df[row][12],df[row][13],df[row][14] 
    # print(N, ZIP_CODE , TRANSACTION_DT,TRANSACTION_AMT,OTHER_ID )
    #  print(temp1)
    #  df[row] = 
    #  print df_u