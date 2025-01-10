import os


def get_folder_statistics(path):
    folder_size = 0
    folder_count = 0
    file_count = 0

    for root, dirs, files in os.walk(path):
        folder_count += len(dirs)
        file_count += len(files)
        for file in files:
            file_path = os.path.join(root, file)
            try:
                folder_size += os.path.getsize(file_path)
            except (OSError, FileNotFoundError):
                continue  # Skip inaccessible files

    return {
        "folder_size": folder_size,
        "subfolder_count": folder_count,
        "file_count": file_count
    }


def compare_paths(path1, path2):
    if not os.path.exists(path1) or not os.path.exists(path2):
        raise FileNotFoundError("One or both paths do not exist.")

    stats1 = get_folder_statistics(path1)
    stats2 = get_folder_statistics(path2)

    print("\nComparison of Paths")
    print(f"{'Metric':<20} {'Path 1':<15} {'Path 2':<15}")
    print(f"{'-' * 50}")
    print(f"{'Folder Size (bytes)':<20} {stats1['folder_size']:<15} {stats2['folder_size']:<15}")
    print(f"{'Subfolder Count':<20} {stats1['subfolder_count']:<15} {stats2['subfolder_count']:<15}")
    print(f"{'File Count':<20} {stats1['file_count']:<15} {stats2['file_count']:<15}")


if __name__ == "__main__":
    path1 = input("Enter the first path: ").strip()
    path2 = input("Enter the second path: ").strip()

    try:
        compare_paths(path1, path2)
    except Exception as e:
        print(f"Error: {e}")
