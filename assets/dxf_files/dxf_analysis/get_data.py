import ezdxf

# Define the DXF file
dxf_file = "Top_1.dxf"  # Assuming the file is in the same folder as the script

# Load the DXF file
try:
    doc = ezdxf.readfile(dxf_file)
except IOError:
    print(f"Error: The file '{dxf_file}' was not found.")
    exit(1)

# Initialize data storage for polylines, coordinates, and drilling data
polylines = []
coordinates = []
drilling_data = []

# Function to normalize polyline data
def normalize_polyline(polyline):
    polyline_data = []
    # Get the polyline thickness directly from the polyline's DXF attributes
    thickness = getattr(polyline.dxf, 'thickness', None)  # Using getattr to handle missing attributes
    for vertex in polyline.vertices:
        vertex_data = {
            "x": vertex.dxf.location.x,
            "y": vertex.dxf.location.y,
            "z": vertex.dxf.location.z,
            "thickness": thickness  # Set thickness if available in the polyline
        }
        polyline_data.append(vertex_data)
    return polyline_data

# Iterate through all entities in the modelspace
for entity in doc.modelspace():
    if entity.dxftype() == "POLYLINE" and len(polylines) == 0:  # Only keep the first polyline
        # Normalize polyline and extract points
        polyline_points = normalize_polyline(entity)
        polylines.append(polyline_points)

    elif entity.dxftype() in ["LINE", "ARC", "POINT"]:  # Exclude CIRCLE type
        # Extract basic geometric data for other entities
        if entity.dxftype() == "LINE":
            coordinates.append({
                "type": "LINE",
                "start": entity.dxf.start,
                "end": entity.dxf.end
            })
        elif entity.dxftype() == "ARC":
            coordinates.append({
                "type": "ARC",
                "center": entity.dxf.center,
                "radius": entity.dxf.radius,
                "start_angle": entity.dxf.start_angle,
                "end_angle": entity.dxf.end_angle
            })
        elif entity.dxftype() == "POINT":
            coordinates.append({
                "type": "POINT",
                "position": entity.dxf.location
            })

    # Example for horizontal/vertical drilling (customize based on your data)
    if entity.dxftype() == "CIRCLE" and "drill" in entity.dxf.layer.lower():
        drilling_data.append({
            "center": entity.dxf.center,
            "radius": entity.dxf.radius,
            "layer": entity.dxf.layer  # Layer name
        })

# Output the polyline data with max x, max y, and max thickness

print("Workpiece data:")
for idx, polyline in enumerate(polylines, 1):
    max_x = max(abs(point['x']) for point in polyline)
    max_y = max(abs(point['y']) for point in polyline)
    max_thickness = max(abs(point['thickness']) for point in polyline if point['thickness'] is not None)
    
    print(f"Length = X: {max_x}\nWidth = Y: {max_y}\nThickness = Z: {max_thickness}")
    
# Output the drilling data with enumerated layers starting from 1
print("\nDrilling Data:")
for idx, data in enumerate(drilling_data, 1):  # Start enumeration from 1
    if 'EDGE' in data['layer']:
        print(f"{idx}. Layer: {data['layer']}, Center: {data['center']}, Radius: {data['radius']}")

