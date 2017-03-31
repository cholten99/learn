# Import librares we need
import json
from pprint import pprint

# Create file handle called nads_fh
nads_fh = open("route.json","r")

# Create document object model called nads_dom by reading in data from file via file handle
nads_dom = json.loads(nads_fh.read())

# Loop through the array that is the value-side of the top level name "bus_routes"
# Each loop through puts a set into i in the form of a dict
for i in nads_dom["bus_routes"]:
  keys = i.keys()
  for key in keys:
    print key
    
    
"""
    for j in nads_dom[i]:
        print " " + j + " : "# + nads_dom[i][j]
        if j == "stop_name":
            for k in nads_dom[i][j]:
                 print "  " + k
"""