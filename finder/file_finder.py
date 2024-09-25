import os
import fnmatch

# Define the folder to search and the output file path
search_folder = 'D:\\'
output_file = 'C:\\'

# Configurable size threshold in bytes (change this as needed)
size_threshold = 3 * 1024 * 1024 * 1024  # Example: 3 GB

# List of file extensions or wildcards to include (e.g., ['*.mp4', '*.mkv', '*.zip'])
extensions = ['*.*']  # Adjust as necessary

# Set logging depth and interval
folder_depth = 3  # Adjust this value to control how deep the folder path should be displayed
log_interval = 10000  # Log progress every 1000 files

# List to store file paths that are larger than the threshold
large_files = []

# Initialize counters
total_files_scanned = 0

# Walk through all directories and subdirectories
for root, dirs, files in os.walk(search_folder):
    # Calculate and display the folder depth
    depth = len(os.path.relpath(root, search_folder).split(os.sep))
    if depth <= folder_depth:
        print(f"Searching in folder: {root}")

    for file in files:
        # Check if the file matches the specified extensions/wildcards
        if any(fnmatch.fnmatch(file, pattern) for pattern in extensions):
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > size_threshold:
                    large_files.append(f"{file_path} - {file_size / (1024 ** 3):.2f} GB")

                # Increment the file counter
                total_files_scanned += 1

                # Log progress every 'log_interval' files
                if total_files_scanned % log_interval == 0:
                    print(f"Scanned {total_files_scanned} files so far...")

            except (OSError, PermissionError):
                # Skip files that cannot be accessed
                continue

# Save the output to the specified file
with open(output_file, 'w', encoding='utf-8') as f:
    if large_files:
        f.write("\n".join(large_files))
        print(f"List of files exceeding the size limit has been saved to {output_file}")
    else:
        f.write("No files exceeding the size limit were found.")
        print("No files exceeding the size limit were found.")

print(f"Total files scanned: {total_files_scanned}")
