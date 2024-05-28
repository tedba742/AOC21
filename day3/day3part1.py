def read_input(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def calculate_gamma_epsilon(binary_numbers):
    num_bits = len(binary_numbers[0])
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(num_bits):
        bit_count = sum(int(number[i]) for number in binary_numbers)
        if bit_count > len(binary_numbers) / 2:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate, 2), int(epsilon_rate, 2)

def main():
    binary_numbers = read_input('input.txt')
    gamma_rate, epsilon_rate = calculate_gamma_epsilon(binary_numbers)
    power_consumption = gamma_rate * epsilon_rate
    print(f"The power consumption of the submarine is: {power_consumption}")

if __name__ == "__main__":
    main()
