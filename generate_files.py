import os
from lorem_text import lorem
from datetime import datetime

# Number of files to be created
x = 501

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
folder_name = "folder_{}".format(current_time)
os.makedirs(folder_name, exist_ok=True)

for i in range(1, x):
    file_name = "{}/file{}.txt".format(folder_name, i)
    with open(file_name, "w") as file:
        file.write(lorem.paragraph())

print("Folder and files created successfully.")
