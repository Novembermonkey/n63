from multiprocessing import Process
import time


#multiprocessing
# def lowercase(letter):
#     print(letter.lower(), end="")
#
# def uppercase(letter):
#     print(letter.upper(), end="")
#
# def run(case, line: str = "SilkSonG tomoRrOw"):
#     if __name__ == '__main__':
#         processes = []
#         line = line
#
#         for i in line:
#             if case == "lower":
#                 p = Process(target=lowercase, args=(i,))
#                 processes.append(p)
#                 p.start()
#
#             elif case == "upper":
#                 p = Process(target=uppercase, args=(i,))
#                 processes.append(p)
#                 p.start()
#
#             else:
#                 raise Exception("Invalid case: choose between (lower/upper)")
#             time.sleep(0.1)
#
#         for p in processes:
#             p.join()
#
# run("upper")
#run("lower")


#decorators
# def upper_dec(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
#
# def lower_dec(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.lower()
#     return wrapper
#
# @lower_dec
# def string1(line):
#     return line
#
# @upper_dec
# def string2(line):
#     return line
#
# print(string1("YOU wIll"))
# print(string2("die"))




