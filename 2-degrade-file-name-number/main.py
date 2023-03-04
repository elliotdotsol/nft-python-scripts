import os
import shutil

# Set the directory where the files are located
src_dir = './original'

# Set the directory where the renamed files should be stored
dst_dir = './new'

# Make sure the destination directory exists
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# Iterate through all files in the source directory
for filename in os.listdir(src_dir):
    # Split the filename into a base name and an extension
    base, ext = os.path.splitext(filename)
    # Check if the base name is a number
    if base.isdigit():
        # Convert the base name to an integer and decrement it by 1
        new_base = str(int(base) - 1)
        # Build the new filename by joining the new base name and the extension
        new_filename = new_base + ext
        # Construct the full file paths for the source and destination files
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, new_filename)
        # Copy the file from the source to the destination
        shutil.copy(src_path, dst_path)