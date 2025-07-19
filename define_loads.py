def define_load_cases(load_length):
    # vertical load cases are structured as dictionaries with "L1" and "L2" keys
    # which correspond with tuples for start and end location of load
    v2 = {
        "Name": "V2",
        "L1": (3 * 12., 3 * 12. + load_length),
        "L2": (8.5 * 12., 8.5 * 12. + load_length)
    }
    v3 = {
        "Name": "V3",
        "L1": (3.5 * 12., 3.5 * 12. + load_length),
        "L2": (8 * 12., 8 * 12. + load_length)
    }
    v4 = {
        "Name": "V4",
        "L1": (4 * 12., 4 * 12. + load_length),
        "L2": (9.5 * 12., 9.5 * 12. + load_length)
    }
    v5 = {
        "Name": "V5",
        "L1": (4.5 * 12., 4.5 * 12. + load_length),
        "L2": (9 * 12., 9 * 12. + load_length)
    }
    v6 = {
        "Name": "V6",
        "L1": (5 * 12., 5 * 12. + load_length),
        "L2": (10 * 12., 10 * 12. + load_length)
    }
    v7 = {
        "Name": "V7",
        "L1": (6 * 12., 6 * 12. + load_length),
        "L2": (10.5 * 12., 10.5 * 12. + load_length)
    }
    v8 = {
        "Name": "V8",
        "L1": (10 * 12., 10 * 12. + load_length),
        "L2": (5 * 12., 5 * 12. + load_length)
    }
    v9 = {
        "Name": "V9",
        "L1": (9 * 12., 9 * 12. + load_length),
        "L2": (4.5 * 12., 4.5 * 12. + load_length)
    }
    v10 = {
        "Name": "V10",
        "L1": (9.5 * 12., 9.5 * 12. + load_length),
        "L2": (4 * 12., 4 * 12. + load_length)
    }
    v11 = {
        "Name": "V11",
        "L1": (8 * 12., 8 * 12. + load_length),
        "L2": (3.5 * 12., 3.5 * 12. + load_length)
    }
    v12 = {
        "Name": "V12",
        "L1": (8.5 * 12., 8.5 * 12. + load_length),
        "L2": (2 * 12., 2 * 12. + load_length)
    }

    vertical_loads = [v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12]

    # lateral load cases are point loads
    s2 = {"Name": "S2", "S": 7 * 12.}
    s3 = {"Name": "S3", "S": 7 * 12.}
    s4 = {"Name": "S4", "S": 7 * 12.}
    s5 = {"Name": "S5", "S": 7 * 12.}
    s6 = {"Name": "S6", "S": 8.5 * 12.}
    s7 = {"Name": "S7", "S": 8.5 * 12.}
    s8 = {"Name": "S8", "S": 8.5 * 12.}
    s9 = {"Name": "S9", "S": 7 * 12.}
    s10 = {"Name": "S10", "S": 7 * 12.}
    s11 = {"Name": "S11", "S": 7 * 12.}
    s12 = {"Name": "S12", "S": 7 * 12.}

    lateral_loads = [s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]

    return vertical_loads, lateral_loads
