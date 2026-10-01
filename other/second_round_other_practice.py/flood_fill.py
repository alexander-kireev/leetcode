def flood_fill(image, sr, sc, new_colour):
    if is_og_colour(image[sr][sc], new_colour):
        return image
    
    og_colour = image[sr][sc]
    stack = [[sr, sc]]
    rows = len(image)
    cols = len(image[0])

    while stack:
        node = stack.pop()

        change_colour(image, node, new_colour)

        potential_nodes = get_nodes(node)

        for new_node in potential_nodes:
            if valid_node(rows, cols, new_node) and is_og_colour(og_colour, image[new_node[0]][new_node[1]]):
                stack.append(new_node)

    return image


def is_og_colour(og_colour, new_node_colour):
    return og_colour == new_node_colour

def get_nodes(node):
    directions = [[-1,0], [0,1], [1,0], [0,-1]]
    new_nodes = []
    x1 = node[0]
    y1 = node[1]

    for x2,y2 in directions:
        new_nodes.append([x1 + x2, y1 + y2])

    return new_nodes

def valid_node(rows, cols, node):
    row = node[0]
    col = node[1]

    if not 0 <= row <= rows - 1:
        return False
    if not 0 <= col <= cols - 1:
        return False
    return True

def change_colour(image, node, new_colour):
    row = node[0]
    col = node[1]
    image[row][col] = new_colour

def run_tests():
    tests = [
        (
            [[1,1,1],
             [1,1,0],
             [1,0,1]],
            1, 1, 2,
            [[2,2,2],
             [2,2,0],
             [2,0,1]]
        ),

        (
            [[0,0,0],
             [0,0,0]],
            0, 0, 2,
            [[2,2,2],
             [2,2,2]]
        ),

        (
            [[0,0,0],
             [0,1,1]],
            1, 1, 1,
            [[0,0,0],
             [0,1,1]]
        ),

        (
            [[1]],
            0, 0, 5,
            [[5]]
        ),

        (
            [[1,2,1],
             [2,1,2],
             [1,2,1]],
            1, 1, 9,
            [[1,2,1],
             [2,9,2],
             [1,2,1]]
        ),

        (
            [[1,1,0],
             [1,0,0],
             [1,1,1]],
            0, 0, 3,
            [[3,3,0],
             [3,0,0],
             [3,3,3]]
        ),
    ]

    for i, (image, sr, sc, new_colour, expected) in enumerate(tests, 1):
        result = flood_fill([row[:] for row in image], sr, sc, new_colour)

        print(f"Test {i}: {'PASS' if result == expected else 'FAIL'}")
        print(f"Input:    image={image}, sr={sr}, sc={sc}, new_colour={new_colour}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        print()


run_tests()