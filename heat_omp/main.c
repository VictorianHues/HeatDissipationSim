#include <stdio.h>
#include <omp.h>

#include "input.h"
#include "compute.h"
#include "output.h"


int main(int argc, char **argv) {
    struct parameters p;
    struct results r = {0};
    
    printf("Max threads: %d\n", omp_get_max_threads());

    read_parameters(&p, argc, argv);
    do_compute(&p, &r);
    return 0;
}
