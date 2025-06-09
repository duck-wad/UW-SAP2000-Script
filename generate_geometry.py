import numpy as np

# generate the nodes 

# example function
def generate_stringer(length, num_segments):
    # based on the length of the stringer and probably some other factors, segment the stringer into N segments
    # the return might be an array of 3D point Tuples, like [(x1, y1, z1), (x2, y2, z2), etc]

    # simple example
    segment_length = length / num_segments
    # assume x 
    x_pos = 0.0
    y_pos = 0.0
    z_pos = 5.0
    points = []
    for i in range(num_segments+1):
        points.append((x_pos, y_pos, z_pos))
        x_pos += segment_length
    return points