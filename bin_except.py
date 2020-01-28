# Author: Mahtab Zilaie
# Date: January 28, 2020
# Description:  binary search function that when the target value is not in the list,
# raises a TargetNotFound exception

from math import floor


def TargetNotFound(Exception):

    """raised when target not found in list"""

    pass

def bin_except(list, target):

    """searches a_list for an occurrence of target"""

    first = 0                   # beginning of list
    last = len(list) - 1        # End of list
    while first <= last:
        middle = floor((first + last) / 2)    # middle of list
        if list[middle] == target:
            return middle                    # situation if target == middle of list
        if list[middle] > target:            # if middle is greater than target
            last = middle - 1                # last now equals middle of the list minus 1
        else:
            first = middle + 1               # else the beginning of list is now the middle plus 1
    raise TargetNotFound                  # raise the exception


