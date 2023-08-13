from gps_records_generator import GpsRecordsGenerator
from linear import get_interpolated_coordinates
import matplotlib.pyplot as plt

NUM_RECORDS = 100

gps_records = GpsRecordsGenerator(turn_rate=-20).get_records(NUM_RECORDS)

interpolated_records = []

for i in range(len(gps_records)-1):
    next_cords = get_interpolated_coordinates(gps_records[i], gps_records[i+1])
    interpolated_records.extend(next_cords)


lats = [lat for lat, _ in gps_records]
lons = [lon for _, lon in gps_records]

latsi = [lat for lat, _ in interpolated_records]
lonsi = [lon for _, lon in interpolated_records]

plt.figure(figsize=(10, 6))

plt.scatter(lonsi, latsi, marker='.', color='r')
plt.scatter(lons, lats, marker='.', color='b')

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Generated Coordinates')
plt.grid()
plt.show()