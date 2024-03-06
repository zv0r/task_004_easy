from subprocess import run, PIPE
import os
import pytest

B_FILE_PATH = './bin/figure_sort'

def test_bin_folder_contains_figure_sort():
    assert os.path.isfile(B_FILE_PATH)

def test_figure_sort_not_correct_input_1():
    result = run([B_FILE_PATH], input='1 2 3 2 1 abc 3 4 7', encoding='utf-8', stderr=PIPE, stdout=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_figure_sort_not_correct_input_2():
    result = run([B_FILE_PATH], input='1.0 2 3 2 3 32', encoding='utf-8', stderr=PIPE, stdout=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_figure_sort_not_correct_input_3():
    result = run([B_FILE_PATH], input='1 -1 2 2 3 -4', encoding='utf-8', stderr=PIPE, stdout=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_figure_sort_not_correct_input_4():
    result = run([B_FILE_PATH], input='1 0 0 2 3 0', encoding='utf-8', stderr=PIPE, stdout=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_figure_sort_correct_input_1():
    result = run([B_FILE_PATH], input='1 2 3 2 1 2 3 4 7', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '2 2\n1 6\n3 28'

def test_figure_sort_correct_input_2():
    result = run([B_FILE_PATH], input='1 5 5 2 4 4 3 1 1', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '3 1\n2 16\n1 25'

def test_figure_sort_correct_input_3():
    result = run([B_FILE_PATH], input='1 1 1 2 2 2', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '1 1\n2 4'

def test_figure_sort_correct_input_4():
    result = run([B_FILE_PATH], input='1 3 9 2 6 7 3 8 11 4 5 1 5 9 8', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert result.stdout == '4 5\n1 27\n2 42\n5 72\n3 88'

if __name__ == '__main__':
    pytest.main()
