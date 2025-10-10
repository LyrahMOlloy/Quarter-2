dist = float(input("Enter the distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

fare = round((dist*rate),2)
print("Total Delivery Fee: ₱", fare)
