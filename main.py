import os

from paddleocr import PaddleOCR
from prettytable import PrettyTable

directory = r".\images"
ocr = PaddleOCR(use_angle_cls=True, lang="en")
field_names = [""]
fields = [
    "Max HP",
    "ATK",
    "DEF",
    "Elemental Mastery",
    "Crit Rate",
    "Crit DMG",
    "Healing Bonus",
    "Incoming Healing Bonus",
    "Energy Recharge",
    "CD Reduction",
    "Shield Strength",
    "Pyro DMG Bonus",
]
for i, field in enumerate(fields):
    fields[i] = [field]

for file_name in os.listdir(directory):
    if file_name == ".gitkeep":
        continue
    field_names.append(file_name)
    i = 0
    img_path = os.path.join(directory, file_name)
    result = ocr.ocr(img_path, cls=True)
    for line in result:
        print(line)
        text = line[1][0]
        if text.startswith("+"):
            if not text.endswith("%"):
                value = int(text[1:].replace(",", ""))
                text = "+{:,}".format(value)
            fields[i].append(text)
            i += 1

table = PrettyTable()
table.field_names = field_names
table.add_rows(fields)
table.align = "l"
print(table)
