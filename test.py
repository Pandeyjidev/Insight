with open('cm.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content] 
# print(content)
df = {}
for line in content:
    x = line.split('|')
    df[x[0]] = x[1:]
keys = df.keys()
#print(df.keys('C00436725'))
print(keys)