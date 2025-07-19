import os
import shutil

# Define file type categories
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx'],
    'Audio': ['.mp3', '.wav'],
    'Executables': ['.exe', '.msi'],
    'Archives': ['.zip', '.rar'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
}

# Set your custom directory path here
path = "C:/Users/hp/OneDrive/Desktop/organizer"

# Change working directory
os.chdir(path)
files = os.listdir()

print(f"\n🔍 Scanning folder: {path}")
print(f"📁 Files found: {files}\n")

# Organize files based on extension
for file in files:
    file_path = os.path.join(path, file)

    if os.path.isdir(file_path):
        print(f"📂 Skipping folder: {file}")
        continue

    _, ext = os.path.splitext(file)
    moved = False

    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            folder_path = os.path.join(path, folder)

            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
                print(f"📁 Created folder: {folder}")

            new_path = os.path.join(folder_path, file)
            shutil.move(file_path, new_path)
            print(f"✅ Moved {file} to {folder}/")
            moved = True
            break

    if not moved:
        print(f"⚠ Skipped {file} — unknown extension: {ext}")

print("\n✅ Done organizing files.")