##GPS map of samples and known hot springs
import csv
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import re

plt.figure(dpi=2000)

# Define the map boundaries and projection
m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='l')

# Draw coastlines, countries, and states
line_color = '#d3d3d3'
m.drawcoastlines(color="grey", linewidth=0.22)
m.drawcountries(color=line_color, linewidth=0.25)
m.drawstates(color=line_color, linewidth=0.25)
m.drawmapboundary(color="#D4F1F8", fill_color="#D4F1F8", zorder=0)
m.fillcontinents(color='w',lake_color="#D4F1F8", zorder=1)

#convert Lon+Lat from format in metadata table to recognisible one
def convert_coordinates(coordinates):
    # Extract numerical values and direction indicators
    matches = re.findall(r"(\d+\.\d+)\s*([NSEW])", coordinates)
    # Initialize variables
    latitude = None
    longitude = None
    # Process the matches
    for value, direction in matches:
        if direction in ['N', 'S']:
            if latitude is None:
                latitude = float(value)
            else:
                raise ValueError("Latitude already set")
        elif direction in ['E', 'W']:
            if longitude is None:
                longitude = float(value)
            else:
                raise ValueError("Longitude already set")
        else:
            raise ValueError(f"Invalid direction: {direction}")
    # Check if both latitude and longitude were found
    if latitude is None or longitude is None:
        raise ValueError("Latitude or longitude missing")
    # Determine negative values for South and West directions
    if 'S' in coordinates:
        latitude *= -1
    if 'W' in coordinates:
        longitude *= -1
    return latitude, longitude

# Split the coordinates column into latitude and longitude columns
GPS_df = pd.DataFrame()
df_LatLon_Str = df['Lat_Lon'].astype(str)
GPS_df[['Lat2', 'Lon2']] = df_LatLon_Str.apply(lambda x: pd.Series(convert_coordinates(x)))

# Read and convert GPS coordinates from df
for _, row in GPS_df.iloc[1:].iterrows():
    lat2, lon2 = float(row[0]), float(row[1])
    # Convert GPS coordinates to x-y coordinates on the map
    x, y = m(lon2, lat2)
    # Plot the GPS coordinates as red circles on the map
    m.plot(x, y, color='#009999', marker='o', markeredgecolor='black', markeredgewidth=0.6, markersize=3, alpha=1, zorder=2)

# Read GPS coordinates from a CSV file HYDROTHERMAL SPRINGS 
with open('/Users/user/Library/CloudStorage/OneDrive-TheUniversityofManchester/Bioinformatics/Hydrothermal_Spring_Work/Batch_for_publication/Aggregated_analysis/output_data/hydrothermal_springs_GPS.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header row
    for row in reader:
            try:
                lat, lon = float(row[1]), float(row[2])
                # Convert GPS coordinates to x-y coordinates on the map
                x, y = m(lon, lat)
                # Plot the GPS coordinates as red circles on the map
                m.plot(x, y, color='#dd4444', marker='o', markersize=0.5, alpha=0.50, zorder=1)
            except ValueError:
                    # Skip over cells that raise a ValueError
                    continue

#Legend
green_dot = plt.scatter([], [], color='#009999', marker='o', s=9, alpha=1)
red_dot = plt.scatter([], [], color='#dd4444', marker='o', s=9, alpha=1)
plt.legend([green_dot, red_dot], ['Aquired datasets', 'Known hydrothermal springs'], loc='upper right', fontsize=5)

# Show the map
plt.savefig('GPS_Coordinates.png', bbox_inches='tight', dpi=2000)
plt.show()
