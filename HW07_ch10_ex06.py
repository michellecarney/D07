# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(user_list):
    for i in range(1, len(user_list)):
        if user_list[i] < user_list[i-1]:
            return False
        else:
            return True



def main():
    pass

if __name__ == '__main__':
    main()