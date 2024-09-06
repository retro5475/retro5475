import random

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

random_quote = random.choice(quotes).strip()

with open("README.md", "r") as readme_file:
    lines = readme_file.readlines()

with open("README.md", "w") as readme_file:
    inside_quote_section = False
    for line in lines:
        if "<!-- Zitat Bereich -->" in line:
            inside_quote_section = True
            readme_file.write(f"> {random_quote}\n")
        elif inside_quote_section and line.strip() == "":
            inside_quote_section = False
            readme_file.write(line)
        else:
            readme_file.write(line)
