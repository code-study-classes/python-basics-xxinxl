calculate_distance = lambda x, y: abs(x - y)

calculate_segments = lambda a, b: a // b

calculate_digit_sum = lambda number: sum(int(digit) for digit in str(abs(number)))

def calculate_rect_area(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return float(width * height)

def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)