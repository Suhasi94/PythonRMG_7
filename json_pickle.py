import json
import pickle
import os
os.chdir(r"C:\Users\User\OneDrive\Desktop\python_rmg_07")

#  dump,dumps - covert python to json  #Serialization or  Marshalling

#  load,loads - covert json to python #Deserialization

data = {"name":"prasana","id":123}

x = json.dumps(data) #serialization or marshalling

print(type(data))
print(x, type(x))
       
y = json.loads(x)  #Deserialization or demarshalling
print(y,type(y))

with open("sample.json","w+") as file:
    json.dump(data,file) #serialization or marshalling
    file.seek(0)
    data = json.load(file) #Deserialization or demarshalling
    print(data,type(data))

# Pickle

data = "hello"
x = pickle.dumps(data) # pickling
print(x,type(x))

y = pickle.loads(x) #unpickling
print(y,type(y))

with open("example.pkl","wb+") as file:
    pickle.dump(data,file) #pickling
    file.seek(0)
    data = pickle.load(file)#unpickling
    print(data)















