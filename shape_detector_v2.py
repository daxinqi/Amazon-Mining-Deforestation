import json
from shapely.geometry import Point, Polygon

# Load GeoJSON data from a file (replace 'path_to_file' with the actual file path)
with open("C:\\Users\\daxin\\Desktop\\amazon_all_48px_v3.1_0.50_1_2023-12_2023.geojson") as f:
    data = json.load(f)

with open("C:\\Users\\daxin\\Desktop\\amazon_all_48px_v3.1_2023_positives_0.999.geojson") as g: 
    data2 = json.load(g)
    
with open("C:\\Users\\daxin\\Desktop\\full_amazon_v9_negatives.geojson") as h: 
    data3 = json.load(h)

# Extract features
features = data['features']
featuress = data2['features']
featuresss = data3['features']

points = []
for feature in featuress:
    pointp = feature['geometry']
    if pointp['type'] == 'Point':
        coordinates = pointp['coordinates']
        # Create a Shapely Point object from the coordinates
        pointp_obj = Point(coordinates)
        points.append(pointp_obj)

points2 = []
for feature in featuresss:
    pointn = feature['geometry']
    if pointn['type'] == 'Point':
        coordinatess = pointn['coordinates']
        # Create a Shapely Point object from the coordinates
        pointn_obj = Point(coordinatess)
        points2.append(pointn_obj)

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


# Calculate true positives and false negatives
for pointp in points:
    point_in_polygon = False
    for polygon in polygons:
        if polygon.contains(pointp):
            true_positives += 1
            point_in_polygon = True
            break
    if not point_in_polygon:
        false_negatives += 1

# Calculate false positives and true negatives
for pointn in points2:
    point_in_polygon = False
    for polygon in polygons:
        if polygon.contains(pointn):
            false_positives += 1
            point_in_polygon = True
            break
    if not point_in_polygon:
        true_negatives += 1


correct = true_positives + true_negatives

total = true_negatives + true_positives + false_negatives + false_positives

acc = correct / total

# Output the results
print("True Positives:", true_positives)
print("True Negatives:", true_negatives)
print("False Positives:", false_positives)
print("False Negatives:", false_negatives)
print("accuracy:", acc)
