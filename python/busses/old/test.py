#this i sa test for the classes we are creating for busses
from buscompany import Bus_Company
print "testing bus companies"

first_company = Bus_Company()
second_company = Bus_Company()

first_company.set_company_name("0brians_bus0")
first_company.set_company_manager("Stacey")

second_company.set_company_name("crazy bus")
second_company.set_company_manager("Nick El Odeon")

print "details of first company"
print "company name : ", first_company.get_company_name(),  ", Manager: ", first_company.get_company_manager
