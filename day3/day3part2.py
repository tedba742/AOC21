def read_input(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_rating(binary_numbers, criteria):
    remaining_numbers = binary_numbers
    num_bits = len(binary_numbers[0])
    
    for i in range(num_bits):
        bit_count = sum(int(number[i]) for number in remaining_numbers)
        if criteria == 'oxygen':
            desired_bit = '1' if bit_count >= len(remaining_numbers) / 2 else '0'
        else:
            desired_bit = '0' if bit_count >= len(remaining_numbers) / 2 else '1'
        
        remaining_numbers = [number for number in remaining_numbers if number[i] == desired_bit]
        
        if len(remaining_numbers) == 1:
            break
    
    return int(remaining_numbers[0], 2)

def main():
    binary_numbers = read_input('input.txt')
    oxygen_generator_rating = find_rating(binary_numbers, 'oxygen')
    co2_scrubber_rating = find_rating(binary_numbers, 'co2')
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print(f"The life support rating of the submarine is: {life_support_rating}")

if __name__ == "__main__":
    main()
