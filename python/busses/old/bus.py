class Bus(object):
    """Bus class"""
  #missing bus route which is an instance of route
    bus_number = ""
    bus_driver = ""

    #this is the constructor
    def __init__(self, arg):
        pass

    #this is the getter function for bus_number
    def get_bus_number():
     return bus_number

    #this is te setter function for bus_number
    def set_bus_number(new_bus_number):
     bus_number = new_bus_number

    #this is the getter function for bus_driver
    def get_bus_driver():
      return cbus_driver

    #this is te setter function for bus_driver
    def set_bus_driver(new_bus_driver):
     bus_driver = new_bus_driver

class Bus_Company(object):
    """Bus_Company class"""

    company_name = ""
    company_manager = ""

    #LIST OF BUSSES TO BE ADDED

    #this is the constructor
    def __init__(self, arg):
        pass

    #this is the getter function for company name
    def get_company_name(self):
     return company_name

    #this is te setter function for compamny name
    def set_company_name(self, new_name_company):
     company_name = new_name_company

    #this is the getter function for company manager
    def get_company_manager():
      return company_name

    #this is te setter function for compamny manager
    def set_company_manager(self, new_name_manager):
     company_name = new_name_manager


class Route(object):
    """route class"""
   #missing list of stops
    route_name = ""
    route_start_time = ""
    route_end_time = ""

    #this is the constructor
    def __init__(self, arg):
        pass

    #this is the getter function for route name
    def get_route_name(self):
     return route_name

    #this is te setter function for route name
    def set_route_name(self, new_route_name):
     route_name = new_route_name

    #this is the getter function for route_start_time
    def get_route_start_time():
      return route_start_time

    #this is te setter function for route_start_time
    def set_route_start_time(self, new_route_start_time):
     route_start_time = new_route_start_time

     #this is the getter function for route_nd_time
     def get_route_end_time():
       return route_end_time

     #this is te setter function for route_end_time
     def set_route_end_time(self, new_route_end_time):
      route_end_time = new_route_end_time

class Stop(object):
    """Bus_Company class"""

    #dictionary of times to other stops
    stop_name= ""

    #this is the constructor
    def __init__(self, arg):
        pass

    #this is the getter function for stop name
    def get_stop_name(self):
     return stop_name

    #this is te setter function for stop name
    def set_stop_name(self, new_stop_name):
     stop_name = new_stop_name
