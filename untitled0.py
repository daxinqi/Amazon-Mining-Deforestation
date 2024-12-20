import json
from shapely.geometry import shape, mapping
from shapely.ops import transform, unary_union
from pyproj import Proj, Transformer

def calculate_total_area_in_square_meters(geojson_path):
    with open(geojson_path, 'r') as f:
        geojson_data = json.load(f)
        
    geometries = []

    for feature in geojson_data.get('features', []):
        geom = shape(feature['geometry'])
        if geom.is_valid:
            geometries.append(geom)

    # Combine all geometries into one multi-polygon object
    combined_geometry = unary_union(geometries)

    # Define a projection (e.g., UTM zone 33N)
    # It's important to choose an appropriate UTM zone or another projection for your data
    utm_proj = Proj(proj="utm", zone=33, ellps="WGS84", datum="WGS84")

    # Create a transformer to convert from WGS84 to the UTM projection
    transformer = Transformer.from_proj("epsg:4326", utm_proj)  # WGS84 to UTM

    # Reproject the geometry to UTM
    reprojected_geometry = transform(transformer.transform, combined_geometry)

    # Calculate the total area in square meters
    total_area_square_meters = reprojected_geometry.area
    
    return total_area_square_meters

# Path to your GeoJSON file
geojson_path = 'C:\\Users\\daxin\\Desktop\\mining-detector-main\\test_region_48px_v3.2-3.7ensemble_0.50_2024-01-01_2024-02-01.geojson'

total_area_square_meters = calculate_total_area_in_square_meters(geojson_path)
print(f"Total area of all polygon objects in square meters: {total_area_square_meters}")

