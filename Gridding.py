import bpy
import random

# Function to duplicate objects and apply random color to materials
def duplicate_object(obj):
    duplicate = obj.copy()
    duplicate.data = obj.data.copy()
    bpy.context.collection.objects.link(duplicate)

    # Applying a random color to the material
    material = bpy.data.materials.new(name="Material")
    material.diffuse_color = (random.random(), random.random(), random.random(), 1.0)
    duplicate.data.materials.append(material)

    return duplicate

# Function to arrange objects in a 4x4 grid
def arrange_in_grid(objects):
    rows = 4
    cols = 4
    spacing = 2.0

    for index, obj in enumerate(objects):
        row = index // cols
        col = index % cols
        obj.location = (col * spacing, row * spacing, 0)

# Main script
selected_object = bpy.context.active_object
duplicates = []

# Duplicate the selected object and arrange duplicates in a grid
for _ in range(16):
    dup_obj = duplicate_object(selected_object)
    duplicates.append(dup_obj)

arrange_in_grid(duplicates)
