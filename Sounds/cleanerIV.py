import os
import re
from pathlib import Path

def normalize_track_name(filename: str) -> str:
    """
    Converts '69. End of the Journey.ogg' -> 'END_OF_THE_JOURNEY.ogg'
    """
    path = Path(filename)
    stem = path.stem
    ext = path.suffix

    # Remove number prefix like '69. ' or '002 - '
    stem = re.sub(r'^\d+\s*[-.]?\s*', '', stem)

    # Replace all non-alphanumeric characters with underscores
    stem = re.sub(r'[^\w]+', '_', stem).strip('_')

    return f"{stem.upper()}{ext}"

def rename_ogg_files_in_own_folder():
    folder = Path(__file__).parent.resolve()
    print(f"[INFO] Script is running in: {folder}")

    renamed_any = False
    for file in folder.iterdir():
        if file.is_file() and file.suffix.lower() == ".ogg":
            new_name = normalize_track_name(file.name)
            new_path = folder / new_name

            print(f"Found: {file.name} -> {new_name}")
            if file.name != new_name:
                file.rename(new_path)
                print(f"Renamed to: {new_name}")
                renamed_any = True
            else:
                print("Already normalized.")

    if not renamed_any:
        print("[INFO] No renames were necessary.")

# 🔁 Run it automatically
if __name__ == "__main__":
    rename_ogg_files_in_own_folder()
