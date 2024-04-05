import pytest
import os


@pytest.fixture
def get_tmp_file(tmp_path):
    tmp_file = os.path.join(tmp_path, "text.txt")
    with open(tmp_file, "w") as file:
        text = ["The sun, rose slowly over the horizon, casting a warm golden glow across the land... Birds chirped:happily in the trees, welcoming the new day,with their cheerful;songs. The sun, rose slowly over the horizon, casting a warm golden glow across the land? The sun, rose slowly over the horizon, casting a warm golden glow across the land!"]
        file.writelines(text)
    return tmp_file


@pytest.fixture
def get_tmp_file_to_result(tmp_path):
    tmp_file = os.path.join(tmp_path, "result.txt")
    return tmp_file