class Truck:
    def __init__(self, id, max_packages, avg_speed, packages, distance_travel, curr_address, time):
        self.id = id
        self.max_packages = max_packages
        self.avg_speed = avg_speed
        self.packages = packages
        self.distance_travel = distance_travel
        self.curr_address = curr_address
        self.time = time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.max_packages, self.avg_speed, self.packages, self.distance_travel,
                                           self.curr_address, self.time)