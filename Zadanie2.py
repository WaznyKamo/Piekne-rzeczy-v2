import zipfile
import string
all_files = ""
with zipfile.ZipFile("zadanie_1_words.zip", 'r') as zip:
    file_names = zip.namelist()
    for file_name in file_names:
        file = str(zip.read(file_name).lower())
        all_files += file

for sign in string.ascii_lowercase:
    print(("{} x {}").format(str(sign), all_files.count(str(sign))))

