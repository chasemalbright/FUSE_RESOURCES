# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Albright, Nathaniel Bush, Joshua Campos, Alan Albiter
# Section:     480
# Assignment:  Lab Assignment 2
# Date:        01 September 2020



initial_distance_meters = 50
final_distance_meters = 615
initial_time_seconds = 30
final_time_seconds = 45
# chosen_time_seconds is the variable name of the number of seconds that we are trying to find the position of given by instructor
chosen_time_seconds = 37

# linear interpolation equation
position_of_car_at_chosen_time = initial_distance_meters + ((chosen_time_seconds - initial_time_seconds) * ((final_distance_meters - initial_distance_meters) / (final_time_seconds - initial_time_seconds)))
print("The position of the car at ", chosen_time_seconds, " seconds is ", position_of_car_at_chosen_time, " meters.")