import re


def get_sentences(file_name: str) -> list:
    result = []
    with open(file_name) as file:
        for line in file:
            result += re.split(r'\. |\? |! |\.{3} ', line)
    return result


def get_count_of_sentences(sentences: list) -> int:
    return len(sentences)

sentences_list = get_sentences("text.txt")
print(get_count_of_sentences(sentences_list))

