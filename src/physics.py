class Force:
    mag = 0
    ang = 0
    start = 0
    end = 0

    def __init__(self, m, a, s, e):
        self.mag = m
        self.ang = a
        self.start = s
        self.end = e

    def __str__(self):
        return f"{self.mag}, {self.ang}, {self.start}, {self.end}"  
    