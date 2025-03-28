import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def plot_runtime_vs_tolerance():
    """Plots runtime vs. tolerance for 1 CPU and 8 CPUs."""
    tolerances = [0.01, 0.001, 0.0001, 0.00001]
    runtime_8cpu = [4, 23, 99, 344]
    runtime_1cpu = [18, 106, 452, 1548]
    
    plt.figure(figsize=(6, 3))
    plt.plot(tolerances, runtime_8cpu, marker='o', label='8 CPUs')
    plt.plot(tolerances, runtime_1cpu, marker='s', label='1 CPU')
    plt.xscale('log')
    plt.yscale('log')
    plt.gca().invert_xaxis()  # Flip the x-axis
    plt.xlabel("Tolerance")
    plt.ylabel("Runtime (s)")
    #plt.title("Runtime vs. Tolerance")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_flops_vs_tolerance():
    """Plots FLOPs vs. tolerance for 1 CPU and 8 CPUs."""
    tolerances = [0.01, 0.001, 0.0001, 0.00001]
    flops_8cpu = [5731772000, 6402794000, 6822602000, 6814994000]
    flops_1cpu = [1273727000, 1389286000, 1494331000, 1514443000]
    
    plt.figure(figsize=(6, 3))
    plt.plot(tolerances, flops_8cpu, marker='o', label='8 CPUs')
    plt.plot(tolerances, flops_1cpu, marker='s', label='1 CPU')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Tolerance")
    plt.ylabel("FLOPs")
    #plt.title("FLOPs vs. Tolerance")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_runtime_vs_cpus():
    """Plots runtime vs. number of CPUs."""
    cpu_counts = [1,2,3,4,5,6,7,8, 10, 12, 14]
    runtime = [179, 106, 86, 74, 71, 68, 61, 59, 48, 42, 39]
    
    plt.figure(figsize=(6, 3))
    plt.plot(cpu_counts, runtime, marker='o')
    plt.xlabel("Number of CPUs")
    plt.ylabel("Runtime (s)")
    #plt.title("Runtime vs. Number of CPUs")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_cache_protocol_comparison():
    """Plots runtime comparison for different cache protocols."""
    protocols = ['1 CPU', '8 CPUs']
    validinvalid_runtime = [1150561, 1683168]
    moesi_runtime = [374929, 201635]
    
    plt.figure(figsize=(6, 3))
    plt.bar(protocols, validinvalid_runtime, label='Valid/Invalid', alpha=0.6)
    plt.bar(protocols, moesi_runtime, label='MOESI', alpha=0.6)
    plt.ylabel("Runtime (s)")
    #plt.title("Cache Protocol Performance Comparison")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_cache_protocol_comparison_hitrate():
    protocols = ['1 CPU', '8 CPUs']
    validinvalid_hitrate = [0.96755, 0.892366667]
    moesi_hitrate = [0.96755, 0.966771086]
    
    plt.figure(figsize=(6, 3))
    plt.bar(protocols, moesi_hitrate, label='MOESI', alpha=0.6)
    plt.bar(protocols, validinvalid_hitrate, label='Valid/Invalid', alpha=0.6)
    plt.ylabel("Hitrate (%)")
    plt.legend(loc='lower left')
    plt.tight_layout()
    plt.show()

def plot_cache_protocol_comparison_colrow():
    cache_protocol_colmajor_rowmajor_test = ['Column Major', 'Row Major']
    validinvalid_major_runtime = [8242714, 6577224]
    moesi_major_runtime = [779429, 926822]
    
    plt.figure(figsize=(6, 3))
    plt.bar(cache_protocol_colmajor_rowmajor_test, validinvalid_major_runtime, label='Valid/Invalid', alpha=0.6)
    plt.bar(cache_protocol_colmajor_rowmajor_test, moesi_major_runtime, label='MOESI', alpha=0.6)
    
    plt.ylabel("Runtime (ns)")
    #plt.title("Cache Protocol Performance Comparison")
    plt.legend(loc='lower left')
    plt.tight_layout()
    plt.show()

    validinvalid_major_hitrate = [0.862534694, 0.927186028]
    moesi_major_hitrate = [0.968657143, 0.963940345]

    plt.figure(figsize=(6, 3))
    plt.bar(cache_protocol_colmajor_rowmajor_test, moesi_major_hitrate, label='MOESI', alpha=0.6)
    plt.bar(cache_protocol_colmajor_rowmajor_test, validinvalid_major_hitrate, label='Valid/Invalid', alpha=0.6)
    plt.ylabel("Hitrate (%)")
    #plt.title("Cache Protocol Performance Comparison")
    plt.legend(loc='lower left')
    plt.tight_layout()
    plt.show()

def plot_temp_grid_runtime():
    """Plots runtime for different temperature grid types, grouped by cache protocol."""
    grid_types = ['50x50', '50x100', '100x50', '100x100', '250x250']
    validinvalid_runtime = [1683168, 3545810, 3978898, 8242714, 47355068]
    moesi_runtime = [201635, 400268, 387985, 779429, 6192232]
    x = range(len(grid_types))
    
    plt.figure(figsize=(6, 3))
    width = 0.4
    plt.bar([i - width/2 for i in x], validinvalid_runtime, width=width, label='Valid/Invalid')
    plt.bar([i + width/2 for i in x], moesi_runtime, width=width, label='MOESI')
    
    plt.xticks(ticks=x, labels=grid_types)
    plt.xlabel("Temperature Grid Type")
    plt.ylabel("Runtime (s)")
    #plt.title("Runtime by Temperature Grid Type and Cache Protocol")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_50x100_vs_100x50():
    """Plots runtime comparison between 50x100 and 100x50 grid sizes."""
    grid_sizes = ['50x100', '100x50']
    validinvalid_runtime = [3545810, 3978898]
    moesi_runtime = [400268, 387985]
    x = range(len(grid_sizes))
    
    plt.figure(figsize=(6, 3))
    width = 0.4
    plt.bar([i - width/2 for i in x], validinvalid_runtime, width=width, label='Valid/Invalid')
    plt.bar([i + width/2 for i in x], moesi_runtime, width=width, label='MOESI')
    
    plt.xticks(ticks=x, labels=grid_sizes)
    plt.xlabel("Grid Size")
    plt.ylabel("Runtime (s)")
    #plt.title("Runtime Comparison: 50x100 vs. 100x50")
    plt.legend()
    plt.show()

def plot_map_type_runtime():
    """Plots runtime for different map types (areas, gradient, plasma), grouped by CPU count."""
    map_types = ['areas', 'gradient', 'plasma']
    runtime_1cpu = [7, 3, 9]
    runtime_8cpu = [3, 1, 3]
    x = range(len(map_types))
    
    plt.figure(figsize=(6, 3))
    width = 0.4
    plt.bar([i - width/2 for i in x], runtime_1cpu, width=width, label='1 CPU')
    plt.bar([i + width/2 for i in x], runtime_8cpu, width=width, label='8 CPUs')
    
    plt.xticks(ticks=x, labels=map_types)
    plt.xlabel("Map Type")
    plt.ylabel("Runtime (s)")
    #plt.title("Runtime by Map Type and CPU Count")
    plt.legend(loc='lower left')
    plt.tight_layout()
    plt.show()

def plot_temp_grid_hitrate():
    grid_types = ['50x50', '50x100', '100x50', '100x100', '250x250']
    validinvalid_hitrate = [0.892366667, 0.887306122, 0.8625, 0.862534694, 0.882827742]
    moesi_hitrate = [0.966771086, 0.950507365, 0.968358333, 0.968657143, 0.968916774]
    x = range(len(grid_types))
    
    plt.figure(figsize=(6, 3))
    width = 0.4
    plt.bar([i - width/2 for i in x], validinvalid_hitrate, width=width, label='Valid/Invalid')
    plt.bar([i + width/2 for i in x], moesi_hitrate, width=width, label='MOESI')
    
    plt.xticks(ticks=x, labels=grid_types)
    plt.xlabel("Temperature Grid Type")
    plt.ylabel("Hitrate (%)")
    #plt.title("Runtime by Temperature Grid Type and Cache Protocol")
    plt.legend(loc='lower left')
    plt.tight_layout()
    plt.show()

#plot_runtime_vs_tolerance()
#plot_flops_vs_tolerance()
#plot_runtime_vs_cpus()
#plot_cache_protocol_comparison()
#plot_cache_protocol_comparison_hitrate()
#plot_cache_protocol_comparison_colrow()
#plot_temp_grid_runtime()
plot_map_type_runtime()
#plot_50x100_vs_100x50()
#plot_temp_grid_hitrate()