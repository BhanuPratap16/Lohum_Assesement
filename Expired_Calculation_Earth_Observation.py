import numpy as np
from scipy.stats import norm

# Input data: Satellites launched per year (from the graph)
years = np.array([2080,2081, 2082, 2083,2084, 2085,2086,2087, 2088, 2089,2090, 2091,2092, 2093,2094, 2095,2096, 2097,2098, 2099,2100, 2101,2102, 2103,2104])
satellites_launched = np.array([50,55,55,60,50,40,40,33,33,33,33,33,30,30,30,30,27,30,35,40,50,60,55,50,60])

# Constants for communication satellite lifecycle (mean and std deviation)
mean_life = 7  # in years
std_dev = 3    # in years

# Define current year for analysis
current_year = 2104

# Average recoverable mass of metals per satellite (in kg) and market price (in $/kg)
avg_metal_mass = 500  # Example: 500 kg of recoverable metals per satellite
metal_price_per_kg = 10  # Example: $10 per kg of metals

# Calculate the proportion of satellites out of service for each launch year
def calc_out_of_service_fraction(launch_year, mean, std_dev, current_year):
    age = current_year - launch_year
    if age <= 0:  # Satellites launched in the future are not out of service
        return 0
    # Proportion of satellites with age greater than lifecycle age
    return 1 - norm.cdf(age, loc=mean, scale=std_dev)

# Calculate total out-of-service satellites and their value
total_out_of_service = 0
total_value = 0

for year, launched in zip(years, satellites_launched):
    out_of_service_fraction = calc_out_of_service_fraction(year, mean_life, std_dev, current_year)
    out_of_service_satellites = launched * out_of_service_fraction
    total_out_of_service += out_of_service_satellites
    # total_value += out_of_service_satellites * avg_metal_mass * metal_price_per_kg

# Print results
print(f"Total out-of-service satellites: {total_out_of_service:.2f}")
# print(f"Total value of recoverable metals: ${total_value:.2f}")
