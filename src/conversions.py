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

def convert_from_standards(original_values, values):
    new_values = {}
    new_values["mass"] = values["kg"] * (1/to_kg[original_values["mass-units"]])
    new_values["x"] = values["x"] * (1/to_meters[original_values["x-units"]])
    new_values["y"] = values["y"] * (1/to_meters[original_values["y-units"]])
    new_values["vel"] = values["m/s"] * (1/to_mps[original_values["vel-units"]])
    new_values["ang"] = values["deg"] * (1/to_deg[original_values["ang-units"]])
    new_values["time"] = values["sec"] * (1/to_sec[original_values["time-units"]])
    for key, value in original_values.items():
        if key.find("units") != -1:
            new_values[key] = value
    return new_values
