import json
l=[i for i in range(1,20) if i%2==0]
lJson=json.dumps(l)
print(lJson)

d={"name":"Jack","age":20,"score":(90,80,89)}
dj=json.dumps(d,sort_keys=True)
print(dj)

import pickle
f=open('1.txt','wb')
pickle.dump(d,f)
f.close()