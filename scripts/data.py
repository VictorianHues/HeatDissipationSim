import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


"""
Parallelization Tests
"""
# Decreasing tolerance thresholds 
random_temp_1000_1000_tolerances = [0.01, 0.001, 0.0001, 0.00001]
random_temp_1000_1000_maxiter = [1909, 12271, 56286, 195363]

random_temp_8cpu_1000_1000_runtime = [4, 23, 99, 344]
random_temp_1cpu_1000_1000_runtime = [18, 106, 452, 1548]
random_temp_8cpu_1000_1000_FLOPs = [5731772000, 6402794000, 6822602000, 6814994000]
random_temp_1cpu_1000_1000_FLOPs = [1273727000, 1389286000, 1494331000, 1514443000]


# Tolerance = 1E-12
map_types_100_100 = ['areas', 'gradient', 'plasma']
map_tests_100_100_maxiter = [122297, 47270, 129331]

map_tests_1cpu_100_100_runtime = [7, 3, 9]
map_tests_1cpu_100_100_FLOPs = [2096537000, 1890816000, 1724428000]

map_tests_8cpu_100_100_runtime = [3, 1, 3]
map_tests_8cpu_100_100_FLOPs = [4891921000, 5672447000, 5173283000]

# Column major vs row major
colmajor_250_250_8cpu_runtime = 75
rowmajor_250_250_8cpu_runtime = 67

colmajor_250_250_8cpu_FLOPs = 7211770000
rowmajor_250_250_8cpu_FLOPs = 8072877000

# Increasing CPU count
cputest_cpu_nums = [1,2,3,4,5,6,7,8]
cputest_250_250_runtime = [253, 127, 112, 105, 99, 89, 76, 64]
cputest_250_250_FLOPs = [2137877000, 4258919000, 4829310000, 5151264000, 5463462000, 6077334000, 7116878000, 8451293000]



"""
Cache Protocol Tests
"""
# 1 CPU vs 8 cpus
cache_protocol_cpunum_test = ['1 cpu', '8 cpus']
validinvalid_runtime = [1150561, 1683168]
moesi_runtime = [374929, 201635]
validinvalid_memreads = [1947, 6458]
moesi_memreads = [1947, 1973]
validinvalid_memwrites = [7899, 293]
moesi_memwrites = [10207, 0]
validinvalid_readhitrate = [0.974943182, 0.91469697]
moesi_readhitrate = [0.974943182, 0.974450758]
validinvalid_writehitrate = [0.913333333, 0.728611111]
moesi_writehitrate = [0.913333333, 0.905109489]
validinvalid_hitrate = [0.96755, 0.892366667]
moesi_hitrate = [0.96755, 0.966771086]

# Column Major vs Row Major
cache_protocol_colmajor_rowmajor_test = ['Column Major', 'Row Major']
validinvalid_major_runtime = [8242714, 6577224]
moesi_major_runtime = [779429, 926822]
validinvalid_major_memreads = [33679, 18553]
moesi_major_memreads = [7679, 8862]
validinvalid_major_memwrites = [47932, 46568]
moesi_major_memwrites = [29, 268]
validinvalid_major_readhitrate = [0.880974026, 0.932497782]
moesi_major_readhitrate = [0.975974026, 0.97228039]
validinvalid_major_writehitrate = [0.727312925, 0.886462585]
moesi_major_writehitrate = [0.915, 0.9]
validinvalid_major_hitrate = [0.862534694, 0.927186028]
moesi_major_hitrate = [0.968657143, 0.963940345]

# Test grid sizes
grid_sizes = ['50x50', '50x100', '100x50', '100x100', '250x250']

validinvalid_runtime = [1683168, 3545810, 3978898, 8242714, 47355068]
moesi_runtime = [201635, 400268, 387985, 779429, 6192232]
validinvalid_memreads = [6458, 13902, 16200, 33679, 181617]
moesi_memreads = [1973, 3957, 3797, 7679, 48179]
validinvalid_memwrites = [10207, 21205, 23195, 47932, 287245]
moesi_memwrites = [0, 0, 0, 29, 13128]

validinvalid_readhitrate = [0.91469697, 0.908599258, 0.882954545, 0.880974026, 0.896746334]
moesi_readhitrate = [0.974450758, 0.955473098, 0.97563447, 0.975974026, 0.976132698]
validinvalid_writehitrate = [0.728611111, 0.731156463, 0.7125, 0.727312925, 0.780758065]
moesi_writehitrate = [0.905109489, 0.913333333, 0.915, 0.915, 0.916]
validinvalid_hitrate = [0.892366667, 0.887306122, 0.8625, 0.862534694, 0.882827742]
moesi_hitrate = [0.966771086, 0.950507365, 0.968358333, 0.968657143, 0.968916774]

