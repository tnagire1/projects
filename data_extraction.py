import os
import csv
from collections import Counter
import xml.etree.ElementTree as ET



def extract_permission(file):
    root = ET.parse(file).getroot()
    permissions=[]
    permission=[]
    permission+= root.findall("uses-permission")
    #permission+= root.findall("uses-feature")
    #permission+= root.findall("permission")
    for perm in permission :
     for att in perm.attrib:
        permissions += [ perm.attrib[att]] 
    return (sorted(permissions)) 

def permission_data(path):
 permission_array=[]
 app_permissions={}
 with os.scandir(path) as entries:
    for entry in entries:
     if(os.path.isdir(entry)):
      for f_name in os.scandir(entry):
       if f_name.name.endswith('.xml'):
        permission_for_app=extract_permission(f_name)
        permission_array+=(permission_for_app)
        app_permissions[entry.name] = permission_for_app
 return ([*set(permission_array)],app_permissions)


def write_to_csv(permission,appname):
    with open(filename, 'a', newline="") as file:
          csvwriter = csv.writer(file)
          csvwriter.writerow([appname]+ permission)
          file.close()

def boolean_array(permission_array,permissions):
    vector= [0]*len(permission_array)
    for permission in permissions:
        vector[permission_array.index(permission)]+=1
    return(vector)


path = '/Users/teja/Downloads/data_set'
filename = '/Users/teja/Downloads/data_sets/data_set_features_1.csv'
permission_array,app_permissions=permission_data(path)
#print(app_permissions)
write_to_csv(permission_array,"app_name")
for app_name in app_permissions:
    permissions=app_permissions[app_name]
    #print(app_name)
    #print(boolean_array(permission_array,permissions))
    write_to_csv(boolean_array(permission_array,permissions),app_name)