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

to_rd = {
    "rd" : 1,
    "dg" : 0.0174533,
}

to_sec = {
    "ms" : 0.001,
    "s" : 1,
    "m" : 60,
    "h" : 3600,
    "d" : 86400,
    "mo" : 2628000,
    "y" : 31556952,
}

round_digits = 6

def convert_to_standards(values):
    new_values = {}
    new_values["kg"] = float(values["mass"]) * to_kg[values["mass-units"]]
    new_values["x"] = float(values["x"]) * to_meters[values["x-units"]]
    new_values["y"] = float(values["y"]) * to_meters[values["y-units"]]
    new_values["m/s"] = float(values["vel"]) * to_mps[values["vel-units"]]
    new_values["rd"] = float(values["ang"]) * to_rd[values["ang-units"]]
    new_values["sec"] = float(values["time"]) * to_sec[values["time-units"]]
    for key, value in values.items():
        if "force" in key and "ang" in key and "units" not in key:
            new_values[key] = float(value) * to_rd[values[f"{key}-units"]]
        elif "units" in key or "force" in key:
            new_values[key] = value
    return new_values

def convert_from_standards(original_values, values):
    new_values = {}
    new_values["mass"] = values["kg"] * (1/to_kg[original_values["mass-units"]])
    new_values["x"] = values["x"] * (1/to_meters[original_values["x-units"]])
    new_values["y"] = values["y"] * (1/to_meters[original_values["y-units"]])
    new_values["vel"] = values["m/s"] * (1/to_mps[original_values["vel-units"]])
    new_values["ang"] = values["rd"] * (1/to_rd[original_values["ang-units"]])
    new_values["time"] = values["sec"] * (1/to_sec[original_values["time-units"]])
    for key, value in original_values.items():
        if "force" in key and "ang" in key and "units" not in key:
            new_values[key] = value * (1/to_rd[original_values[f"{key}-units"]])
        elif "units" in key or "force" in key:
            new_values[key] = value
    return new_values
