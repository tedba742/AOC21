def hex_to_bin(hex_str):
    """Convert a hexadecimal string to a binary string."""
    return ''.join(format(int(c, 16), '04b') for c in hex_str)

def parse_packet(binary, index):
    """Parse a packet from the binary string starting at the given index."""
    version = int(binary[index:index+3], 2)
    type_id = int(binary[index+3:index+6], 2)
    index += 6

    version_sum = version

    if type_id == 4:  # Literal value
        while binary[index] == '1':
            index += 5
        index += 5
    else:  # Op
        length_type_id = int(binary[index], 2)
        index += 1
        if length_type_id == 0:
            subpacket_length = int(binary[index:index+15], 2)
            index += 15
            end_index = index + subpacket_length
            while index < end_index:
                sub_version_sum, index = parse_packet(binary, index)
                version_sum += sub_version_sum
        else:
            num_subpackets = int(binary[index:index+11], 2)
            index += 11
            for _ in range(num_subpackets):
                sub_version_sum, index = parse_packet(binary, index)
                version_sum += sub_version_sum

    return version_sum, index

def main(file_path):
    with open(file_path, 'r') as file:
        hex_str = file.read().strip()
    
    binary = hex_to_bin(hex_str)
    version_sum, _ = parse_packet(binary, 0)
    print(f"Sum of version numbers: {version_sum}")

file_path = 'input.txt'
main(file_path)
