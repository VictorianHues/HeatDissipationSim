#ifndef COMPUTE_H
#define COMPUTE_H

#include "input.h"
#include "output.h"

void do_compute(const struct parameters *p,
                struct results *r);

void update_results(const struct parameters *p, double **temp_grid, 
    size_t iteration, size_t N, size_t M, struct results *r, 
    double max_diff, time_t start_time);

#endif
