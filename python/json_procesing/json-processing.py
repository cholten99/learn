# Import librares we need
import json
from pprint import pprint

# Create file handle called nads_fh
route_fh = open("route.json","r")

# Create document object model called nads_dom by reading in data from file via file handle
route_dom = json.loads(route_fh.read())

# Let's start by printing out what we're doing
print "Bus routes"

# Loop through the array that is the value-side of the top level name "bus_routes"
# Each loop through puts a set into top_level_sets in the form of a dict
for top_level_set in route_dom["bus_routes"]:
  print " Route name : " + top_level_set["route_name"]
  print "  Route start time : " + top_level_set["route_start_time"]
  print "  Route end time : " + top_level_set["route_end_time"]
  print "  Stop names :"
  # Loop through the stop names array
  for stop in top_level_set["stop_names"]:
    print "   Name : " + stop

# THE NEXT CHALLANGE WOULD BE TO CREATE AN INSTANCE OF A ROUTE CLASS FOR EACH TOP LEVEL SET IN THE JSON FILE!
