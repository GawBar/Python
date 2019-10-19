def parse_ranges(ranges):
    # range: ['1-2,3-4,5-6']
    # split string of ranges to list of bounds
    for bounds in ranges.split(","):
        # bounds: ['1-2', '3-4', '5-6']
        # split bounds to single bound 
        bound = bounds.split("-")
        # bound: ['1', '2']
        bound_start = int(bound[0])
        # bound_start: 1
        try:
            bound_end = int(bounds[1])
            # bound_end: 2 except it is not numeric string
        except (IndexError, ValueError):
            bound_end = bound_start
            # bound_end: 1
        for val in range(bound_start, bound_end + 1):
            # generator
            yield val
