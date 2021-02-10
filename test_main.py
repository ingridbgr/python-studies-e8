from main import *


def test_list_comprehension_exercise_1():

    result = list_comprehension_exercise_1()
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert result == expected



def test_list_comprehension_exercise_2():

    result = list_comprehension_exercise_2()
    expected = [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21] 

    assert result == expected


def test_list_comprehension_exercise_3():

    result = list_comprehension_exercise_3()
    expected = [-3, -1, 1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31]

    assert result == expected



def test_list_comprehension_exercise_4():

    result = list_comprehension_exercise_4()
    expected = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    assert result == expected