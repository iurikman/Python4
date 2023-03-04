

## Functions


def write_new_person(surname = "Empty", f_name = "Empty", s_name = "Empty"):
    with open('Persons.txt', 'a') as data:
        data.write("\n" + surname + " " + f_name + " " + s_name)

def read_full_list():
    file = open("Persons.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())

def read_one_person(n):
    file = open("Persons.txt", "r")
    print(file.readlines()[n-1])
    file.close()

def find_person(word):
    with open('Persons.txt') as file:
        for num, line in enumerate(file, 1):
            if word in line:
                print(num, line)

def delete_person(n):
    file = open("Persons.txt", "d")

