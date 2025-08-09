import os
from datetime import datetime
import toml


def find_pyproject_toml(start_path, max_depth=3):
    for root, dirs, files in os.walk(start_path):
        depth = root[len(start_path) :].count(os.sep)
        if "pyproject.toml" in files:
            return os.path.join(root, "pyproject.toml")
        if depth >= max_depth - 1:
            del dirs[:]  # Don't recurse further down this path
    return None


def update_version_in_pyproject(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        pyproject_data = toml.load(file)

    current_timestamp = datetime.now().strftime("%Y.%m.%d.%H%M%S")

    # Check if the necessary keys exist
    if "project" not in pyproject_data:
        print(
            f"Error: 'project' key is missing in {file_path}. Please add it manually."
        )
        return
    if "version" not in pyproject_data["project"]:
        print(
            f"Error: 'version' key is missing under 'project' in {file_path}. Please add it manually."
        )
        return

    pyproject_data["project"]["version"] = current_timestamp

    with open(file_path, "w", encoding="utf-8") as file:
        toml.dump(pyproject_data, file)


if __name__ == "__main__":
    start_directory = os.getcwd()
    pyproject_path = find_pyproject_toml(start_directory)

    if pyproject_path:
        print(f"Found pyproject.toml at {pyproject_path}")
        update_version_in_pyproject(pyproject_path)
        print(f"Updated version to {datetime.now().strftime('%Y.%m.%d.%H%M%S')}")
    else:
        print("No pyproject.toml found within the specified depth.")
