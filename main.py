"""
Given n as input. Starting from 1 till n print 'Pepsi' if the number is divisible by 3 in following format. Print 'Coke' otherwise
n=5
Expected Output 
Coke-1 
Coke-2 
Pepsi-3 
Coke-4 
Coke-5
"""

num = 10
pt = "Coke"
pt2 = "Pepsi"

for i in range (1,num+1):
  if (i%3==0):
    print(f"{pt2}-{i}")

  else:
    print(f"{pt}-{i}")
