import os
import shutil

# Define the project structure
project_structure = {
    "dynamic_pricing_system": [
        "pricing/__init__.py",
        "pricing/product.py",
        "pricing/pricing_strategy.py",
        "pricing/factory.py",
        "database/db_config.py",
        "tests/__init__.py",
        "tests/test_pricing.py",
        "config.py",
        "main.py",
        "requirements.txt",
        # "README.md"     Also add readme file if you want
    ]
}


# Function to create files and folders
def create_project_structure():
    for root_folder, files in project_structure.items():
        # Create the main project folder
        os.makedirs(root_folder, exist_ok=True)

        for file_path in files:
            # Create necessary subdirectories
            full_path = os.path.join(root_folder, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            # Create the files in the subdirectories
            with open(full_path, "w") as f:
                f.write("import")

    print("Project structure created successfully!")


# Function to move setup file to a scripts folder
def move_project_structure():
    script_name = "setup.py"
    target_folder = "scripts"

    # Creating the 'scripts' folder if it doesn't exist
    os.makedirs(target_folder, exist_ok=True)

    # Move the setup file
    shutil.move(script_name, os.path.join(target_folder, script_name))
    print(f"Moved {script_name} to {target_folder} folder")


# Run the function
if __name__ == "__main__":
    create_project_structure()
    move_project_structure()