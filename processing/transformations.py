import re

def remove_specials(text):
    if isinstance(text, str):
        return re.sub(r'[\(\)]', '', text)
    return text
def remove_double_spaces(text):
    if isinstance(text, str):
        return re.sub(r'\s+', ' ', text).strip()
    return text

def sanitize(text):
    cleaned_text = remove_specials(text)
    cleaned_text = remove_double_spaces(cleaned_text)

    if isinstance(cleaned_text, float):
        return cleaned_text
    else:
        return [item.strip() for item in cleaned_text.split(",")]