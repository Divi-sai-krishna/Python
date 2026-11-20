import os
import shutil


def unique_path(folder, filename):
    """If filename already exists in folder, add _1, _2, ... before the extension."""
    base, ext = os.path.splitext(filename)
    path = os.path.join(folder, filename)
    counter = 1
    while os.path.exists(path):
        path = os.path.join(folder, base + "_" + str(counter) + ext)
        counter += 1
    return path


def move_jpgs(source, destination):
    """Move every .jpg/.jpeg file from source into destination. Returns the count."""
    # Create the destination folder if it doesn't exist yet
    os.makedirs(destination, exist_ok=True)

    moved = 0
    for filename in os.listdir(source):
        full_path = os.path.join(source, filename)

        # Skip sub-folders; only look at files
        if not os.path.isfile(full_path):
            continue

        # Case-insensitive match so .JPG and .jpeg are caught too
        if filename.lower().endswith((".jpg", ".jpeg")):
            target = unique_path(destination, filename)
            shutil.move(full_path, target)
            print("Moved:", filename, "->", target)
            moved += 1

    return moved


def main():
    print("=== JPG MOVER ===")
    source = input("Folder to scan (press Enter for current folder): ").strip() or "."
    destination = input("New folder name (press Enter for 'jpg_images'): ").strip() or "jpg_images"

    if not os.path.isdir(source):
        print("Error: '" + source + "' is not a valid folder.")
        return

    # If the destination is just a name, create it inside the source folder
    if not os.path.isabs(destination):
        destination = os.path.join(source, destination)

    count = move_jpgs(source, destination)

    if count == 0:
        print("No .jpg files found.")
    else:
        print("\nDone! Moved " + str(count) + " file(s) to " + destination)


if __name__ == "__main__":
    main()
