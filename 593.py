# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
#
# The coordinate (x,y) of a point is represented by an integer array with two integers.
import itertools
import sys
import json


def parse_argument():
    """
    parses arguments and returns the passed argument as json object
    :return: 
    """
    args = sys.argv
    if len(args) != 2:
        print "Argument mismatch"
    json_object = {}
    try:
        json_object = json.loads(args[1])
    except Exception, e:
        print ("Error parsing json, %s" % e)
    finally:
        return json_object


class Solution(object):
    def get_distance(self, point1, point2):
        """
        computes distance between two points in two dimensional cartesian coordinates
        :param point1: 2D point(x, y)
        :param point2: 2D point(x, y)
        :return: float
        """
        return abs(((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5)

    def valid_square(self, four_points):
        for option in itertools.permutations(four_points):
            p1, p2, p3, p4 = option
            side_1 = self.get_distance(p1, p2)
            side_2 = self.get_distance(p2, p3)
            side_3 = self.get_distance(p3, p4)
            side_4 = self.get_distance(p1, p4)
            diagonal_1 = self.get_distance(p1, p3)
            diagonal_2 = self.get_distance(p2, p4)
            valid_square = side_1 == side_2 == side_3 == side_4 and diagonal_1 == diagonal_2
            if valid_square:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    argument = parse_argument()
    if len(argument) != 4:
        print 'Argument mismatch, four points expected as argument like "[[0, 0], [1, 1], [1, 0], [0, 1]]"'
        print 'Using module variable as an argument'
        argument = [[0, 0], [1, 1], [1, 0], [0, 1]]
    print s.valid_square(argument)
