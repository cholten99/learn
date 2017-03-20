#this i sa test for the classes we are creating for busses
from bus import *
print "Testing bus companies"

first_company = Bus_Company()
second_company = Bus_Company()

first_company.set_company_name("0brians_bus0")
first_company.set_company_manager("Stacey")

second_company.set_company_name("crazy bus")
second_company.set_company_manager("Nick El Odeon")

print "Details of first company"
print "  Company name: ", first_company.get_company_name()
print "  Manager: ", first_company.get_company_manager()
print "Details of second company"
print "  Company name: ", second_company.get_company_name()
print "  Manager: ", second_company.get_company_manager()

