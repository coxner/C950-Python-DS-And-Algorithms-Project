class Package:
    def __init__(self, ID, address, city, state, zip, deadline, mass, delivery_status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.delivery_status = delivery_status
        self.delivery_time = None
        self.on_truck = None
        self.loaded_on_truck = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip,
                                                       self.deadline, self.mass, self.delivery_status, self.delivery_time,
                                                       self.on_truck)
