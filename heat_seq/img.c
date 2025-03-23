#include "output.h"
#include "fail.h"
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define PGM_DEPTH 256

static double *gdata;
static size_t gkey, gw, gh;
double gvmin, gvmax;

void begin_picture(size_t key, size_t width, size_t height, double vmin, double vmax)
{
    if (!(gdata = calloc(width * height, sizeof(double)))) die("calloc");
    gkey = key;
    gw = width;
    gh = height;
    gvmin = vmin;
    gvmax = vmax;
}

void draw_point(size_t x, size_t y, double value)
{
    gdata[y * gw + x] = value;
}

void end_picture(void)
{
    FILE *f;
    char fname[100];
    size_t i, j;

    /* create file name */
    snprintf(fname, sizeof(fname), "/home/HeatDissipationSim/images/seq_images/img.%.10zu.pgm", gkey);
    printf("Creating image file: %s... ", fname);

    /* open file */
    if (!(f = fopen(fname, "w"))) die("fopen");

    /* write header */
    fprintf(f, "P2\n%zu %zu\n%u\n", gw, gh, PGM_DEPTH-1);
    
    /* write image data */
    for (j = 0; j < gh; ++j)
    {
        for (i = 0; i < gw; ++i) {
            int v = (PGM_DEPTH-1) * (gdata[j * gw + i] - gvmin) / (gvmax - gvmin);
            if (v < 0) v = 0;
            else if (v >= PGM_DEPTH) v = PGM_DEPTH-1; 
            fprintf(f, "%u ", v);
        }
        fputc('\n', f);
    }

    /* close and finish */
    fclose(f);
    printf("done.\n");
    free(gdata);
}

void draw_heatmap(const struct parameters* p, double** t, size_t iteration) {
    // Define the dynamic range for visualization
    double vmin = p->io_tmin;
    double vmax = p->io_tmax;

    // Start the image with the iteration as the key
    begin_picture(iteration, p->M, p->N, vmin, vmax);

    // Draw each grid point
    for (size_t i = 0; i < p->N; i++) {
        for (size_t j = 0; j < p->M; j++) {
            draw_point(j, i, t[i][j]); // Draw at (x, y)
        }
    }

    // Finalize the picture
    end_picture();
}