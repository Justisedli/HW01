

import json

with open("alice.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()
text = text.replace(" ", "")
text = text.replace("\n", "")

znak_count = {}
for znak in text:
    if znak in znak_count:
        znak_count[znak] += 1
    else:
        znak_count[znak] = 1

znak_count = dict(sorted(znak_count.items()))

with open("hw01_output.json", "w", encoding="utf-8") as output_file:
    json.dump(znak_count, output_file, ensure_ascii=False, indent=4)
