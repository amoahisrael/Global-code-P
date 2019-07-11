def get_name():
    name=input("Please enter your name:")
    return name


def get_age():
    age=input("Please enter your age:")
    return age
    


def printinfo( name, age ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return;
printinfo( get_age(),get_name() )