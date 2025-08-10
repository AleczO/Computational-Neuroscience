#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#define N 10
#define T 180


double draw_random(const double range_from, const double range_to) {
    std::random_device rd;
    std::mt19937 generator(rd());
    std::uniform_real_distribution<double> distr(range_from, range_to);

    return distr(generator);
}


void shuffle_random(std::vector<int>& v) {
    std::random_device rd;
    std::mt19937       generator(rd());

    std::ranges::shuffle(v, generator);
}


void set_synaptic_weights(std::vector<double> &Adj) {
    std::vector<int> Indexes(N);
    for (int i = 0; i < N; i++) {
        Indexes[i] = i;
    }

    shuffle_random(Indexes);

    for (int i = 0; i < 3; ++i) {
        Adj[Indexes[i]] = draw_random(-0.2,0.0);
    }

    for (int i = 3; i < N; ++i) {
        Adj[Indexes[i]] = draw_random(0.0,0.5);
    }
}


void print_weights_params(std::vector<std::vector<double>>& Network) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            std::cout << Network[i][j] << ' ';
        }
        std::cout << '\n';
    }
}



int main() {

    std::vector<std::vector<double>> Network(N, std::vector<double>(N, -1.0));

    set_synaptic_weights(Network[0]);


    // Synapses weights
    for (int i = 0; i < N; ++i) {
        set_synaptic_weights(Network[i]);
    }

    // Direct feedback
    for (int i = 0; i < N; ++i) {
        Network[i][i] = draw_random(-0.05, 0.0);
    }

    print_weights_params(Network);

    // Simulation
    for (double t = 0 ; t < T; t += 0.05) {

    }

    return 0;
}