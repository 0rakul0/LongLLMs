import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,;:()\-]', '', text)
    text = re.sub(r'\s([?.!,;:](?:\s|$))', r'\1', text)
    return text

with open("../data/cpc_2015.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

cleaned_text = clean_text(raw_text)

with open("../data/cpc_2015_cleaned.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)
