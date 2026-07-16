import os
import shutil

curr=os.getcwd()

folders=["Above 1B","Above 1KB","Above 1MB"]
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created: {folder}")
small=os.path.join(curr,"1B")
medium=os.path.join(curr,"1KB")
large=os.path.join(curr,"1MB")

ignore_dirs = {'Above 1B', 'Above 1KB', 'Above 1MB', '.ipynb_checkpoints'}
for root,dirnames,files in os.walk(curr):
    dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
    for file in files:
        full_path = os.path.join(root, file)
        if small in full_path or medium in full_path or large in full_path:
            continue
        try:
            file_size = os.path.getsize(full_path)
        except OSError:
            continue
        if 1<os.path.getsize(full_path)<1024:
            shutil.copy(full_path,small)
        elif 1025<os.path.getsize(full_path)<10*1024:
            shutil.copy(full_path,medium)
        else :
            shutil.copy(full_path,large)
print("Sorting has been done. Give someone a hug")