# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_sum(number_list):
    new_sum_list = []
    sum_num = 0
    for number in number_list:
        sum_num += number
        new_sum_list.append(sum_num)
    return new_sum_list



def main():
    sample_list = [1, 2, 3]
    sample_list2 = [1, 20, 30]
    print(cumulative_sum(sample_list))
    print(cumulative_sum(sample_list2))

if __name__ == '__main__':
    main()