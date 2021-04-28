import unittest
from Main import getIndex, getErrors, parseSection, main


class TestCode(unittest.TestCase):

    def test_code_1(self):
        flag = [True, True, False]
        error_code, message = getErrors(flag, "L1", 1, "digits", 3)
        assert error_code == "E01"
        print("Test error code 1 successful\n")

    def test_code_2(self):
        flag = [False, True, False]
        error_code, message = getErrors(flag, "L1", 1, "digits", 3)
        assert error_code == "E02"
        print("Test error code 2 successful\n")

    def test_code_3(self):
        flag = [True, False, False]
        error_code, message = getErrors(flag, "L1", 1, "digits", 3)
        assert error_code == "E03"
        print("Test error code 3 successful\n")

    def test_code_4(self):
        flag = [False, False, False]
        error_code, message = getErrors(flag, "L1", 1, "digits", 3)
        assert error_code == "E04"
        print("Test error code 4 successful\n")

    def test_code_5(self):
        flag = [False, False, True]
        error_code, message = getErrors(flag, "L1", 1, "digits", 3)
        assert error_code == "E05"
        print("Test error code 5 successful\n")

    def test_index_1(self):
        index = getIndex('L1')
        assert index == 0
        print("Test index 1 successful\n")

    def test_index_2(self):
        index = getIndex('L2')
        assert index == 1
        print("Test index 2 successful\n")

    def test_index_3(self):
        index = getIndex('L3')
        assert index == 2
        print("Test index 3 successful\n")

    def test_index_4(self):
        index = getIndex('L4' )
        assert index == 3
        print("Test index 4 successful\n")

    def test_parser1(self):
        section = ['L1', '99', '', 'A']
        report = [
            ['Section', 'Sub-Section', 'Given DataType', 'Expected DataType', 'Given Length', 'Expected MaxLength',
             'Error Code']]

        summary = []
        parseSection(section, report, summary)
        assert report[1][0] == "L1"
        assert report[1][1] == "L11"
        assert report[1][6] == "E03"

        assert report[2][0] == "L1"
        assert report[2][1] == "L12"
        assert report[2][6] == "E04"

        assert report[3][0] == "L1"
        assert report[3][1] == "L13"
        assert report[3][6] == "E01"



