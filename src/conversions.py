to_kg = {
    "kg" : 1,
    "lb" : 2.20462,
    "t" : 907.185
}

to_meters = {
    "m" : 1,
    "ft" : 0.3048,
    "mi" : 1609.34,
    "km" : 1000,
    "au" : 149597870691,
    "ly" : 9460730472580044,
}

to_mps = {
    "m/s" : 1,
    "mi/hr" : 0.44704,
    "km/hr" : 0.277778,
    "ft/s" : 0.3048,
    "k" : 0.514444,
}

to_deg = {
    "dg" : 1,
    "rd" : 57.2958,
}

to_sec = {
    "s" : 1,
    "m" : 60,
    "h" : 3600,
    "d" : 86400,
    "mo" : 2628000,
    "y" : 31556952,
}

def convert_to_standards(values):
    new_values = {}
    new_values["kg"] = int(values["mass"]) * to_kg[values["mass-units"]]
    new_values["x"] = int(values["x"]) * to_meters[values["x-units"]]
    new_values["y"] = int(values["y"]) * to_meters[values["y-units"]]
    new_values["m/s"] = int(values["vel"]) * to_mps[values["vel-units"]]
    new_values["deg"] = int(values["ang"]) * to_deg[values["ang-units"]]
    new_values["sec"] = int(values["time"]) * to_sec[values["time-units"]]
    return new_values