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
def ret_Output(switch, nameJoin):

    #If user input is equal to 1, print address, otherwise default to phone number
    if switch == 1:
        (street, city, state, zipCode, phone) = nameJoin.split(',')
        print("Street:    {}\nCity:     {}\nState:    {}\nZip Code: {}\n".format(street.title(), city.title(), state.upper(), zipCode))
    
    else:
        (street, city, state, zipCode, phone) = nameJoin.split(',')
        print("Phone Number: {}\n".format(phone))

    return()

#Main function
def main():
    choice = 0
    data = get_Data()

    #Get user input to determine output type, if invalid choice made restart loop
    while choice == 0:
        choice = int(input("Lookup (1) phone numbers or (2) addresses: "))

        #Test user input for valid choice
        if choice == 1:
            valid = True

            #Ask user for name input. If input is found in dictionary keys, print output.
            #If input blank, quit program. Else print error message and start loop over.
            while valid == True:
                name = input("Please enter a space-seperated First and Last name: ").lower()
                if name == "":
                    exit(0)
                if name in data.keys(): #Failing here, takes name, but wont match
                    result = [val.strip() for key, val in data.items() if name in key]
                    result = ''.join(result)
                    ret_Output(choice, result)
                else:
                    print(":::INVALID NAME OR FORMAT ENTERED:::")
                    
        #Test user input for valid choice
        if choice == 2:
            valid = True

            #Ask user for name input. If input is found in dictionary keys, print output.
            #If input blank, quit program. Else print error message and start loop over.
            while valid == True:
                name = input("Please enter a space-seperated First and Last name: ").lower()
                if name == "":
                    exit(0)
                if name in data.keys():
                    result = [val.strip() for key, val in data.items() if name in key]
                    result = ''.join(result)
                    ret_Output(choice, result)
                else:
                    print(":::INVALID NAME OR FORMAT ENTERED:::")

        #If invalid choice made, reset choice and start loop over
        else:
            print(":::INVALID CHOICE:::")
            choice = 0
        

    return(-1)

main()
