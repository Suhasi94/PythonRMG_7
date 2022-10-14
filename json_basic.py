import os
os.chdir(r"C:\Users\User\OneDrive\Desktop\python_rmg_07")
import json
"""
data = {"name":"abc","id":123}

#print(type(data))
#Serialization
x = json.dumps(data)
#print(x,type(x))

#Derialization

y = json.loads(x)
#print(y,type(y))

with open("sample.json","w+") as file:
    json.dump(data,file)
    file.seek(0)
    data =json.load(file)
    print(data,type(data))
    

###Pickle

import pickle

data = "hello"
x = pickle.dumps(data)
print(x,type(x))

y = pickle.loads(x)
print(y,type(y))

with open("example.pkl","wb+") as file:
    pickle.dump(data,file)
    file.seek(0)
    data = pickle.load(file)
    print(data)

"""




























