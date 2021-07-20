

##--Libaries Imported--##

import list_function
import profile
profile_list = []
filename = "profiles.txt"  # file having data

##--Information about the Author or who wrote the Code.--##
print("File     : Project_Base_social.py")
print("Author   : Kashif")
print("Email ID : kashifmehdi53@gmail.com")
print("This is my own work as defined by the Codequest Academic Misconduct Policy.\n")


##--Function reading the Profile.txt file--##
def read_file(filename, profile_list):
    f = open(filename, "r")
    line = f.readlines()
    for i in range(len(line)):
        line[i] = line[i].replace("\n", "")

    i = 0
    while(i < len(line)):
        profile_list.append(profile.Profile(line[i].split(" ")[0], line[i].split(" ")[
                            1], line[i].split(" ")[2], line[i].split(" ")[3]))
        i = i+1
        profile_list[-1].set_status(line[i])
        i = i+1
        c = int(line[i])
        profile_list[-1].set_number_friends(c)
        i = i+1
        j = i
        f_list = []
        for k in range(j, j+c):
            f_list.append(line[k])

        profile_list[-1].set_friends_list(f_list)
        i = i+c

    return profile_list


profile_list = read_file(filename, profile_list)

##--Function to Display Summary--##


def display_summary(profile_list):
    print("==============================================================================")
    print("                   Profile Summary                ")
    print("==============================================================================")

    for i in range(len(profile_list)):
        print(
            "------------------------------------------------------------------------------")
        print(profile_list[i].get_given_name()+" " +
              profile_list[i].get_family_name()+" "+"("+profile_list[i].get_gender()+" "+"| "+profile_list[i].get_email()+")")
        print("-", profile_list[i].get_status())
        if profile_list[i].get_number_friends() > 0:
            print(
                "- Friends ({}): ".format(profile_list[i].get_number_friends()))
            for element in profile_list[i].get_friends_list():
                print("   "+element)
        else:
            print("- No friends yet...")

    main_menu()


##--Function of Main Menu--##

def main_menu():

    while True:
        try:
            selection = input(
                "Please enter your choice [summary|add|remove|search|update|quit]: ")

            if selection == 'summary':
                display_summary(profile_list)
                break
            elif selection == 'add':
                add_profile(profile_list)
                break
            elif selection == 'remove':
                remove_profile(profile_list)
                break
            elif selection == 'search':
                search_profile(profile_list)
                break
            elif selection == 'update':
                update_profile(profile_list)
                break
            elif selection == 'quit':
                break
            else:
                print("Not a valid command -- Please try again")

        except:
            print("Not a valid command- try again")
    exit


##--Function to write in the file--##

def write_to_file(profile_list):
    f = open('new_profiles.txt', "w+")
    for i in range(len(profile_list)):
        f.write(profile_list[i].get_given_name()+" " + profile_list[i].get_family_name() +
                " "+profile_list[i].get_email()+" "+profile_list[i].get_gender()+"\n")
        f.write(profile_list[i].get_status()+"\n")
        f.write(str(profile_list[i].get_number_friends())+"\n")
        if profile_list[i].get_number_friends() > 0:
            for element in profile_list[i].get_friends_list():
                f.write(element+"\n")


##--Function to find the profile--##

def find_profile(profile_list, email):

    emails = []
    for profile in profile_list:
        emails.append(profile.get_email())

    if email not in emails:
        return -1
    else:
        return emails.index(email)


##--Function to add profile--##

def add_profile(profile_list):
    print("\n---In Add Command---")
    email = input("Please enter the email address:")
    r = find_profile(profile_list, email)

    if r == -1:
        given_name = input("Please enter the given name: ")
        family_name = input("Please enter the family name: ")
        gender = input("Please enter the gender: ")
        status = input(" Please enter the current status: ")

        new_profile = profile.Profile(given_name, family_name, gender, status)

        profile_list.append(new_profile)
        print(f"Successfully added {email} to the Profile.")
    else:
        print(f"{email} already exists in the profile!!!")

    main_menu()


##--Function to remove profile--##

def remove_profile(profile_list):
    print("\n---In Remove Command---")
    email = input("Please enter the email address: ")
    r = find_profile(profile_list, email)
    if r == -1:
        print(f"{email} not found in the profiles!!!")
    else:
        del profile_list[r]
        print(f"Successfully removed {email} from the profile.")

    main_menu()


##--Function to search profile--##

def search_profile(profile_list):
    print("\n---In Search Command---")
    email = input("Please enter the email address: ")
    r = find_profile(profile_list, email)
    if r == -1:
        print(f"{email} not found in the profiles!!!")
    else:
        i = r
        print(profile_list[i].get_given_name()+" "+profile_list[i].get_family_name() +
              " ("+profile_list[i].get_gender()+" | " + profile_list[i].get_email()+")")
        print("- "+profile_list[i].get_status())
        print("- Friends ({})".format(profile_list[i].get_number_friends()))
        for ele in profile_list[i].get_friends_list():
            print("    " + ele)

    main_menu()

##--Function to update profile--##


def update_profile(profile_list):  # sourcery no-metrics
    print("\n---In Update Command---")
    email = input("Please enter the email address: ")
    r = find_profile(profile_list, email)
    if r == -1:
        print(f"{email} not found in the profiles!!!")
    else:
        c = input(
            f"Update{profile_list[r].get_given_name()}{profile_list[r].get_family_name()} [status|add_friend|remove_friend]: ")

        #### To change the status of person ####
        if c == 'status':
            status = input("Please enter the new status: ")
            profile_list[r].set_status(status)
            print(
                f"Updated a status for {profile_list[r].get_given_name()} {profile_list[r].get_family_name()}")
            i = r
            print(profile_list[i].get_given_name()+" "+profile_list[i].get_family_name(
            )+" ("+profile_list[i].get_gender()+" | " + profile_list[i].get_email()+")")
            print("- "+profile_list[i].get_status())
            print(
                "- Friends ({}):".format(profile_list[i].get_number_friends()))
            for ele in profile_list[i].get_friends_list():
                print("    " + ele)

        #### To Add a new friend ####
        elif c == 'add_friend':
            email_2 = input(
                "Please enter the email address of the friend to add: ")
            p = find_profile(profile_list, email_2)
            if p == -1:
                print(f"{email_2} not found in the profiles!!!")
            else:
                f_list = profile_list[r].get_friend_list()
                if email_2 in f_list:
                    print(
                        f"{profile_list[r].get_given_name()} is already a friend.")
                else:
                    f_list.append(email_2)
                    profile_list[r].set_friends_list(f_list)
                    print(
                        f" Added {profile_list[r].get_given_name()} updated profile is: ")
                    i = r
                    print(profile_list[i].get_given_name()+" "+profile_list[i].get_family_name(
                    )+" ("+profile_list[i].get_gender()+" | " + profile_list[i].get_email()+")")
                    print("- "+profile_list[i].get_status())
                    print(
                        "- Friends ({}):".format(profile_list[i].get_number_friends()))
                    for ele in profile_list[i].get_friends_list():
                        print("    " + ele)

        #### To remove a friend ####
        elif c == 'remove_friend':
            email_3 = input(
                "Please enter the email address of the friend to add: ")
            o = find_profile(profile_list, email_3)
            if o == -1:
                print(f"{email_3} not found in the profiles!!!")
            else:
                f_list1 = profile_list[r].get_friend_list()
                if email_3 in f_list1:
                    print(
                        f"{email_3}'s is not a friend of {profile_list[r].get_given_name()} ")
                else:
                    f_list1.remove(email_3)
                    profile_list[o].set_friends_list(f_list1)
                    print(f" Removed {email_3} updated profile is: ")
                    i = r
                    print(profile_list[i].get_given_name()+" "+profile_list[i].get_family_name(
                    )+" ("+profile_list[i].get_gender()+" | " + profile_list[i].get_email()+")")
                    print("- "+profile_list[i].get_status())
                    print(
                        "- Friends ({}):".format(profile_list[i].get_number_friends()))
                    for ele in profile_list[i].get_friends_list():
                        print("    " + ele)

        else:
            print("Not a valid command - returning to the main menu!")

    main_menu()


##--calling the main menu--##
main_menu()
##--calling the write function--##
#--will write all the new data--#
write_to_file(profile_list)

# Terminating Message
print("\n\n--- Program terminating ---\n\n")
