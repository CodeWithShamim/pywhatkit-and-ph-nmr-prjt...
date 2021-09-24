#track phone number..........

import phonenumbers
from phonenumbers import geocoder




number = input("Enter your phone number with country code :-")


s = phonenumbers.parse(number, "CH")
r = geocoder.description_for_number(s, "en")
print(r)

#carrier
from phonenumbers import carrier
r = carrier.name_for_number(s, "en")
print(r)
