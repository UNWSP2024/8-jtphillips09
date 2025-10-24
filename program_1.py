def initials_generator(personsName):

    personsInitials = ""
    #    Add your logic here
    name_parts = personsName.split()
    for part in name_parts:
        personsInitials += part[0].upper() + ". "

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name')

initials = initials_generator(personsName)

print(initials)
