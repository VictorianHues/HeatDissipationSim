#include <stdio.h>

#include "input.h"
#include "compute.h"
#include "output.h"


int main(int argc, char **argv) {
    printf("Starting heat dissipation simulation...\n");
    /* Structure to hold input parameters */
    struct parameters p;
    
    /* Structure to hold simulation results */
    struct results r = {0};

    /* Read command-line parameters and input files */
    read_parameters(&p, argc, argv);

    do_compute(&p, &r);

    report_results(&p, &r);

    printf("Simulation completed.\n");
    return 0;
}
