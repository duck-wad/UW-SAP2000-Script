# NL: i just wrote a few example functions to generate some frame components
# these can be modified to work with current design


def generate_stringer_nodes(
    length, num_segments, y_pos, z_pos_top, depth, web_divisions, web_offset
):
    segment_length = length / num_segments

    top_chord_points = []
    bottom_chord_points = []
    web_points = []
    vertical_web_points = []

    for i in range(num_segments):
        top_chord_points.append(
            (
                (i * segment_length, y_pos, z_pos_top),
                (i * segment_length + segment_length, y_pos, z_pos_top),
            )
        )
        bottom_chord_points.append(
            (
                (i * segment_length, y_pos, z_pos_top - depth),
                (i * segment_length + segment_length, y_pos, z_pos_top - depth),
            )
        )

        # web_divisions is number of segments the bottom chord will be split by the webs
        # for instance, if web_divisions == 3, then there will be 6 total webs, it will look like 3 triangles
        # web_div_length is the base of the triangle
        # if web_offset is defined ex) 1 inch, then the diagonals start and end 1 inch from the end of the segment
        web_div_length = (segment_length - 2 * web_offset) / web_divisions
        for j in range(web_divisions):
            web_points.append(
                (
                    (
                        web_offset + i * segment_length + j * web_div_length,
                        y_pos,
                        z_pos_top - depth,
                    ),
                    (
                        web_offset + i * segment_length + (j + 0.5) * web_div_length,
                        y_pos,
                        z_pos_top,
                    ),
                )
            )
            web_points.append(
                (
                    (
                        web_offset + i * segment_length + (j + 0.5) * web_div_length,
                        y_pos,
                        z_pos_top,
                    ),
                    (
                        web_offset + i * segment_length + (j + 1.0) * web_div_length,
                        y_pos,
                        z_pos_top - depth,
                    ),
                )
            )

        vertical_web_points.append(
            (
                (web_offset + i * segment_length, y_pos, z_pos_top),
                (web_offset + i * segment_length, y_pos, z_pos_top - depth),
            )
        )
        vertical_web_points.append(
            (
                (i * segment_length + segment_length - web_offset, y_pos, z_pos_top),
                (
                    i * segment_length + segment_length - web_offset,
                    y_pos,
                    z_pos_top - depth,
                ),
            )
        )

    return top_chord_points, bottom_chord_points, web_points, vertical_web_points


def generate_leg_nodes(
    east_or_west, x_pos, y_pos, z_pos_top, depth, web_divisions, outer_offset
):
    # determine the direction to offset the outer leg chord
    # for west, outer leg further west (in negative direction), if east it goes in positive direction
    if east_or_west == "west":
        out_dir = -1
    elif east_or_west == "east":
        out_dir = 1
    else:
        raise ValueError(
            f"Invalid value for east_or_west argument. Expected either 'east' or 'west'"
        )

    # return separate lists with the inner post and outer post coordinates
    inner_leg_points = []
    outer_leg_points = []
    web_points = []

    inner_leg_points.append(((x_pos, y_pos, z_pos_top), (x_pos, y_pos, 0.0)))
    outer_leg_points.append(
        (
            (x_pos + out_dir * depth, y_pos, z_pos_top - outer_offset),
            (x_pos + out_dir * depth, y_pos, 0.0),
        )
    )

    # make the webs same process stringer. for loop makes the "triangles" with the base on the outer leg
    web_div_length = (z_pos_top - outer_offset) / web_divisions
    for i in range(web_divisions):
        web_points.append(
            (
                (x_pos + out_dir * depth, y_pos, i * web_div_length),
                (x_pos, y_pos, (i + 0.5) * web_div_length),
            )
        )
        web_points.append(
            (
                (x_pos, y_pos, (i + 0.5) * web_div_length),
                (x_pos + out_dir * depth, y_pos, (i + 1.0) * web_div_length),
            )
        )

    # have one web connect from top of outer leg horizontally to the inner leg
    # as well as one connecting from top of outer leg to the top of the inner leg
    web_points.append(
        (
            (x_pos + out_dir * depth, y_pos, z_pos_top - outer_offset),
            (x_pos, y_pos, z_pos_top - outer_offset),
        )
    )
    web_points.append(
        (
            (x_pos + out_dir * depth, y_pos, z_pos_top - outer_offset),
            (x_pos, y_pos, z_pos_top),
        )
    )

    return inner_leg_points, outer_leg_points, web_points


def generate_moment_frame_nodes(
    width, x_pos, z_pos_top, depth, web_divisions, web_offset
):
    moment_chord_points = []
    web_points = []
    vertical_web_points = []

    moment_chord_points.append(((x_pos, 0.0, z_pos_top), (x_pos, width, z_pos_top)))
    moment_chord_points.append(
        ((x_pos, 0.0, z_pos_top - depth), (x_pos, width, z_pos_top - depth))
    )

    # make the webs same process as the stringer
    web_div_length = (width - 2 * web_offset) / web_divisions
    for i in range(web_divisions):
        web_points.append(
            (
                (x_pos, web_offset + i * web_div_length, z_pos_top - depth),
                (x_pos, web_offset + (i + 0.5) * web_div_length, z_pos_top),
            )
        )
        web_points.append(
            (
                (x_pos, web_offset + (i + 0.5) * web_div_length, z_pos_top),
                (x_pos, web_offset + (i + 1.0) * web_div_length, z_pos_top - depth),
            )
        )

    vertical_web_points.append(
        ((x_pos, web_offset, z_pos_top), (x_pos, web_offset, z_pos_top - depth))
    )
    vertical_web_points.append(
        (
            (x_pos, width - web_offset, z_pos_top),
            (x_pos, width - web_offset, z_pos_top - depth),
        )
    )

    return moment_chord_points, web_points, vertical_web_points
