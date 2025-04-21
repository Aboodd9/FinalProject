import re

def sanitize_input(input_string):
    """Very basic RegEx input sanitization"""
    pattern = r"^[a-zA-Z0-9 _.-]+$"
    return bool(re.match(pattern, input_string))
