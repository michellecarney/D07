# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(user_list):
    capitalized_list = []
    for item in user_list:
        if type(item) == type(capitalized_list):
            newitem = item[0]
            capitalized_list.append(newitem.capitalize())
        else:
            capitalized_list.append(item.capitalize())
    return capitalized_list


def main():
    sample_list = ['apple', ['bear'], 'cat']
    print(capitalize_nested(sample_list))

if __name__ == '__main__':
    main()