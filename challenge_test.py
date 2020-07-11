#!/usr/bin/env python3

import unittest
from challenge import TSP


def test_data():
    """
    test_data calculates our test data model for tests.
    The calculated data is the same as in: https://developers.google.com/optimization/routing/tsp#program1
    I wanted to make sure, that my calculation is correct.
    Furthermore I have added a few parameters to the data model, like the city names and the TSP size
    """
    data = {}
    data['cities'] = [
        'New York', 'Los Angeles', 'Chicago', 'Minneapolis', 'Denver',
        'Dallas', 'Seattle', 'Boston', 'San Fransisco', 'St. Louis', 'Houston',
        'Phoenix', 'Salt Lake City'
    ]
    data['tsp_size'] = len(data['cities'])
    # The yapf: disable comments turns off yapf python code formatting,
    # We don't want that our distance_matrix looks ugly, when we have to look at it :)
    data['distance_matrix'] = [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    ]  # yapf: disable
    data['num_routes'] = 1
    data['depot'] = 0
    return data

class TestMain(unittest.TestCase):

    def test_result(self):
        """
        test_result tests our TSP implementation against the test data provided by Google.
        """
        # Our expected result as stated on: https://developers.google.com/optimization/routing/tsp#solution1
        expected = {'route': ['New York',
            'Boston',
            'Chicago',
            'Minneapolis',
            'Denver',
            'Salt Lake City',
            'Seattle',
            'San Fransisco',
            'Los Angeles',
            'Phoenix',
            'Houston',
            'Dallas',
           'St. Louis',
           'New York'],
        'start_position': 'New York',
        'total_distance': '7293 miles'}
        data = test_data()
        tsp = TSP(data)
        result = tsp.get_result()
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
