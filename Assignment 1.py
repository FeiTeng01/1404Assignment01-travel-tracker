"""
This Program is for users to track places they wish to visit and places they have visited.
Name: Fei Teng
Date: Augst 25 2019


"""
menu ="""
The menu of this program is shown below:
L - List places
A - add new places
M - Mark a visited place
Q- quit
"""

# Menu and choises printing function #
def main():
    print("Welcome to travel tracker Ver 1.0 - Fei Teng ")
    print(menu)                                                    #This is for printing menu 
    choice = input("Please Enter your choice"). upper()            # asking about the input for choice been made.
    All_Places = loading_plc()                                     #function connect to each other by using this.
    while choice != "Q" :                                          # if choice is Q, it will process end.

        if choice == "L":                                          #link the choice L to the list_places function
            List_Places(All_Places)

        elif choice == "A":                                        #link the choice A to the added_newplaces function
            All_Places.append(added_newplaces())

        elif choice == "M":                                        #link the choice M to the visited_places function
           visited_places(All_Places)

        else:                                                      #text displayed when entering other choices.
            print("Sorry, the choice you have entered is invalid, please enter a valid choice.")

        print(menu)
        save_to_file(All_Places)
       print("places saved to",'places.csv',"\n updated to places.csv, have a nice day.")

#CSV function #
def loading_plc():           
    All_Places = []                                             #using list to achieve data saving
    places_csv = open('places.csv','r')                         #open the file with read mode.
    for line in places_csv:                                     #use for loop
        line = line.strip("\n")                                 #for line striping
        place_name_country_priority = line.split(",")           #for spliting the line
        All_Places.append(place_name_country_priority)          #define the data format to be saved.
    places_csv.close()                                          #close the file
    return All_Places



#Travel tracker display function

def List_Places(All_Places):                    
    count = 0                                        #declare the variable and start from 0
    for i in range(len(All_Places)):                 #using for loop with constant i
        if All_Places[i][3] == "n":                  # This is to check the situation of the place
            count += 1                               #If it's been visited, count then + 1
            symbol = "*"                             #Add the label to the visited places.
        else:
            symbol = " "                             #else for not been visited place, hence add ""
        print(" ", symbol, str(i) + ".", "", end="")    # This is to show the result
        for k in range(len(All_Places[i]) - 2):           # add the dash before country
            if k == 1:              
                dash = "in"
            else:
                dash = ""                                 #else add the space
            print(dash, "{:30}".format(All_Places[i][k]), end=" ")    #organising format
        print("priority {:4}".format(All_Places[i][-2]))             
    if count == 0:
        print("No places left to visit. Why not add a new place")
    print(len(All_Places), "places.", "You still want to visit", count,"places" )      #show the count of visited places   

#visited places marking function#

def visited_places(All_Places):                          # This is to mark a place as visited
    count = 0                                            # first to declare the variable
    for i in range(len(All_Places)):                     #use the for loop with constant i
        if All_Places[i][3] == "n":                      # cheak the status of the place
            count += 1                                   #count +1 if it's been visited
            symbol = "*"                                  #add symbol
        else:
            symbol = " "                                           
        print(" ", symbol, str(i) + ".", "", end="")             #to show the result
        for k in range(len(All_Places[i]) - 2):                    
            if k == 1:
                dash = "in"
            else:
                dash = ""
            print(dash, "{:30}".format(All_Places[i][k]), end=" ")
        print("(pripority {:4})".format(All_Places[i][-2]))
    if count == 0:
        print("No unvisited places")
        return All_Places
        return main()


    elif count >= 0:
        print(len(All_Places) - count, "  places ,", "You still want to visit ",count, "places")  
    place_number = vari_number("Enter the number of a place to mark as visited\n>>> ")           #asking the code which states the city
    if All_Places[place_number][3] == "v":                                                       # show the related info
        print("You have already visited", All_Places[place_number][0])
    else:
        All_Places[place_number][3] = "v"                                                   #else statement for the place to be marked as visited
        print(All_Places[place_number][0], "in", All_Places[place_number][1], "visited")        # print visited places
        return All_Places


#variable determine function (refer to line 101
def vari_number(choice):                     
    valid = False
    while not valid:
        try:
            input_number = int(input(choice))     #connet to the input and make this as a number
            if input_number < 0:            
                print("Sorry, please enter a vaild number, Number must be >= 0")
            elif input_number >= 4:              
                print("place number not in the list")
            else:
                return input_number   # ask again
        except ValueError:            #except error
            print("Invalid input; enter a valid number")

#add new places function#
def added_newplaces():                              
    added = []                                                 #create list
    place_name = type_input("Please enter the name of the place: ")                          #place name
    place_country = type_input("Please enter the Country of the place: ")                    #place country
    place_priority = str(number_priority("Please enter the priority of the place: "))        #place priority
    added.append(place_name)
    added.append(place_country)
    added.append(place_priority)       
    added.append("n")                             #input the above information to the travel tracker
    print(place_name, "in", place_country, "(priority {:4})".format(place_priority),
          "added to Travel Tracker")
    return added


def type_input(choice):
    type_string = input(choice)
    while len(type_string) == 0:
        print("Sorry, your input should not be blank.")
        type_string = input(choice)
    return type_string.title()

def number_priority(choice):
    vaild = False
    while not vaild:
        try:
            typein_number = int(input(choice))
            if typein_number < 0:
                print("Sorry, the number has to be greater than 0")
            else:
                return typein_number
        except ValueError:
            print("Your input is invalid,Please enter a valid number.")






def save_to_file(all_places):   # This function is used to write the travel tracker to the csv file
    final_save = open("places.csv", 'w')
    for i in range(len(all_places)):
        if i != 0:
            print("\n", end="", file=final_save)
        for k in range(len(all_places[i])):
            final_save.write(all_places[i][k])
            if k != 3:                print(",", end="", file=final_save)
    final_save.close()   # Close the csv file


if __name__ == '__main__':
    main()







