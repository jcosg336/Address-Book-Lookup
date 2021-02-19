"""
Program: Database_lookup.py
Date: 2/18/2021
"""

#global varible declaration
directory = dict()

#Function to open file and copy data to a dictonary, then return the dictionary.
#If file not found, print "ERROR MESSAGE 1" and close program
def get_Data():
    try:
        test = open("address.txt")
    except:
        print(":::ERROR MESSAGE 1: FILE NOT FOUND!:::")
        exit(-1)
    else:
        with open("address.txt") as f:
            for line in f:
                (key, value) = [x for x in line.split(',', 1)]
                directory[key.lower()] = value.lower()
            
    return(directory)

#Function to format output and print
def ret_Output(switch, nameJoin, name):

    #If user input is equal to 1, print address, otherwise default to phone number
    if switch == 1:

        (street, city, state, zipCode, phone) = nameJoin.split(',')
        print("\nName:      {}".format(name.title()))
        print("Street:    {}\nCity:     {}\nState:    {}\nZip Code: {}\n".format(street.title(), city.title(), state.upper(), zipCode))
        
    else:
        (street, city, state, zipCode, phone) = nameJoin.split(',')
        print("\nName:          {}".format(name.title()))
        print("Phone Number: {}\n".format(phone))

    return()

#Main function
def main():
    choice = 2
    data = get_Data()
    reLoop = True

    #Get user input to determine output type, if invalid choice made restart loop
    while (choice > 0 and choice < 3):
        choice = int(input("Lookup (1) phone numbers or (2) addresses: "))

        #Test user input for valid choice
        if choice == 1:

            #Ask user for name input. If input is found in dictionary keys, print output.
            #If input blank, quit program. Else print error message and start loop over.
            while reLoop == True:
                
                name = input("Please enter a space-seperated First and Last name:\n4 CHARACTER MINIMUM: ").lower()

                #check user input, if blank quit program
                if name == "":
                    reLoop = False
                    print(":::PROGRAM CLOSING:::")
                    return(-1)

                #if user input is 3 char or more, search input in dictionary, if found call ret_output
                if len(name) >= 4:
                    if any(key.startswith(name) for key in data): #test user input against keys
                        retName = next((key for key in data if key.startswith(name)), None)  #convert data.key to string                  
                        result = [val.strip() for key, val in data.items() if name in key]   #strip value from key found
                        result = ''.join(result)                  #join key value selected into a string type
                        ret_Output(choice, result, retName)       #pass choice, string created from key values, and string of key itself to return output

                    else:  #catch fail, notify user
                        print(":::INVALID ENTRY:::")

                if len(name) < 4:  #user input less than the reqired 3 characters
                        print(":::NAME NOT FOUND OR TOO FEW CHARACTERS:::")
   
        #Test user input for valid choice
        if choice == 2:

            #Ask user for name input. If input is found in dictionary keys, print output.
            #If input blank, quit program. Else print error message and start loop over.
            while reLoop == True:
                name = input("Please enter a space-seperated First and Last name:\n3 CHARACTER MINIMUM:: ").lower()
                if name == "":
                    reLoop = False
                    print(":::PROGRAM CLOSING:::")
                    return(-1)
                if len(name) >= 3:
                    if any(key.startswith(name) for key in data):
                        retName = next((key for key in data if key.startswith(name)), None)
                        result = [val.strip() for key, val in data.items() if name in key]
                        result = ''.join(result)
                        ret_Output(choice, result, retName)

                    else:
                        print(":::INVALID ENTRY:::")

                if len(name) <= 2:
                        print(":::NAME NOT FOUND OR TOO FEW CHARACTERS:::")

        #If invalid choice made, reset choice and start loop over
        else:
            print(":::INVALID CHOICE:::")
            choice = 2

