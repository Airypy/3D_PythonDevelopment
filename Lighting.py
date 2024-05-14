import bpy

def setup_basic_lighting():
    # Remove existing lights
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='LIGHT')
    bpy.ops.object.delete()

    # Add point lights
    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(1, 4, 5))
    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(7, 0, 2))
    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(-0, 3, 5))

    # Add spotlights
    bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(91, 89, 5))
    bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(00, -8, 5))
    
    # Configure lights
    for obj in bpy.context.selected_objects:
        obj.data.energy = 1000  # Adjust energy as needed
        obj.data.color = (1, 1, 1)  # Set light color to white
        obj.data.use_shadow = True
        obj.data.shadow_soft_size = 2  # Set shadow soft size

if __name__ == "__main__":
    setup_basic_lighting()
