import re


uz_reg1 = "^[0-9]{2} [0-9]{3} [0-9]{2} [0-9]{2}$"
uz_reg2 = "^[+][9][9][8] [0-9]{2} [0-9]{3} [0-9]{2} [0-9]{2}$"
uz_reg3 = "^[8] [0-9]{2} [0-9]{3} [0-9]{2} [0-9]{2}$"

#+7 922 111 05 00
#922 111 05 00
#111 05 00
ru_reg1 = "^[+][7] [0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}$"
ru_reg2 = "^[0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}$"
ru_reg3 = "^[0-9]{3} [0-9]{2} [0-9]{2}$"

class RegionDescriptor:
    def __get__(self, instance):
        return instance.__dict__["_region"]
    def __set__(self, instance, region):
        instance.__dict__["_region"] = region

class PhoneNumberDescriptor:
    def __get__(self, instance):
        return instance.__dict__["_value"]

    def __set__(self, instance, value):
        if instance.__dict__["_region"] == "uz":
            if not any([re.match(uz_reg1, value), re.match(uz_reg2, value), re.match(uz_reg3, value)]):
                raise Exception("Invalid phone number")
            instance.__dict__["_value"] = value
        else:
            if not any([re.match(ru_reg1, value), re.match(ru_reg2, value), re.match(ru_reg3, value)]):
                raise Exception("Invalid phone number")
            instance.__dict__["_value"] = value

class PhoneNumber:
    region = RegionDescriptor()
    number = PhoneNumberDescriptor()

region = input("Choose region(uz/ru): ")
if region in ("uz", "ru"):
    user_phone = input("Enter phone number: ")
else:
    raise Exception("Invalid region")

phone_number = PhoneNumber()
phone_number.region = region
phone_number.number = user_phone

print(phone_number.__dict__)

git init


