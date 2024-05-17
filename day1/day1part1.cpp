#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::ifstream inputFile("input.txt");
    std::vector<int> depths;
    int depth;

    while (inputFile >> depth) {
        depths.push_back(depth);
    }

    inputFile.close();

    int increaseCount = 0;
    for (size_t i = 1; i < depths.size(); ++i) {
        if (depths[i] > depths[i - 1]) {
            ++increaseCount;
        }
    }

    std::cout << "Number of increases: " << increaseCount << std::endl;
}
