def total_height(board):
    return sum(max(col) for col in zip(*board))

def max_height(board):
    return max(max(col) for col in zip(*board))

def height_difference(board):
    heights = [max(col) for col in zip(*board)]
    return max(heights) - min(heights)

def holes(board):
    total_holes = 0
    for col in zip(*board):
        block_found = False
        for block in col:
            if block == 1:
                block_found = True
            elif block_found:
                total_holes += 1
    return total_holes

def bumpiness(board):
    heights = [max(col) for col in zip(*board)]
    return sum(abs(heights[i] - heights[i - 1]) for i in range(1, len(heights)))

def calculate_heuristics(board):
    total_height_value = total_height(board)
    max_height_value = max_height(board)
    height_difference_value = height_difference(board)
    holes_value = holes(board)
    bumpiness_value = bumpiness(board)

    return {
        'total_height': total_height_value,
        'max_height': max_height_value,
        'height_difference': height_difference_value,
        'holes': holes_value,
        'bumpiness': bumpiness_value
    }