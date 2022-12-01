import os
from xml.dom.minidom import parseString
import csv
import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
from collections import Counter as ct
app_permission={}
permission_count={}
app_count={}
 

def extract_permission(file):
 data = '' # string data from file
 with open(file, 'r') as f:
    data = f.read()
 dom = parseString(data) # parse file contents to xml dom
 nodes = dom.getElementsByTagName('uses-permission') # xml nodes named "uses-permission"
 permissions = [] 
 for node in nodes:
    permissions += [node.getAttribute("android:name")] 
 permissions=sorted(permissions)
 return (sorted(permissions)) 


path = '/Users/teja/Desktop/selectedAPKs-decoded'
with os.scandir(path) as entries:
    for entry in entries:
     if(os.path.isdir(entry)):
      for f_name in os.scandir(entry):
       if f_name.name.endswith('.xml'):
         permission=(extract_permission(f_name))
         app_permission[entry.name]=permission

for key,values in app_permission.items():
   app_count[key]=len(values)
   for i in values:
    if i in permission_count:
      permission_count[i] += 1
    else:
     permission_count[i] = 1
sorted_permission_count = (sorted(permission_count.items(), key=lambda x:x[1],reverse=True))
sorted_app_count= (sorted(app_count.items(), key=lambda x:x[1],reverse=True))

print(((sorted_permission_count))[0:10])
print(((sorted_app_count))[0:10])

d = dict(ct(dict(sorted_app_count).values()))
plot_data = sorted(d.items())
plt.plot(*zip(*plot_data))
plt.show()