val = int(input("HI! Enter your age! "))
startCount = 0 #accumulates sum


for adder in range(1, val + 1):
      startCount += adder  

print("The sum of all numbers from", 1 ,"to", val ,"is:", startCount)