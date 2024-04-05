import re


def get_sentences(file_name: str) -> list:
    result = []
    with open(file_name) as file:
        for line in file:
            result += re.split(r'\. |\? |! |\.{3} ', line)
    return result


