from preprocess import *
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1.lat-p2.lat)**2 + (p1.lon-p2.lon)**2)

def haversine_distance(lat1, lon1, lat2, lon2, unit='km'):
    """
    Calculate the Haversine distance between two points on Earth.
    
    Args:
        lat1, lon1: Latitude and longitude of point 1 (in degrees).
        lat2, lon2: Latitude and longitude of point 2 (in degrees).
        unit: 'km' (default) or 'mi' for miles.
    
    Returns:
        Distance in the specified unit.
    """
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Earth radius in km (or miles)
    R = 6371.0 if unit == 'km' else 3959.0  # 3959 miles
    
    return R * c

file_name =  'coordinates.csv'
points = open_points(file_name)

print("Distance between A&B: ", haversine_distance( points[0].lat, points[0].lon, points[1].lat, points[1].lon  ) )
