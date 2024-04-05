import re


def get_sentences(file_name: str) -> list:
    """
    get all sentences from text file that end with ., ?, ! or ...
    :param file_name: file with text
    :return: list of sentences
    """
    result = []
    with open(file_name) as file:
        for line in file:
            result += re.split(r'\. |\? |! |\.{3} ', line)
    return result


def get_count_of_sentences(sentences: list) -> int:
    """
    get the length of list of sentences
    :param sentences: list of sentences
    :return: count of sentences
    """
    return len(sentences)


def get_count_of_words(sentences: list) -> int:
    """
    go throw each sentence and split into words based on signs: ",", "space", ", ", ":", ";"
    :param sentences: list of sentences
    :return: count of words
    """
    words_count = 0
    for sentence in sentences:
        words = re.split(r', |\s|,|;|:', sentence)
        words_count += len(words)
    return words_count


def write_to_file_result(words_count: str, sentences_count: str, file_name: str) -> str:
    """
    write results about count of sentences and words into file
    :param words_count: count of words
    :param sentences_count: count of sentences
    :param file_name: file to write result
    :return: file with results
    """
    with open(file_name, "w") as file:
        lines = [f"Count of sentences: {sentences_count}\n",
                 f"Count of words: {words_count}"]
        file.writelines(lines)
    return file_name



