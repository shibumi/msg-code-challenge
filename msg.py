#!/usr/bin/env python

from geopy.distance import distance
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def get_msg_data():
    """
    get_msg_data parses our CSV file, calculates the GPS distances via the Vincentys Formulae in the geopy library
    and returns a data object with an initialized distance_matrix, it also sets the depot (our start/end position),
    the number of routes and it calculates the TSP size.
    """
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
    """
    TSP calculates the Traveling Salesman Problem for our Challenge.
    I see no benefit in re-implementing existing problems. So we just use Google's
    excellent OR tools library for calculating the Traveling Salesman Problem.
    The benefits are: I learn to use a new library + I don't need to waste time on a semi-perfect solution.
    I doubt my personal solution would have outscaled Google's implementation in performance.
    """
    def create_distance_callback(self, dist_matrix):
        """
        create_distance_callback creates a callback function.
        The callback function works as functon pointer to a cost function.
        In this case, we are setting the cost function == the distance of two nodes
        """
        def distance_callback(from_node, to_node):
            return int(dist_matrix[from_node][to_node])
        # return our cost function
        return distance_callback


    def get_result(self):
        """
        get_result returns out calculated result. If calculation failed, it will return {}
        """
        return self.result
    

    def __init__(self, data):
        """
        init just directly triggers the calculation of the TSP problem and sets the result variable
        """
        self.result = {}
        routing = pywrapcp.RoutingModel(data['tsp_size'], data['num_routes'],
                                        data['depot'])
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        # Create the distance callback aka our cost function over our distance_matrix
        dist_callback = self.create_distance_callback(data['distance_matrix'])
        # Set our distance callback for all of our traveling salesman
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        # Solve the problem.
        assignment = routing.SolveWithParameters(search_parameters)
        if assignment:
            # setting distance in miles and start city
            self.result['total_distance'] = str(assignment.ObjectiveValue()) + " miles"
            self.result['start_position'] = data['cities'][data['depot']]
            # Index of the variable for the starting node, we always choose 0, because we have
            # just one traveling salesman ;)
            index = routing.Start(0)
            # Python lists are ordered, therefore we can savely store the values in a list
            self.result['route'] = []
            while not routing.IsEnd(index):
                # Convert variable indices to node indices in the displayed route.
                self.result['route'].append(data['cities'][routing.IndexToNode(index)])
                index = assignment.Value(routing.NextVar(index))
            self.result['route'].append(data['cities'][routing.IndexToNode(index)])
        else:
            self.result = {}


if __name__ == "__main__":
    data = get_msg_data()
    tsp = TSP(data)
    print(tsp.get_result())
