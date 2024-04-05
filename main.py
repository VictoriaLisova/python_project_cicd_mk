from data_analysis import get_sentences, get_count_of_sentences, get_count_of_words, write_to_file_result

def main():
    sentences_list = get_sentences("text.txt")
    sentences_count = get_count_of_sentences(sentences_list)
    print(sentences_count)
    words_count = get_count_of_words(sentences_list)
    print(words_count)
    write_to_file_result(words_count, sentences_count, "result.txt")


if __name__ == '__main__':
    main()
