# Script: generate_files.py

## Description
This script creates a folder with the current time and date, and generates 10 .txt files inside the folder, each containing Lorem Ipsum text.

## Dependencies
- Python 3.x
- lorem-text library

## Usage
1. Ensure Python 3.x and the necessary dependencies are installed.
2. Run the script using the command: `python generate_files.py`.

## Steps
1. Import required modules:
   - `os` for file system operations
   - `lorem_text` for generating Lorem Ipsum text
   - `datetime` for retrieving the current time and date.

2. Define the current time and date:
   - Using `datetime.now().strftime("%Y-%m-%d_%H-%M-%S")` to format the current time.

3. Create a folder with the current time and date:
   - The folder name is constructed using the format "folder_<current_time>".
   - The `os.makedirs()` function is used to create the folder, ensuring it is created only if it doesn't exist (`exist_ok=True`).

4. Generate 10 .txt files inside the folder:
   - Iterate from 1 to 10 using a for loop.
   - Create a file name for each iteration using the format "<folder_name>/file<i>.txt".
   - Use the `lorem.paragraph()` function from the `lorem_text` library to generate Lorem Ipsum text.
   - Open each file in write mode (`"w"`) and write the generated text into it.

5. Print success message:
   - Display the message "Folder and files created successfully.".

## Example Output
- The script will create a folder named "folder_<current_time>" (e.g., folder_2023-06-02_15-30-45).
- Inside the folder, 10 .txt files will be generated (file1.txt, file2.txt, ..., file10.txt) with Lorem Ipsum text.

## Notes
- Ensure that the `lorem_text` library is installed before running the script. Install it using `pip install lorem-text`.
- Modify the script as needed to customize the folder and file names or adjust the number of files generated.
- Exercise caution when running the script multiple times, as it may overwrite existing files or folders.

