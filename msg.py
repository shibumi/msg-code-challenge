#!/usr/bin/env python

from geopy.distance import distance
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def test_data():
    """Stores the data for the problem."""
    data = {}
    data['cities'] = [
        'New York', 'Los Angeles', 'Chicago', 'Minneapolis', 'Denver',
        'Dallas', 'Seattle', 'Boston', 'San Fransisco', 'St. Louis', 'Houston',
        'Phoenix', 'Salt Lake City'
    ]
    data['tsp_size'] = len(data['cities'])
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


def get_msg_data():
    data = {}
    data['cities'] = []
    data['tsp_size'] = 0
    data['distance_matrix'] = [[]]
    data['num_routes'] = 1
    data['depot'] = 0
    positions = {}
    with open("msg_standorte_deutschland.csv") as csvFile:
        # skip first line
        next(csvFile)
        for line in csvFile:
            # remove newline from every line and split at delimeter ";"
            l = line.rsplit("\n")[0].split(",")
            # correct index. So 0 refers to the HQ in Munich and so on.
            data['cities'].append(l[1])
            positions[int(l[0]) - 1] = (l[6], l[7])
    # initialize TSP size
    data['tsp_size'] = len(data['cities'])
    for source, source_coord in positions.items():
        for dest, dest_coord in positions.items():
            # calculate distance between each position via geopy library
            # we could also calculate this by ourself via: https://en.wikipedia.org/wiki/Vincenty's_formulae
            # or via: https://en.wikipedia.org/wiki/Haversine_formula
            # the geopy library uses the Vincenty's formulae, because it's more precise.
            data['distance_matrix'][int(source)].append(
                distance(source_coord, dest_coord).m)
        # do not append last empty list
        # len(positions) - 1, because we corrected the index
        if int(source) < len(positions) - 1:
            data['distance_matrix'].append([])
    return data


class TSP:
    def create_distance_callback(self, dist_matrix):
        # Create a callback to calculate distances between cities.
        def distance_callback(from_node, to_node):
            return int(dist_matrix[from_node][to_node])

        return distance_callback


    def get_result(self):
        return self.result
    

    def __init__(self, data):
        self.result = {}
        routing = pywrapcp.RoutingModel(data['tsp_size'], data['num_routes'],
                                        data['depot'])
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        # Create the distance callback.
        dist_callback = self.create_distance_callback(data['distance_matrix'])
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        # Solve the problem.
        assignment = routing.SolveWithParameters(search_parameters)
        if assignment:
            self.result['total_distance'] = str(assignment.ObjectiveValue()) + " miles"
            self.result['start_position'] = data['cities'][data['depot']]
            # Index of the variable for the starting node.
            index = routing.Start(0)
            self.result['route'] = ''
            while not routing.IsEnd(index):
                # Convert variable indices to node indices in the displayed route.
                self.result['route'] += str(
                    data['cities'][routing.IndexToNode(index)]) + ' -> '
                index = assignment.Value(routing.NextVar(index))
            self.result['route'] += str(data['cities'][routing.IndexToNode(index)])
        else:
            self.result = {}


if __name__ == "__main__":
    data = get_msg_data()
    tsp = TSP(data)
    print(tsp.get_result())
