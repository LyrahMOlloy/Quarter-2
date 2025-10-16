def farecalc (dist,rate):
  fare = round((dist*rate),2)
  return fare

dist = float(input("Enter the distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

farefin = farecalc(dist,rate)
print("Total Delivery Fee: ₱", farefin)
