import json
from pprint import pprint
nads_data = open("notifiable-animal-disease-records.json","r")
#print nads_data.read() 
nads_dom = json.loads(nads_data.read())
pprint(nads_dom)