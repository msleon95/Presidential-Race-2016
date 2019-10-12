# california_elections.py
# Author: Laura Leon
# modified on Dec 4, 2018
# Purpose: Program to demonstrate how to input a California county and
# output the winner of the presidential race from that county
# Program uses open(), readline(), dictionary, print(), for loop,
# rstrip(), split(), max(), range(), int, if conditions, keys() method,
# and input
#

# Open file california_counties.txt
california = open("california_counties.txt")

# Read the header
header = california.readline()

# Create a dictionary containing keys as counties and values as the winner
my_dict={}

# Create the output text
print("*** 2016 Presidential Race ***")
print("State of California")

# For loop through each county and see who won the majority
for line in california:
    # Use split to change the string into a list
    cols=line.rstrip("\n").split("\t")
    # Use max function to find the biggest number of votes
    winner=max(int(cols[1]),int(cols[2]),int(cols[3]))
    # For loop again to find the candidate with the highest number
    for x in range(1,4):
        # Use if condition to test which element has the highest number
        if int(cols[x])==winner:
            # Give variable to the position
            position_winner=x
            # Position 1 is for Clinton
            if position_winner==1:
                my_dict[cols[0]]="Clinton"
            # Position 2 is for Trump
            elif position_winner==2:
                my_dict[cols[0]]="Trump"
            # Position is for Johnson
            elif position_winner==3:
                my_dict[cols[0]]="Johnson"

# Print the county options        
print(my_dict.keys())

# User enters a county
county = input("Enter a California county:")

# Call from the dictionary
print(my_dict[county],"won in",county)

