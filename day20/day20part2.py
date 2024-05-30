def parse_input(file_path):
    with open(file_path, 'r') as file:
        sections = file.read().strip().split('\n\n')
    
    enhancement_algo = sections[0].replace('\n', '')
    input_image = [list(line) for line in sections[1].split('\n')]
    
    return enhancement_algo, input_image

def get_pixel_value(image, x, y, out_of_bounds_pixel):
    if 0 <= x < len(image) and 0 <= y < len(image[0]):
        return image[x][y]
    else:
        return out_of_bounds_pixel

def get_output_pixel(image, x, y, enhancement_algo, out_of_bounds_pixel):
    binary_str = ''
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            binary_str += '1' if get_pixel_value(image, x + dx, y + dy, out_of_bounds_pixel) == '#' else '0'
    index = int(binary_str, 2)
    return enhancement_algo[index]

def enhance_image(image, enhancement_algo, out_of_bounds_pixel):
    new_image = []
    extended_size = 2
    for x in range(-extended_size, len(image) + extended_size):
        new_row = []
        for y in range(-extended_size, len(image[0]) + extended_size):
            new_pixel = get_output_pixel(image, x, y, enhancement_algo, out_of_bounds_pixel)
            new_row.append(new_pixel)
        new_image.append(new_row)
    return new_image

def count_lit_pixels(image):
    return sum(row.count('#') for row in image)

def main(file_path, steps):
    enhancement_algo, input_image = parse_input(file_path)
    out_of_bounds_pixel = '.'
    
    for step in range(steps):
        input_image = enhance_image(input_image, enhancement_algo, out_of_bounds_pixel)
        out_of_bounds_pixel = enhancement_algo[0] if out_of_bounds_pixel == '.' else enhancement_algo[-1]
    
    return count_lit_pixels(input_image)

file_path = 'input.txt'
steps = 50
num_lit_pixels = main(file_path, steps)
print("Number of lit pixels after {} enhancements: {}".format(steps, num_lit_pixels))
