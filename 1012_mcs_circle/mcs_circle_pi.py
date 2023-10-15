import random
import math 

trials = int(input("Number of trials: "))
accuracy_list = []
darts_list = [] 

a = 0
while a < trials:
  a = a + 1 
  
  number_darts = int(input("Total number of darts: "))
  darts_list.append(number_darts)
  darts_thrown = 0
  in_circle = 0
  
  while darts_thrown < number_darts:
    darts_thrown += 1
    x = random.random()
    y = random.random()

    if x*x + y*y < 1:
      in_circle += 1
  
  #area = pi * r^2 = pi 
  pi_value = (in_circle * 4.0)/number_darts
  print("Your value of pi: " + str(pi_value))
  
  percent_error = abs((pi_value - math.pi)/math.pi) * 100.0
  accuracy_list.append(percent_error)
  print("% error between your value of pi: " + str(percent_error) + "% ")
