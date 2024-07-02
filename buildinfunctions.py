nested_list = [
    1,
    [2, 3, [4, 5]],
    [6, [7, 8], 9],
    10,
    [[11, 12], 13, [14, [15, 16]]],
    [17, [18, [19, 20]]]
]

def find_positions(nested_list, value, path=None):
    if path is None:
        path = []
    
    positions = []
    
    for index, item in enumerate(nested_list):
        current_path = path + [index]
        if isinstance(item, list):
            positions.extend(find_positions(item, value, current_path))
        elif item == value:
            positions.append(current_path)
    
    return positions

values_to_find = [4, 13, 20]
positions = {value: find_positions(nested_list, value) for value in values_to_find}
positions
