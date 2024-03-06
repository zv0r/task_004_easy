from subprocess import run, PIPE
import os
import pytest

B_FILE_PATH = './bin/string_sort'

def test_bin_folder_contains_string_sort():
    assert os.path.isfile(B_FILE_PATH)

def test_string_sort_not_correct_input_1():
    result = run([B_FILE_PATH], input='asdwe1', encoding='utf-8', stderr=PIPE, stdout=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_string_sort_not_correct_input_2():
    result = run([B_FILE_PATH], input='123', encoding='utf-8', stderr=PIPE, stdout=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_string_sort_not_correct_input_3():
    result = run([B_FILE_PATH], input='man.women', encoding='utf-8', stderr=PIPE, stdout=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_string_sort_not_correct_input_4():
    result = run([B_FILE_PATH], input='ABCDREW', encoding='utf-8', stderr=PIPE, stdout=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_string_sort_correct_input_1():
    result = run([B_FILE_PATH], input='abc 2', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == 'cba'

def test_string_sort_correct_input_2():
    result = run([B_FILE_PATH], input='cba 1', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == 'abc'

def test_string_sort_correct_input_3():
    result = run([B_FILE_PATH], input='peeredu 1', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == 'deeepru'

def test_string_sort_correct_input_4():
    result = run([B_FILE_PATH], input='deeepru 2', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == 'urpeeed'

def test_string_sort_correct_input_5():
    result = run([B_FILE_PATH], input='abrakadbra 1', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == 'aaaabbdkrr'

if __name__ == '__main__':
    pytest.main()
