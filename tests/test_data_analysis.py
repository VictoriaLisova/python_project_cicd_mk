import pytest
from data_analysis import get_sentences, get_count_of_sentences, get_count_of_words, write_to_file_result


def test_get_sentences(get_tmp_file):
    actual_sentences = get_sentences(get_tmp_file)
    expected = ["The sun, rose slowly over the horizon, casting a warm golden glow across the land",
                "Birds chirped:happily in the trees, welcoming the new day,with their cheerful;songs",
                "The sun, rose slowly over the horizon, casting a warm golden glow across the land",
                "The sun, rose slowly over the horizon, casting a warm golden glow across the land"]
    assert len(actual_sentences) == len(expected)
    assert [actual_sentences[i] == expected[i] for i in range(len(expected))]


def test_get_count_of_sentences(get_tmp_file):
    sentences = get_sentences(get_tmp_file)
    actual_count = get_count_of_sentences(sentences)
    assert actual_count == 4


@pytest.mark.parametrize("line, expected", [
    (["The sun, rose slowly over the horizon, casting a warm golden glow across the land"], 15),
    (["Birds chirped:happily in the trees, welcoming the new day,with their cheerful;songs"], 14),
    (["People bustled about their daily chores, the sound of laughter and conversation filling the air"], 15)
])
def test_get_count_of_words(line, expected):
    assert get_count_of_words(line) == expected


def test_write_to_file_result(get_tmp_file_to_result):
    count_of_sentences = 10
    count_of_words = 109
    expected_result = f"Count of sentences: {count_of_sentences}\nCount of words: {count_of_words}"
    file_result = write_to_file_result(count_of_words, count_of_sentences, get_tmp_file_to_result)
    actual = ""
    with open(file_result) as file:
        for line in file:
            line = line.strip().split()
            actual += " ".join(line)+"\n"
    actual = actual.strip("\n")
    assert expected_result == actual