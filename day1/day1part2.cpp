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

    if (depths.size() < 3) {
        return 1;
    }

    int increaseCount = 0;

    int prevSum = depths[0] + depths[1] + depths[2];

    for (size_t i = 1; i < depths.size() - 2; ++i) {
        int currentSum = depths[i] + depths[i + 1] + depths[i + 2];
        if (currentSum > prevSum) {
            ++increaseCount;
        }
        prevSum = currentSum;
    }

    std::cout << "Number of increases in sliding window sums: " << increaseCount << std::endl;

    return 0;
}
