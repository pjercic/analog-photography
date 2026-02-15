import os

def create_structure():
    # The root directory name
    root_dir = "analog-open-science"
    
    # The folder structure dictionary
    structure = {
        "01_primary": ["01_physics_ray.md", "02_chemistry_sun.md", "03_art_observation.md"],
        "02_secondary": ["01_physics_optics.md", "02_chemistry_latent.md", "03_history_modernism.md"],
        "03_high_school": ["01_physics_reciprocity.ipynb", "02_chemistry_redox.md", "03_psych_gestalt.md"],
        "04_university": ["01_quantum_sensitometry.ipynb", "02_emulsion_engineering.md", "03_philosophy_ethics.md"],
        "lab_manuals": ["rig_room_obscura.md", "rig_sliding_box.md", "rig_densitometer.md"],
        "safety_data": ["general_lab_safety.md", "chemical_msds.md"],
        "assets": [] # For images and diagrams
    }

    # Create root directory
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
        print(f"Created root directory: {root_dir}")

    # Create subdirectories and files
    for folder, files in structure.items():
        folder_path = os.path.join(root_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")
        
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                # Add a simple header to each file
                title = file.replace("_", " ").replace(".md", "").replace(".ipynb", "").title()
                f.write(f"# {title}\n\n*Content coming soon...*")
            print(f"  -> Created file: {file}")

    print("\n✅ Course structure generated successfully!")
    print(f"Next step: 'cd {root_dir}' and 'git init'")

if __name__ == "__main__":
    create_structure()