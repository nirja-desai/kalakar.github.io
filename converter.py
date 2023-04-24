import json
import os

# Load the GeoJSON file
with open('geo_json_final.geojson', 'r') as f:
    data = json.load(f)

# Loop through each feature in the GeoJSON file
for feature in data['features']:
    # Change the file extension for the "image" property
    filename, ext = os.path.splitext(feature['properties']['image'])
    feature['properties']['image'] = f"{filename}.jpg"

# Save the modified GeoJSON file
with open('geo_json_final.geojson', 'w') as f:
    json.dump(data, f)
