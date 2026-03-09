import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Programs": [".exe", ".msi"]
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            moved = False
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"Moved: {filename} -> {category}")
                    moved = True
                    break
            
            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved: {filename} -> Others")

def main():
    print("FILE ORGANIZER")
    folder = input("Enter folder path to organize: ").strip()
    organize_files(folder)
    print("Done organizing files.")

if __name__ == "__main__":
    main()