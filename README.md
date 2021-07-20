

<h1 align="center">Profile Managment Program</h1>
<h2 align="center">Manages social profiles</h2>

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Interactive mode](#Interactive mode)

## General info
A menu driven program that will allow the user to enter commands and process these commands until the quit command is entered.

The program will store and maintain personal profile information (using a List of Profile objects). 

Personal profile information will be stored in a text file that will be read in when the program commences.

Once the initial profile data has been read in from the file, the program should allow the user to
interactively query and manipulate the profile information.

## Technologies
Project is created with:
*  Python version : 3.8

## Input
--- 
When your program begins, it will read in personal profile information from a file called profiles.txt.
This is a text file that stores profile information for the simple social network.
The person’s given name, family name, email address, and gender are stored on one line and are
separated by the space character.


## Interactive Mode
Your program will enter an interactive mode after the profile information has been read from the file. The following commands are allowed:

1. Summary:
Outputs the contents of the profile list.

2. Add:
Prompts for and reads a person’s email address. If the email address does not already exist (i.e.a match is not found on email address) in the profile list, prompts for and reads the rest of theperson’s details (given name, family name, gender and status) and adds the information to theprofile list (note that the number of friends will be set to zero – no friends are read in at this point).
A message is displayed to the screen indicating that the profile has been successfully added.

3. Remove:
Prompts for and reads the person’s email address. If the email address (profile) is found,it is removed from the list of profiles and a message is displayed to the screen indicating
that this has been done. If the profile is not found in the profiles list, an error message is displayed.

4. Search:
Prompts for and reads the person’s email address and searches for the person in the profile list.
If the person is found in the profile list, the person’s details are displayed to the screen. If the person is not found in the profile list, an error message stating the person has not been found is displayed.

5. Update:
Prompts for reads the person’s email address. If the email (profile) is not found in the profiles list, an error message is displayed to the screen. If the profile with matching email address is found, the following prompt is displayed: 'Update given_name family_name
[status|add_friend|remove_friend]:'

6. Quit:
Causes the program to quit, outputting the contents of the profile list (list of profile objects) to a file.
