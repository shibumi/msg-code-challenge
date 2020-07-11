#!/usr/bin/env python

from geopy.distance import distance

class MSG:

    def __init__(self):
        self.distances = []
        positions = {}
        with open("msg_standorte_deutschland.csv") as csvFile:
            # skip first line
            next(csvFile)
            for line in csvFile:
                # remove newline from every line and split at delimeter ";"
                l = line.rsplit("\n")[0].split(",")
                positions[l[0]] = (l[6], l[7])
        for source, source_coord in positions.items():
             for dest, dest_coord in positions.items():
                # calculate distance between each position via geopy library
                # we could also calculate this by ourself via: https://en.wikipedia.org/wiki/Vincenty's_formulae
                # or via: https://en.wikipedia.org/wiki/Haversine_formula
                # the geopy library uses the Vincenty's formulae, because it's more precise.
                d = distance(source_coord, dest_coord).m
                 # do not add distances with distance 0.0, because these are source == destination cycles
                if d != 0.0:
                    self.distances.append([source, dest, distance(source_coord, dest_coord).m])
        # sort based on distance == third element in calculated distances list
        self.distances.sort(key=lambda x: x[2])
        # from now here on use dijkstar
        print(self.distances)





if __name__ == "__main__":
    MSG()     