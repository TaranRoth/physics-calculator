from cmath import cos, sin
import math
from .physics import Force
from .conversions import round_digits

class Object:


    def populate_forces(self):
        for key, value in self.data.items():
            if key[-1].isdigit():
                self.forces.append(Force(float(value), float(self.data[f"{key}-ang"]), float(self.data[f"{key}-start"]), float(self.data[f"{key}-end"])))

    def __init__(self, d):
        self.current_time = 0
        self.data = {}
        self.forces = []
        for key, value in d.items():
            self.data[key] = value
        self.populate_forces()

    def get_rad(self, vert, hori):
        if vert < 0.00001 and vert > -0.00001:
            vert = 0
        if hori < 0.00001 and hori > -0.00001:
            hori = 0
        if vert == 0 and hori == 0:  
            return 0
        elif vert == 0 and hori > 0:
            return 0
        elif vert == 0 and hori < 0:
            return math.pi
        elif hori == 0 and vert > 0:
            return math.pi / 2
        elif hori == 0 and vert < 0:
            return math.pi * 1.5
        #print(f"Vert: {vert}, hori: {hori}")
        return math.atan(vert / hori)

    def get_nforce(self, time):
        vert_nforce = 0
        hori_nforce = 0
        for force in self.forces:
            if time >= force.start and time <= force.end:
                vert_nforce += sin(force.ang).real * force.mag
                hori_nforce += cos(force.ang).real * force.mag
        nforce_mag = math.sqrt(vert_nforce ** 2 + hori_nforce ** 2)
        nforce_ang = self.get_rad(vert_nforce, hori_nforce)
        return [nforce_mag, nforce_ang]

    def tick(self, time, current_time):
        nforce = self.get_nforce(current_time)
        init_vert_vel = sin(self.data["rd"]).real * self.data["m/s"]
        vert_vel = sin(nforce[1]).real * nforce[0] * time / self.data["kg"] + init_vert_vel
        self.data["y"] += (vert_vel + init_vert_vel) / 2 * time
        init_hori_vel = cos(self.data["rd"]).real * self.data["m/s"]
        hori_vel = cos(nforce[1]).real * nforce[0] * time / self.data["kg"] + init_hori_vel
        self.data["x"] += (hori_vel + init_hori_vel) / 2 * time
        self.data["m/s"] = math.sqrt(vert_vel ** 2 + hori_vel ** 2)
        self.data["rd"] = self.get_rad(vert_vel, hori_vel)

    def simulate(self):
        times_to_tick = 1000
        current_time = 0
        for i in range(times_to_tick):
            time_to_tick = float(self.data["sec"]) / times_to_tick
            self.tick(time_to_tick, current_time)
            current_time += time_to_tick
    





