import os

# Add the directory that contains the files
directory = "./"

# Get a list of all the files in the directory
files = os.listdir(directory)

# Iterate through the files and remove the leading zeros
for file in files:
  # Ignore any files that don't have leading zeros
  if not file[0] == "0":
    continue

  # Split the file name into the base name and extension
  base, ext = os.path.splitext(file)

  # Remove the leading zeros from the base name
  base = base.lstrip("0")

  # Recreate the file name with the updated base name
  new_file = base + ext

  # Rename the file
  os.rename(os.path.join(directory, file), os.path.join(directory, new_file))