class colorz:
    RED = '\033[91m'
    LUVGREEN = '\033[92m'
    PURPLE = "\033[95m" 
    LUVRESET = "\033[0m"
    CYAN = 	"\033[96m"

print(colorz.LUVGREEN + "Travel Destination Lister + Updater" + colorz.LUVRESET)
dest = []
#taking in first input
print(colorz.PURPLE + "Please enter your 5 travel destinations!" + colorz.LUVRESET)
for i in range(5):
    loc = input("Destination " + str(i+1) +": ")
    dest.append(loc)

#displaying the destinations
print(colorz.CYAN + "Current Travel Destinations:" + colorz.LUVRESET)
for y in range(len(dest)):
    print(str(y+1)+".", dest[y])

#checking if user wants to updat 2nd and 5th destinations
print(colorz.PURPLE + "Do you wish to update the 2nd and 5th destinations?" + colorz.LUVRESET)
selec = input("Enter Y for yes or N for no: ").capitalize()

#what will happen if user selects either Y or N
if selec == 'Y':
    del dest[1]
    newDest2 = input("Enter your new 2nd destination: ")
    dest.insert(1, newDest2)
    del dest[4]
    newDest5 = input("Enter your new 5th destination: ")
    dest.insert(4, newDest5)
else:
    print("You may now exit this program.")

#displaying updated destinations
print(colorz.CYAN + "Updated Travel Destinations: " + colorz.LUVRESET)
for y in range(len(dest)):
    print(str(y+1)+".", dest[y])

print(colorz.LUVGREEN + "Thank you for using this program!" + colorz.LUVRESET)