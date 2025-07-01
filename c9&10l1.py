#Jacob Sexton 7/1/25

name = input("Enter your full name: ")

name = name.strip()

if ',' in name:
    #if it's already the right format
    parts = name.split(',')
    #same thing as below, but you have to split the string from the , making it 2 different parts
    last = parts[0].strip().capitalize()
    first = parts[1].strip().capitalize()
    print(last + ", " + first)
else:
    #this assumes that you put in in First name first and last name last
    parts = name.split()
    #this will split the names into parts so that I can capitilize just the first letter
    #of both the first and last name.
    first = parts[0].strip().capitalize()
    last = parts[-1].strip().capitalize()
    print(last + ", " + first)
