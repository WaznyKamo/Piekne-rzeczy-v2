# W plikach word_0.txt, word_1.txt, ..., word_29.txt znajdują się pojedyncze słowa
# składające się z małych i wielkich liter ASCII.
# Pliki word_0.txt, word_1.txt, ..., word_29.txt są spakowane w zadanie_1_words.zip.
# Twoim zadaniem jest policzenie, ile razy każda z liter występuje we wszystkich
# plikach. Małe i wielkie litery liczymy razem.

import zipfile
import string
all_files = ""
with zipfile.ZipFile("zadanie_1_words.zip", 'r') as zip:
    file_names = zip.namelist()
    for file_name in file_names:
        file = str(zip.read(file_name).lower())
        all_files += file

for sign in string.ascii_lowercase:
    print("{} x {}".format(str(sign), all_files.count(str(sign))))

