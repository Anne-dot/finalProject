import ezdxf

# Load the DXF file
dxf_file = "Top_1.dxf"  # Replace with your file path
doc = ezdxf.readfile(dxf_file)

# Initialize data storage
coordinates = []
drilling_data = []

# Iterate through all entities in the modelspace
for entity in doc.modelspace():
    if entity.dxftype() in ["LINE", "CIRCLE", "ARC", "POINT"]:
        # Extract basic geometric data
        if entity.dxftype() == "LINE":
            coordinates.append({
                "type": "LINE",
                "start": entity.dxf.start,
                "end": entity.dxf.end
            })
        elif entity.dxftype() == "CIRCLE":
            coordinates.append({
                "type": "CIRCLE",
                "center": entity.dxf.center,
                "radius": entity.dxf.radius
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

# Output results
print("Drilling Data:")
for idx, data in enumerate(drilling_data, 1):
    print(f"{idx}. Layer: {data['layer']}, Center: {data['center']}, Radius: {data['radius']}")
