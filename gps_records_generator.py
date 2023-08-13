import math
import matplotlib.pyplot as plt


class GpsRecordsGenerator:

    def __init__(self, start_lat=50, start_lon=20, ac_speed=50, ac_heading=45, turn_rate=0):
        self.gps_records = [(start_lat, start_lon)]
        self.ac_speed = ac_speed
        self.ac_heading = ac_heading
        self.interval = 1
        self.turn_rate = turn_rate

    def get_records(self, num_records):
        for i in range(num_records):
            new_record = self.get_new_record(self.gps_records[-1][0], self.gps_records[-1][1], self.ac_heading, self.ac_speed, self.interval)
            self.gps_records.append(new_record)
            self.ac_heading += self.turn_rate

        return self.gps_records

    def get_new_record(self, lat, lon, heading_deg, speed_mps, interval):
        R = 6371000
        angular_distance = (speed_mps * interval) / R

        lat1 = math.radians(lat)
        lon1 = math.radians(lon)
        heading_rad = math.radians(heading_deg)

        lat2 = math.asin(
            math.sin(lat1) * math.cos(angular_distance) + math.cos(lat1) * math.sin(angular_distance) * math.cos(
                heading_rad))
        lon2 = lon1 + math.atan2(math.sin(heading_rad) * math.sin(angular_distance) * math.cos(lat1),
                                 math.cos(angular_distance) - math.sin(lat1) * math.sin(lat2))

        new_lat = math.degrees(lat2)
        new_lon = math.degrees(lon2)

        return (new_lat, new_lon)
