#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream inputFile("input.txt");
    if (!inputFile) {
        std::cerr << "Failed to open input file." << std::endl;
        return 1;
    }

    std::string command{""};
    int value{0};
    int horizontalPosition{0};
    int depth{0};
    int aim{0};

    while (inputFile >> command >> value) {
        if (command == "forward") {
            horizontalPosition += value;
            depth += aim * value;
        } else if (command == "down") {
            aim += value;
        } else if (command == "up") {
            aim -= value;
        }
    }

    inputFile.close();

    int result = horizontalPosition * depth;
    std::cout << "Result (horizontal position * depth): " << result << std::endl;

}
