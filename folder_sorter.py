import os
import sys
import shutil
from pathlib import Path

def sort_downloads(download_path):
    download_path = os.path.abspath(download_path)
    if not os.path.isdir(download_path):
        print(f"Error: {download_path} is not a valid directory.")
        sys.exit(1)

    # Unified categories map with extensions and subcategories
    categories = {
        'Documents': {
            'extensions': ['.pdf', '.docx', '.doc', '.txt', '.rtf', '.xlsx', '.xls', '.pptx', '.ppt', '.csv', '.odt', '.ods', '.odp'],
            'subcategories': {
                'Word': ['.docx', '.doc', '.odt'],
                'Excel': ['.xlsx', '.xls', '.ods'],
                'PowerPoint': ['.pptx', '.ppt', '.odp'],
                'PDF': ['.pdf'],
                'Spreadsheets': ['.csv'],
                'Text': ['.txt', '.rtf']
            }
        },
        'Images': {
            'extensions': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
            'subcategories': {
                'Photos': [],
                'Screenshots': [],
                'Icons': [],
                'Wallpapers': []
            }
        },
        'Videos': {
            'extensions': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
            'subcategories': {
                'Movies': [],
                'Clips': [],
                'TV Shows': [],
            }
        },
        'Audio': {
            'extensions': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'],
            'subcategories': {
                'Music': [],
                'Recordings': [],
                'Podcasts': [],
                'Audiobooks': []
            }
        },
        'Archives': {
            'extensions': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
            'subcategories': {
                'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
                'Extracted': []
            }
        },
        'Code': {
            'extensions': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.go', '.rb', '.php', '.swift', '.kt'],
            'subcategories': {
                'Python': ['.py'],
                'JavaScript': ['.js'],
                'Web': ['.html', '.css', '.rb', '.php'],
                'Desktop': ['.java', '.cpp', '.c'],
                'Mobile': ['.go', '.swift', '.kt']
            }
        },
        'Installers': {
            'extensions': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
            'subcategories': {
                'Windows': ['.exe', '.msi'],
                'Mac': ['.dmg', '.pkg'],
                'Linux': ['.deb', '.rpm']
            }
        }
    }

    # Create main directories and subdirectories
    main_dirs = list(categories.keys()) + ['Misc']
    for main_dir in main_dirs:
        os.makedirs(os.path.join(download_path, main_dir), exist_ok=True)
        
        # Create subdirectories for known categories
        if main_dir in categories:
            for subcat in categories[main_dir]['subcategories']:
                os.makedirs(os.path.join(download_path, main_dir, subcat), exist_ok=True)

    files_moved, folders_moved = 0, 0

    # Get the path of the current executable
    exe_path = sys.executable if getattr(sys, 'frozen', False) else None

    def move_item(src_path, dest_path):
        nonlocal files_moved, folders_moved
        counter = 1
        while os.path.exists(dest_path):
            name, ext = os.path.splitext(os.path.basename(dest_path))
            dest_path = os.path.join(os.path.dirname(dest_path), f"{name}_{counter}{ext}")
            counter += 1
        
        shutil.move(src_path, dest_path)
        print(f"Moved {os.path.basename(src_path)} to {os.path.relpath(dest_path, download_path)}")
        return 1 if os.path.isfile(dest_path) else 0

    # Move existing folders to Archive/Extracted
    for item in os.listdir(download_path):
        itempath = os.path.join(download_path, item)
        if item not in main_dirs and os.path.isdir(itempath):
            # Skip the executable's directory
            if exe_path and os.path.dirname(exe_path) == itempath:
                continue
            
            dest_path = os.path.join(download_path, 'Archive', 'Extracted', item)
            folders_moved += move_item(itempath, dest_path)

    # Sort and move files
    for item in os.listdir(download_path):
        itempath = os.path.join(download_path, item)
        if item in main_dirs or os.path.isdir(itempath):
            continue

        # Skip the executable itself
        if exe_path and itempath == exe_path:
            continue

        file_ext = Path(item).suffix.lower()
        moved = False

        for category, details in categories.items():
            if file_ext in details['extensions']:
                # Find the subcategory for the file extension
                for subcategory, extensions in details['subcategories'].items():
                    if file_ext in extensions:
                        dest_path = os.path.join(download_path, category, subcategory, item)
                        files_moved += move_item(itempath, dest_path)
                        moved = True
                        break
                    else:
                        dest_path = os.path.join(download_path, category, item)
                        folders_moved += move_item(itempath, dest_path)
                        moved = True
                        break
                
                if moved:
                    break

        # Move unrecognized files to Misc
        if not moved:
            dest_path = os.path.join(download_path, 'Misc', item)
            files_moved += move_item(itempath, dest_path)

    print(f"Total files moved: {files_moved}")
    print(f"Total folders moved to Decompressed: {folders_moved}")

def main():
    # Use the current working directory as the default path
    download_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    sort_downloads(download_path)
    
    # Wait for user to press Enter before exiting
    input("\nPress Enter to exit...")

if __name__ == '__main__':
    main()