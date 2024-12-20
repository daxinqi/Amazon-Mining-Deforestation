import json
from shapely.geometry import Point, Polygon

# Load GeoJSON data from a file (replace 'path_to_file' with the actual file path)
with open("C:\\Users\\xuejungu\\Desktop\\Daxin_research\\amazon_all_48px_v3.1_0.50_1_2023-12_2023.geojson") as f:
    data = json.load(f)

with open("C:\\Users\\xuejungu\\Desktop\\Daxin_research\\amazon_all_48px_v3.1_2023_positives_0.999.geojson") as g: 
    data2 = json.load(g)

# Extract features
features = data['features']
featuress = data2['features']

points = []
for feature in featuress:
    point = feature['geometry']
    if point['type'] == 'Point':
        coordinates = point['coordinates']
        # Create a Shapely Point object from the coordinates
        point_obj = Point(coordinates)
        points.append(point_obj)

labels = [True, False, True, True, False]

# Extract Polygon geometries
polygons = []
for feature in features:
    geometry = feature['geometry']
    if geometry['type'] == 'Polygon':
        coordinates = geometry['coordinates']
        # Create a Shapely Polygon object from the coordinates
        polygon = Polygon(coordinates[0])  # Assuming single-ring polygons
        polygons.append(polygon)


# Initialize counters
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

# Calculate true positives, true negatives, false positives, and false negatives
# (same as your existing code)
# Calculate true positives
# Calculate true positives and false positives
for polygon in polygons:
    for i, point in enumerate(points):
        if polygon.contains(point):
            if labels[i]:
                true_positives += 1
            else:
                false_positives += 1

# Calculate true negatives and false negatives
for polygon in polygons:
    for i, point in enumerate(points):
        if not polygon.contains(point):
            if labels[i]:
                false_negatives += 1
            else:
                true_negatives += 1
                
# Output the results
print("True Positives:", true_positives)
print("True Negatives:", true_negatives)
print("False Positives:", false_positives)
print("False Negatives:", false_negatives)