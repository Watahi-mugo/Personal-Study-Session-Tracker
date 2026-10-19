# Personal Study Session Tracker
###################################################################################################
# This script allows users to input the subjects they are studying, and the duration they spent on each subject. 
# It will count the total number of sessions, calculate the total time spent studying, and the average time spent per session(tt/count).
# Then give a summary report of the total time spent in studying and the average time a session took.
# Handles invalid inputs and allows the user to exit the program gracefully.
###################################################################################################
total_time = 0
average_t = 0 
count = 0 
session = int(input("Enter the total sessions you are studying: "))
if session <= 0:
    print("If no session studied, exit the program")  
while session > 0:
    subject = input("Enter the subject you are studying:" )    
    duration = int(input("Enter the minutes spent studying: "))
    while duration <= 0:
        duration = int(input("Enter the minutes spent studying: "))
        print("If no session was studied, exit the program.")    
    total_time += duration    
    difficulty = int(input("How difficult was the session? (1-5):"))
    if difficulty < 1 or difficulty > 5:
         print("Invalid input. Please enter a number between 1 and 5.")
    count +=1
    session-= 1
    print("total_time =", total_time, "minutes")
    print("session", session) 
if count != 0:
    print( "total count", count)
    average_t = total_time / count 
    print("The average time per session is:", average_t, "minutes")





    