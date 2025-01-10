# find the coordinates of the workpiece corners
# the size of the workpiece

import ezdxf

# Load the DXF file
dxf_file = "Top_1.dxf"  # Replace with your file path
doc = ezdxf.readfile(dxf_file)

# Initialize data storage for polylines
polylines = []

# Iterate through all entities in the modelspace
for entity in doc.modelspace():
    if entity.dxftype() == "POLYLINE":
        # Add each vertex in the polyline
        polyline_points = [{"start": vertex.dxf.location, "end": vertex.dxf.location} for vertex in entity.vertices]
        polylines.append(polyline_points)

# Check if any polylines were detected
if not polylines:
    print("No polylines found in the DXF file.")
else:
    # Output the polyline data
    for idx, polyline in enumerate(polylines, 1):
        print(f"Polyline {idx}:")
        for i, point in enumerate(polyline, 1):
            print(f"  {i}. Start: {point['start']}, End: {point['end']}")

