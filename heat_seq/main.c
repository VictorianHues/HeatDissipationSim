#include <stdio.h>

#include "input.h"
#include "compute.h"
#include "output.h"


int main(int argc, char **argv) {
    struct parameters p;
    struct results r = {0};

    read_parameters(&p, argc, argv);
    do_compute(&p, &r);

    return 0;
}
