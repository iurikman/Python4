
## main file

from functions import *

input_letter = input(" w - write new person data \n r - read all \n rstr - read string \n f - find string")
if input_letter == "w":
    write_new_person(input("Surname:"), input("First name:"), input("Second name:"))

if input_letter == "r":
    read_full_list()

if input_letter == "rstr":
    read_one_person(int(input("Number of person:")))

if input_letter == "f":
    find_person(input("Word: "))

