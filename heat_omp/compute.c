#include <time.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <stdio.h>
#include <float.h>
#include <time.h>
#include <omp.h>

#include "compute.h"
#include "fail.h"
#include "input.h"
#include "annotation.h"

#define ADJACENT_WEIGHT (sqrt(2) / (sqrt(2) + 1) / 4.0)
#define DIAGONAL_WEIGHT (1 / (sqrt(2) + 1) / 4.0)

void draw_heatmap(const struct parameters *p, double **grid, size_t iteration);
void print_grid(const struct parameters *p, double **grid);
void update_results(const struct parameters *p, double **temp_grid, 
    size_t iteration, size_t N, size_t M, struct results *r, 
    double max_diff, time_t start_time);
void initialize_grids(const struct parameters *p, double ***temp_grid,
    double ***temp_grid__new, double ***conductivity_grid);
void print_simulation_parameters(const struct parameters *p);


/**
 * @brief Print a heatmap of the temperature grid for logging purposes
 * 
 * @param p Simulation parameters.
 * @param grid Temperature grid.
 * 
 */
void print_grid(const struct parameters *p, double **grid) 
{
    for (size_t i = 0; i < p->N; i++) {
        for (size_t j = 0; j < p->M; j++) {
            printf("%f ", grid[i][j]);
        }
        printf("\n");
    }
}

/**
 * @brief Draw a heatmap of the temperature grid.
 * 
 * @param p Simulation parameters.
 * @param temp_grid Temperature grid.
 * @param iteration Current iteration.
 * @param N Number of rows.
 * @param M Number of columns.
 * @param r Simulation results.
 * @param max_diff Maximum difference between iterations.
 * @param start_time Start time of the simulation.
 * 
 * @note The function will update the results structure with the current state of the simulation.
 * 
 */
void update_results(const struct parameters *p, double **temp_grid, 
    size_t iteration, size_t N, size_t M, struct results *r, 
    double max_diff, time_t start_time)
{
    draw_heatmap(p, temp_grid, iteration);

    double temp_min = temp_grid[0][0];
    double temp_max = temp_grid[0][0];
    double temp_avg = 0.0;
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < M; j++)
        {
            if (temp_grid[i][j] < temp_min)
                temp_min = temp_grid[i][j];
            if (temp_grid[i][j] > temp_max)
                temp_max = temp_grid[i][j];
            temp_avg += temp_grid[i][j];
        }
    }
    temp_avg /= (N * M);

    time_t current_time = time(NULL);
    double elapsed_time = difftime(current_time, start_time);

    r->niter = iteration;
    r->tmin = temp_min;
    r->tmax = temp_max;
    r->tavg = temp_avg;
    r->maxdiff = max_diff;
    r->time = elapsed_time;

    if (p->printreports)
    {
        report_results(p, r);
    }
}

/**
 * @brief Initialize the temperature and conductivity grids.
 * 
 * @param p Simulation parameters.
 * @param temp_grid Temperature grid.
 * @param temp_grid__new New temperature grid.
 * @param conductivity_grid Conductivity grid.
 * 
 * @note The function will allocate memory for the grids and initialize them with the initial values.
 */
void initialize_grids(const struct parameters *p, double ***temp_grid, 
    double ***temp_grid__new, double ***conductivity_grid) 
{
    size_t N = p->N;
    size_t M = p->M;

    *temp_grid = (double**) malloc(N * sizeof(double*));
    *temp_grid__new = (double**) malloc(N * sizeof(double*));
    *conductivity_grid = (double**) malloc(N * sizeof(double*));

    if (!*temp_grid || !*temp_grid__new || !*conductivity_grid) 
    {
        fprintf(stderr, "Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }

    /* Allocate memory for each row */
    for (size_t i = 0; i < N; i++) 
    {
        (*temp_grid)[i] = (double*) malloc(M * sizeof(double)); 
        (*temp_grid__new)[i] = (double*) malloc(M * sizeof(double));
        (*conductivity_grid)[i] = (double*) malloc(M * sizeof(double));

        if (!(*temp_grid)[i] || !(*temp_grid__new)[i] || !(*conductivity_grid)[i]) 
        {
            fprintf(stderr, "Memory allocation failed.\n");
            exit(EXIT_FAILURE);
        }
    }

    /* Initialize temperature and conductivity */
    for (size_t i = 0; i < N; i++) 
    {
        for (size_t j = 0; j < M; j++) 
        {
            (*temp_grid)[i][j] = p->tinit[i * M + j];   // Convert from 1D input
            (*temp_grid__new)[i][j] = p->tinit[i * M + j];
            (*conductivity_grid)[i][j] = p->conductivity[i * M + j];
        }
    }
}

/**
 * @brief Print the simulation parameters.
 * 
 * @param p Simulation parameters.
 * 
 * @note The function is used for logging purposes.
 */
void print_simulation_parameters(const struct parameters *p)
{
    printf("Simulation parameters:\n"
           "  -n %zu\n"
           "  -m %zu\n"
           "  -i %zu\n"
           "  -k %zu\n"
           "  -e %e\n"
           "  -L %e\n"
           "  -H %e\n"
           "  -p %zu\n"
           "  -r %zu\n",
           p->N, p->M, p->maxiter, p->period, p->threshold,
           p->io_tmin, p->io_tmax,
           p->nthreads, p->printreports);
}


/**
 * @brief Update the temperature grid for one iteration in parallel.
 * 
 * @param p Simulation parameters.
 * @param temp_grid Current temperature grid.
 * @param temp_grid__new New temperature grid.
 * @param conductivity_grid Conductivity grid.
 * @param N Number of rows.
 * @param M Number of columns.
 * @param max_diff Pointer to the maximum difference between iterations.
 */
void update_temperature_grid(const struct parameters *p, double **temp_grid, 
    double **temp_grid__new, double **conductivity_grid, size_t N, size_t M, double *max_diff)
{
    double local_max_diff = 0.0;

    #pragma omp parallel for reduction(max:local_max_diff) schedule(static) num_threads(p->nthreads)
    for (size_t i = 1; i < N-1; i++) // Top and bottom rows are ghost cells
    { 
        for (size_t j = 0; j < M; j++) 
        {
            start_roi();

            size_t up = i - 1;
            size_t down = i + 1;
            size_t left = (j + M - 1) % M;
            size_t right = (j + 1) % M;

            double c = conductivity_grid[i][j];

            double adjacent_sum =
                (temp_grid[i][left] + temp_grid[i][right] + temp_grid[up][j] + temp_grid[down][j]) * ADJACENT_WEIGHT;

            double diagonal_sum =
                (temp_grid[up][left] + temp_grid[up][right] + temp_grid[down][left] + temp_grid[down][right]) * DIAGONAL_WEIGHT;

            double weighted_sum = adjacent_sum + diagonal_sum;

            temp_grid__new[i][j] = c * temp_grid[i][j] + (1 - c) * weighted_sum;

            double diff = fabs(temp_grid__new[i][j] - temp_grid[i][j]);
            if (diff > local_max_diff) 
            {
                local_max_diff = diff;
            }

            end_roi();
        }
    }
    
    *max_diff = local_max_diff;
}


/**
 * @brief Compute the heat dissipation in the system.
 * 
 * @param p Simulation parameters.
 * @param r Simulation results.
 * 
 * @note The function will update the results structure with the final state of the simulation.
 */
void do_compute(const struct parameters* p, struct results *r) 
{
    printf("Computing heat dissipation...\n");
    print_simulation_parameters(p);

    size_t N = p->N; // Number of rows
    size_t M = p->M; // Number of columns
    size_t maxiter = p->maxiter; // Maximum number of iterations
    double threshold = p->threshold; // Convergence threshold

    time_t time_start = time(NULL);

    double **temp_grid;
    double **temp_grid__new;
    double **conductivity_grid;

    initialize_grids(p, &temp_grid, &temp_grid__new, &conductivity_grid);

    size_t iteration = 0;
    double max_diff = threshold + 1.0; /* Ensure at least one iteration */

    update_results(p, temp_grid, iteration, N, M, r, max_diff, time_start); // Initial state

    while (iteration < maxiter && max_diff > threshold) 
    {
        max_diff = 0.0;
        iteration++;

        update_temperature_grid(p, temp_grid, temp_grid__new, conductivity_grid, N, M, &max_diff);

        double **temp = temp_grid;
        temp_grid = temp_grid__new;
        temp_grid__new = temp;

        if (iteration % p->period == 0) 
        {
            update_results(p, temp_grid, iteration, N, M, r, max_diff, time_start);
        } 
    }

    update_results(p, temp_grid, iteration, N, M, r, max_diff, time_start); // Final state

    printf("Parallel Heat dissipation completed.\n");

    /* Free allocated memory */
    for (size_t i = 0; i < N; i++) 
    {
        free(temp_grid[i]);
        free(temp_grid__new[i]);
        free(conductivity_grid[i]);
    }
    free(temp_grid);
    free(temp_grid__new);
    free(conductivity_grid);
}