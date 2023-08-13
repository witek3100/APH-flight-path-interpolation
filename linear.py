

def get_interpolated_coordinates(cords1, cords2, num_points=10):
    coordinates = [cords1]

    for i in range(num_points):
        fraction = i / (num_points - 1)
        lat = cords1[0] + fraction * (cords2[0] - cords1[0])
        lon = cords1[1] + fraction * (cords2[1] - cords1[1])
        coordinates.append((lat, lon))

    return coordinates


