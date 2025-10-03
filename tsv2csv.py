import re

with open("hurtlex_IT.tsv", "r", encoding = "utf-8") as tsv_file:
    with open("hurtlex_IT.csv", "w", encoding = "utf-8") as csv_file:
        for line in tsv_file:
            line_content = re.sub('\t', ',', line)
            csv_file.write(line_content)