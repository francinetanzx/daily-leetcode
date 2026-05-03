"""
788. Rotated Digits

An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].

Example 1:

Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Example 2:

Input: n = 1
Output: 0
Example 3:

Input: n = 2
Output: 1
 

Constraints:

1 <= n <= 104
"""

def rotatedDigits(n: int) -> int:
    """
    Time: O(N)
    Space: O(N)
    """
    valid_digits_mapping = {
        0: 0,
        1: 0, 
        2: 1, 
        3: 0,
        4: 0, 
        5: 1, 
        6: 1,
        7: 0,
        8: 0,
        9: 1
    }
    count_of_good_numbers = 0
    tracker = [-1] * n

    for i in range(1, n + 1):
        # if i < 10, there is no prefix to check, validate and move on
        if i < 10: 
            count_of_good_numbers += 1 if valid_digits_mapping[i] else 0
            tracker[i-1] = valid_digits_mapping[i]
            continue 

        # get prefix (all except last digit) and last digit
        all_except_last_digit = i // 10 
        last_digit = i % 10

        # check all_except_last_digit from tracker 
        is_prefix_good = tracker[all_except_last_digit - 1]

        # check last_digit from valid_digits_mapping 
        is_last_digit_good = valid_digits_mapping[last_digit]

        if is_prefix_good and is_last_digit_good: 
            count_of_good_numbers += 1
            tracker[i-1] = 1
        else:
            tracker[i-1] = 0
    
    return count_of_good_numbers

