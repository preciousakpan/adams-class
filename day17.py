import math
import time
import datetime
import shutil

num = int(input("Enter Digit "))
result = math.sqrt(num)
print (f'The square root of {num} is {result}')

n = math.radians(90)
result2 = math.sin(math.pi/2)
print (result2)

print (math.factorial(4))
time.sleep(5)
print (math.factorial(5))

print(datetime.datetime.now())

source=r'C:\Users\HP\OneDrive\Desktop\ISAAC\day12.py'
destination=r'C:\Users\HP\OneDrive\Desktop\ISAAC\new\day12-copy.py'
shutil.copy(source,destination)
print("Copied Successfully")
