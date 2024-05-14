import bpy

def get_children_names_recursive(obj, parent_name, children_names):
    for child in obj.children:
        children_names.append(child.name)
        get_children_names_recursive(child, parent_name, children_names)

def main():
    # Get the selected object
    selected_obj = bpy.context.active_object
    if not selected_obj:
        print("Please select an object.")
        return
    
    # Check if the selected object has a parent
    if selected_obj.parent:
        parent_name = selected_obj.parent.name
        print("Parent name:", parent_name)
    else:
        print("The selected object has no parent.")
        parent_name = None
    
    # Get names of all children recursively
    children_names = []
    get_children_names_recursive(selected_obj, parent_name, children_names)
    
    # Print the names of all children
    print("Children names:")
    for child_name in children_names:
        print(child_name)

if __name__ == "__main__":
    main()
