import json
from shapely.geometry import MultiPolygon, Point, Polygon

# Load GeoJSON data from a file (replace 'path_to_file' with the actual file path)
with open("C:\\Users\\daxin\\OneDrive\\Desktop\\Confusion Matrix\\Threshold_Data_Amazonas\\test_region_48px_v3.2-3.7ensemble_0.20_2023-01-01_2023-12-31.geojson") as f:
    data_output = json.load(f)

with open("C:\\Users\\daxin\\Desktop\\amazon_all_48px_v3.1_2023_positives_0.999.geojson") as g: 
    data_positive = json.load(g)
    
with open("C:\\Users\\daxin\\Desktop\\full_amazon_v9_negatives.geojson") as h: 
    data_negative = json.load(h)
    
with open("C:\\Users\\daxin\\Desktop\\mining-detector-main\\data\\boundaries\\test_region.geojson") as i: 
    cropped_region = json.load(i)    

# Extract features
features_output = data_output['features']
features_positive = data_positive['features']
features_negative = data_negative['features']
features_cropped = cropped_region['features']

points_p = []
for feature in features_positive:
    pointp = feature['geometry']
    if pointp['type'] == 'Point':
        coordinates_p = pointp['coordinates']
        # Create a Shapely Point object from the coordinates
        pointp_obj = Point(coordinates_p)
        points_p.append(pointp_obj)

points_n = []
for feature in features_negative:
    pointn = feature['geometry']
    if pointn['type'] == 'Point':
        coordinates_n = pointn['coordinates']
        # Create a Shapely Point object from the coordinates
        pointn_obj = Point(coordinates_n)
        points_n.append(pointn_obj)

# Extract Polygon geometries
polygons = []
for feature in features_output:
    geometry = feature['geometry']
    if geometry['type'] == 'Polygon':
        coordinates_out = geometry['coordinates']
        # Create a Shapely Polygon object from the coordinates
        polygon = Polygon(coordinates_out[0])  # Assuming single-ring polygons
        polygons.append(polygon)

# Extract Polygon geometries of cropped region
polygons_cropped = []
for feature in features_cropped:
    geometry_c = feature['geometry']
    if geometry_c['type'] == 'Polygon':
        coordinates_cropped = geometry_c['coordinates']
        # Create a Shapely Polygon object from the coordinates
        polygon_region = Polygon(coordinates_cropped[0])  # Assuming single-ring polygons
        polygons_cropped.append(polygon_region)
        
    
#polygons_cropped = []
#for feature in features_cropped:
#    geometry_c = feature['geometry']
#    if geometry_c['type'] == 'MultiPolygon':
#        coordinates_cropped = geometry_c['coordinates']
#        # Create a Shapely MultiPolygon object from the coordinates
#        polygons_m = [Polygon(polygon[0]) for polygon in coordinates_cropped]  # Assuming single-ring polygons
#       multi_polygon_region = MultiPolygon(polygons_m)
#        polygons_cropped.append(multi_polygon_region)
        
points_p_cropped = []

points_n_cropped = []

# Initialize counters
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

#crop labels
for pointp in points_p:
    for polygon in polygons_cropped:
        if polygon.contains(pointp):
            points_p_cropped.append(pointp)
            break
            
for pointn in points_n:
    for polygon in polygons_cropped:
        if polygon.contains(pointn):
            points_n_cropped.append(pointn)
            break

# Calculate true positives and false negatives in cropped region
for pointp in points_p_cropped:
#for pointp in points_p:
    point_in_polygon_p = False
    for polygon in polygons:
        if polygon.contains(pointp):
            true_positives += 1
            point_in_polygon_p = True
            break
    if not point_in_polygon_p:
        false_negatives += 1


# Calculate false positives and true negatives
for pointn in points_n_cropped:
#for pointn in points_n:
    point_in_polygon_n = False
    for polygon in polygons:
        if polygon.contains(pointn):
            false_positives += 1
            point_in_polygon_n = True
            break
    if not point_in_polygon_n:
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
