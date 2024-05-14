**Blender Script Repository**

This repository contains a collection of scripts and plugins for Blender, designed to automate various tasks and enhance workflow efficiency. Each script is documented below along with instructions on how to use and test them.

### Duplicate and Arrange Objects in a 4x4 Grid

- **Script Name:** `Gridding.py`
- **Description:** This script duplicates a selected object multiple times and arranges the duplicates in a 4x4 grid. Each duplicate object is assigned a material with a different color and texture.
- **Usage:** Select the object you want to duplicate, then run the script. The duplicates will be created and arranged automatically.
- **Testing:** Select different objects of varying sizes and shapes, and test the script to ensure that duplicates are created and arranged correctly.

### Basic Lighting Setup for Blender Scene

- **Script Name:** `Lighting.py`
- **Description:** This script sets up basic lighting for a Blender scene by adding and configuring point lights and spotlights.
- **Usage:** Run the script to automatically add and configure lights in the scene.
- **Testing:** Create different scenes with varying objects and test the script to ensure that lights are added and configured appropriately.

### Find Parent and Children of Main Object

- **Script Name:** `Hierarchy.py`
- **Description:** This script finds the name of the main object's parent and lists the names of all its children, regardless of hierarchy depth.
- **Usage:** Select the main object and run the script to find its parent and children.
- **Testing:** Create complex hierarchies with nested objects and test the script to verify that it correctly identifies the parent and lists all children.

### Object Data Fetch and JSON Export Plugin

- **Plugin Name:** `Store_Data.zip`
- **Description:** This Blender plugin fetches data of selected objects and stores it in a JSON file in local storage. The exported data includes location, rotation (in degrees), scale, parent name (if any), and children count.
- **Usage:** Select the objects you want to export data for, then use the plugin to export to JSON.
- **Testing:** Select various objects with different hierarchies and properties, then export the data using the plugin to verify the correctness of the JSON output.

### Model Export Plugin

- **Plugin Name:** `3D_Pipeline.zip`
- **Description:** This Blender plugin exports models in other formats, allowing users to specify the export path and file format (e.g., .obj, .fbx).
- **Usage:** Use the plugin interface to specify the export path and file format, then export the model.
- **Testing:** Export different models to various formats using the plugin and verify the exported files in external applications.

### Additional Information

- **Compatibility:** These scripts and plugins are compatible with Blender versions [3.6].
- **Dependencies:** No additional dependencies are required to run these scripts and plugins.

Feel free to use, modify, and contribute to this repository. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request. Thank you for using our Blender script repository!
