# Folder Sorter

## Overview
Folder Sorter is a Python script that automatically organizes files in a directory into categorized subdirectories based on file types, mostly for downloads folder.

## Features
- Automatically sorts files into categories:
  - Documents
  - Images
  - Videos
  - Audio
  - Archives
  - Code
  - Installers
  - Misc
- Works with any directory
- Preserves original file names
- Handles duplicate file names by adding a counter

## Prerequisites
- Python 3.7+
- PyInstaller (optional, for creating executable)

## Installation
Clone the repository
```bash
git clone https://github.com/Will6855/folder-sorter.git
cd folder-sorter
```
- or download the executable from the [release section](https://github.com/Will6855/folder-sorter/releases)


## Usage

### Running Directly with Python
```bash
python folder_sorter.py  # Sorts current directory
python folder_sorter.py /path/to/directory  # Sorts specific directory
```

### Creating Executable
```bash
pyinstaller --onefile --name="FolderSorter" folder_sorter.py
```

### Using the Executable
- Double-click `FolderSorter.exe` to sort the current directory
- Drag and drop the executable to any folder to sort its contents
- Run from command line with optional path argument

## Sorting Categories
- **Documents**: PDF, DOCX, TXT, XLSX, etc.
- **Images**: JPG, PNG, GIF, etc.
- **Videos**: MP4, AVI, MKV, etc.
- **Audio**: MP3, WAV, FLAC, etc.
- **Archives**: ZIP, RAR, 7Z, etc.
- **Code**: Python, JavaScript, HTML, etc.
- **Installers**: EXE, MSI, DMG, etc.
- **Misc**: Unsorted or unrecognized files

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Disclaimer
Always backup your files before running automated sorting scripts.