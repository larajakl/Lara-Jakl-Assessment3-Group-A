"""
Upper and Lower
"""
def count_upper_lower(string : str):
    upper_case_letters = 0
    lower_case_letters = 0
    for i in range(0, len(string)):
        if string[i].isupper() == True:
            upper_case_letters += 1
        elif string[i].islower() == True:
            lower_case_letters += 1
    print(f"No. of Upper case characters: {upper_case_letters}")
    print(f"No. of Lower case characters: {lower_case_letters}")

"""
Check 33
"""

def has_33(list):
    if 3 in list:  # to work on all the strings that include 3 at least once
        for i in range(0, len(list) - 1):  # len(list) - 1 because I check for the last 2 elements of the list in line 23
            if list[i] == 3:
                if list[i] == list[i + 1]:  # this checks if the value after 3 is also a 3
                    return True
                else:
                    return False
    else:  # I used this else statement to return False (instead of None) when a string does not contain any 3.
        return False

# I still wanted need to check for the option where the first occurrence of 3 is not followed by another 3,
# but maybe another occurrence afterwards is, but I did not have time :(


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")
    returned_boolean1 = has_33([1, 3, 3])
    returned_boolean2 = has_33([1, 3, 1, 3])
    returned_boolean3 = has_33([3, 1, 3])
    print(returned_boolean1)
    print(returned_boolean2)
    print(returned_boolean3)
    count_upper_lower("SimoN")
