# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.


import copy
import sys
import json


def parse_argument():
    """
    parses arguments and returns the passed argument as json object
    :return: 
    """
    arguments = sys.argv
    if len(arguments) != 2:
        print "Argument mismatch"
    json_object = {}
    try:
        json_object = json.loads(arguments[1])
    except Exception, e:
        print ("Error parsing json, %s" % e)
    finally:
        return json_object


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        required_subsets = list()
        for index, value in enumerate(copy.deepcopy(nums)):
            single_set = list()
            single_set.append(value)
            for v in nums[index+1:]:
                if abs(value - v) in [1, 0]:
                    single_set.append(v)
            if max(single_set) != min(single_set):
                required_subsets.append(single_set)
        required_subset_length = 0
        for required_subset in required_subsets:
            subset_length = len(required_subset)
            if subset_length > required_subset_length:
                required_subset_length = subset_length
        return required_subset_length


if __name__ == "__main__":
    num_solver = Solution()
    args = parse_argument()
    if len(args) != 2:
        print 'Argument mismatch, number set expected in"[1,3,2,2,5,2,3,7]" format'
        print 'Using module variable'
        args = [1, 3, 2, 2, 5, 2, 3, 7]
    print num_solver.findLHS(args)
