from cmath import cos, sin
import math

class Object:
    data = {}

    def __init__(self, data):
        attributes = ["x","y","vel","acc", "jer", "avel", "aacc", "ang", "nforce"]
        self.data = data
        for attribute in attributes:
            if attribute not in self.data:
                self.data[attribute] = 0
        if "mass" not in data:
            self.data["mass"] = 1
        if "grav" not in data:
            self.data["grav"] = -9.81
    
    def tick(self):
        vert_vel = sin(self.data["ang"]) * self.data["vel"]
        self.data["y"] += vert_vel / 50
        hori_vel = cos(self.data["ang"]) * self.data["vel"]
        self.data["x"] += hori_vel / 50
        self.data["vel"] += self.data["acc"] / 50
        self.data["acc"] += (self.data["grav"] + self.data["nforce"]) / self.data["mass"]

    





