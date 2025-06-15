import os
import shutil
import platform

system = platform.system()

categories = {"Videos" : ["mov", "mp4"], "Documents" : ["docx", "pdf", "md", "txt", "odt", "doc"], "Images" : ["jpg", "svg", "jpeg", "png", "gif"], "Installers" : ["iso", "dmg", "exe", "deb", "appimage"], "Zip Files" : ["zip", "gz", "tar", "7z", "rar"], "Unknown" : ["unknown"], "Code" : ["py", "cpp", "js", "java", "cs", "sh"], "Audio" : ["mp3", "wav"], "Spreadsheet" : ["csv", "xls", "xlsx", "ods"]}

user = os.getlogin()
path = ""

if system == "Linux":
    path = f"/home/{user}/Downloads"
elif system == "Darwin":
    path = f"/Users/{user}/Downloads"
elif system == "Windows":
    path = f"C:\\Users\\{user}\\Downloads"

os.chdir(path)
dir = path
files = []
file_paths = []
type = []
moved = False

for file in os.listdir(dir):
    file_path = os.path.join(dir, file).strip(path)
    file_path2 = os.path.join(dir, file)
    if os.path.isfile(file_path2):
        files.append(file)
        file_paths.append(file_path)

for key in categories:
    try:
        os.mkdir(key)
    except FileExistsError as e:
        print(f"{e}. The directory already exists")
        print("Continuing with process. If the existing directory is not where you want to store your files, please rename it and retry.")
        continue

print("Made directories, processing files.")

for file in files:
    file_list = file.split(".")

    for val in categories:
        for file_type in categories[val]:
            if file_list[-1] == file_type:
                print(f"Moving {file} to {val}.")
                shutil.move(f"{path}/{file}", f"{path}/{val}/{files[files.index(file)]}")
                moved = True
            
if moved == False:
    print(f"Moving unknown file: {file} to directory: 'Unknown'.")
    shutil.move(f"{path}/{file}", f"{path}/Unknown/{files[files.index(file)]}")




