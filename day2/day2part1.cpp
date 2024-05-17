#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream inputFile("input.txt");
    std::string command{""};
    int value{0};
    int horizontalPosition{0};
    int depth{0};

    while (inputFile >> command >> value) {
        if (command == "forward") {
            horizontalPosition += value;
        } else if (command == "down") {
            depth += value;
        } else if (command == "up") {
            depth -= value;
        }
    }

    inputFile.close();

    int result = horizontalPosition * depth;
    std::cout << "Result (horizontal position * depth): " << result << std::endl;

    return 0;
}
