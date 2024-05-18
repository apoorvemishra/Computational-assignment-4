#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Function to generate uniform random numbers between 0 and 1
double uniform_random() {
    return rand() / (RAND_MAX + 1.0);
}

// Function to generate exponential random numbers with mean 0.5
double exponential_random() {
    double lambda = 2.0;
    double u = uniform_random();
    return -log(1 - u) / lambda;
}

int main() {
    int n = 10000;
    double data[n];

    // Seed the random number generator
    srand(time(NULL));

    // Generate exponential random numbers
    for(int i = 0; i < n; i++) {
        data[i] = exponential_random();
    }

    // Write the data to a file
    FILE *f = fopen("exponential_data.txt", "w");
    if (f == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        fprintf(f, "%f\n", data[i]);
    }

    fclose(f);
    return 0;
}
