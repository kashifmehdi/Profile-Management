import list_function
import profile
profile_list = []
filename = 'profiles.txt'


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
        #f_list = line[i: i+c]
        profile_list[-1].set_friends_list(f_list)
        i = i+c

    return profile_list


profile_list = read_file(filename, profile_list)


def main_menu():
    while True:
        try:
            selection = input(
                'Please enter choice [summary|add|remove|search|update|quit]: ')
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
                print('Not a valid command - please try again.')
                main_menu()

        except:
            print('Not a valid command - please try again.')
    exit


# Function display_summary() - place your own comments here...  : )
def display_summary(profile_list):
    print('==============================================================================')
    print('Profile Summary')
    print('==============================================================================')

    for i in range(len(profile_list)):
        print(
            '------------------------------------------------------------------------------')
        print(profile_list[i].get_given_name()+" "+profile_list[i].get_family_name() +
              " ("+profile_list[i].get_gender()+" | " + profile_list[i].get_email()+")")
        print("- "+profile_list[i].get_status())
        if profile_list[i].get_number_friends() > 0:
            print(
                "- Friends ({})".format(profile_list[i].get_number_friends()))
            for ele in profile_list[i].get_friends_list():
                print("    " + ele)
        else:
            print("- no friends yet...")

    main_menu()


# Function write_to_file() - place your own comments here...  : )
def write_to_file(profile_list):
    f = open("new_profiles.txt", "w+")
    for i in range(len(profile_list)):
        f.write(profile_list[i].get_given_name()+" "+profile_list[i].get_family_name(
        )+' '+profile_list[i].get_email()+" "+profile_list[i].get_gender()+"\n")
        f.write(profile_list[i].get_status()+"\n")
        f.write(str(profile_list[i].get_number_friends())+"\n")
        if profile_list[i].get_number_friends() > 0:
            for ele in profile_list[i].get_friends_list():
                f.write(ele+"\n")


# Function find_profile() - place your own comments here...  : )
def find_profile(profile_list, email):

    emails = []
    for i in range(len(profile_list)):
        emails.append(profile_list[i].get_email())

    r = list_function.find(emails, email)
    return r


# Function add_profile() - place your own comments here...  : )
def add_profile(profile_list):
    email = input('Please enter email address: ')
    r = find_profile(profile_list, email)

    if r == -1:
        given_name = input("Please enter given name: ")
        family_name = input("Please enter the family name: ")

        gender = input("Please enter gender: ")
        status = input("Please enter current status: ")

        new_profile = profile.Profile(
            given_name, family_name, email, gender, status)

        profile_list.append(new_profile)
        print("Successfully added {} to the profiles.".format(email))

    else:
        print("{} already exists in the profile".format(email))

    main_menu()


# Function remove_profile() - place your own comments here...  : )
def remove_profile(profile_list):
    email = input('Please enter email address: ')
    r = find_profile(profile_list, email)

    if r == -1:
        print("{} is not found in profiles.".format(email))

    else:
        del profile_list[r]
       # print("Successfully removed {} from profiles.".format(email))
        print("Successfully removed {} form profiles.".format(email))

    main_menu()


def search_profile(profile_list):
    email = input('Please enter email address: ')
    r = find_profile(profile_list, email)
    if r == -1:
        print('{} is not found in profiles.'.format(email))

    else:
        i = r
        print(profile_list[i].get_given_name()+" "+profile_list[i].get_family_name() +
              " ("+profile_list[i].get_gender()+" | " + profile_list[i].get_email()+")")
        print("- "+profile_list[i].get_status())
        print("- Friends ({})".format(profile_list[i].get_number_friends()))
        for ele in profile_list[i].get_friends_list():
            print("    " + ele)

    main_menu()


def update_profile(profile_list):
    email = input('Please enter email address: ')

    r = find_profile(profile_list, email)
    if r == -1:
        print('{} is not found in profiles.'.format(email))

    else:
        c = input('Update {} {} [status|add_friend|remove_friend]: '.format(
            profile_list[r].get_given_name(), profile_list[r].get_family_name()))
        if c == 'status':
            status = input("Please enter the new status: ")
            profile_list[r].set_status(status)
            print("Updated status for {} {}:".format(
                profile_list[r].get_given_name(), profile_list[r].get_family_name()))
            i = r
            print(profile_list[i].get_given_name()+" "+profile_list[i].get_family_name(
            )+" ("+profile_list[i].get_gender()+" | " + profile_list[i].get_email()+")")
            print("- "+profile_list[i].get_status())
            print(
                "- Friends ({}):".format(profile_list[i].get_number_friends()))
            for ele in profile_list[i].get_friends_list():
                print("    " + ele)

        elif c == 'add_friend':
            email_2 = input('Please enter email address of friend to add:  ')
            p = find_profile(profile_list, email_2)
            if p == -1:
                print('{} is not found in profiles.'.format(email_2))
            else:
                f_list = profile_list[r].get_friends_list()
                if email_2 in f_list:
                    print("{} is already a friend:".format(
                        profile_list[p].get_given_name()))
                else:
                    f_list.append(email_2)
                    profile_list[r].set_friends_list(f_list)
                    print("Added {} updated profile is:".format(
                        profile_list[p].get_given_name()))
                    i = r
                    print(profile_list[i].get_given_name()+" "+profile_list[i].get_family_name(
                    )+" ("+profile_list[i].get_gender()+" | " + profile_list[i].get_email()+")")
                    print("- "+profile_list[i].get_status())
                    print(
                        "- Friends ({}):".format(profile_list[i].get_number_friends()))
                    for ele in profile_list[i].get_friends_list():
                        print("    " + ele)

        elif c == 'remove_friend':
            email_3 = input(
                'Please enter email address of friend to remove:  ')
            o = find_profile(profile_list, email_3)
            if o == -1:
                print('{} is not found in profiles.'.format(email_3))
            else:
                f_list1 = profile_list[r].get_friends_list()
                if email_3 not in f_list1:
                    print("{} is not {}'s friend:".format(
                        email_3, profile_list[r].get_given_name()))

                else:
                    f_list1.remove(email_3)
                    profile_list[o].set_friends_list(f_list1)
                    print("removed {} updated profile is:".format(email_3))
                    i = r
                    print(profile_list[i].get_given_name()+" "+profile_list[i].get_family_name(
                    )+" ("+profile_list[i].get_gender()+" | " + profile_list[i].get_email()+")")
                    print("- "+profile_list[i].get_status())
                    print(
                        "- Friends ({}):".format(profile_list[i].get_number_friends()))
                    for ele in profile_list[i].get_friends_list():
                        print("    " + ele)

        else:
            print('Not a valid command - returning to main menu.')

    main_menu()


main_menu()

write_to_file(profile_list)

# Terminating message
print("\n\n-- Program terminating --\n")
