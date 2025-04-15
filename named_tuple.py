from collections import namedtuple
from typing import NamedTuple

person = namedtuple("Person", "name age gender")

dante = person("Dante", 45, "male")
kurt = person("Kurt", 27, "male")

#asdict
print(dante._asdict())

#replace
kurt= kurt._replace(name = "Kurt Cobain")
print(kurt._asdict())

#make
data = ["Elvis Presley", 42, "male"]
elvis = person._make(data)
print(elvis.name)

#class
class Person(NamedTuple):
    name: str
    age: int
    gender: str = "male"

egor_letov = Person("Egor Letov", 43)
print(egor_letov._asdict())

#fields, field_defaults
print(Person._fields)
print(Person._field_defaults)