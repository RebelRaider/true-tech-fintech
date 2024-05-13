import re


def extract_mobile_number(text):
    cleaned_text = re.sub(r"[^\d+]", "", text)

    mobile_number_match = re.search(r"(\+?\d{10,12})", cleaned_text)

    if mobile_number_match:
        return mobile_number_match.group()
    else:
        return None


def extract_account_number(text):
    cleaned_text = re.sub(r"\D", "", text)

    account_number_match = re.search(r"\d{10,}", cleaned_text)

    if account_number_match:
        return account_number_match.group()
    else:
        return None
