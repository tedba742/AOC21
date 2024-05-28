#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <array>

std::vector<int> read_input(const std::string& filename) {
    std::ifstream file(filename);
    std::string line;
    std::vector<int> fish_timers;

    if (file.is_open()) {
        std::getline(file, line);
        std::stringstream ss(line);
        std::string timer;
        while (std::getline(ss, timer, ',')) {
            fish_timers.push_back(std::stoi(timer));
        }
        file.close();
    }

    return fish_timers;
}

long long simulate_lanternfish(const std::vector<int>& fish_timers, int days) {
    std::array<long long, 9> fish_counts = {0};

    for (int timer : fish_timers) {
        fish_counts[timer]++;
    }

    for (int day = 0; day < days; ++day) {
        long long new_fish = fish_counts[0];
        for (int i = 1; i < 9; ++i) {
            fish_counts[i - 1] = fish_counts[i];
        }
        fish_counts[6] += new_fish;
        fish_counts[8] = new_fish;
    }

    long long total_fish = 0;
    for (long long count : fish_counts) {
        total_fish += count;
    }

    return total_fish;
}

int main() {
    std::vector<int> fish_timers = read_input("input.txt");
    int days = 80;
    long long total_fish = simulate_lanternfish(fish_timers, days);

    std::cout << "Total number of lanternfish after " << days << " days: " << total_fish << std::endl;

    return 0;
}