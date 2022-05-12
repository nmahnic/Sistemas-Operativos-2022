# Importing os module
import os
 
# Creating a child process using fork() method
val = os.fork()
 
# Testing the values returned by fork() method
if val > 0:
    pid = os.getpid()
    print(f"Hi I am Parent Process and my PID is {pid} and PID {val} is my Child Process.")
    
elif val == 0:
    pid = os.getpid()
    print(f"Hi I am Child Process and my PID is {pid}.")
    
else:
    print("Sorry!! Child Process creation has failed...")