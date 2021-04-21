import standardDefinition   # module that reads the standard definition json
import errorCodes   # module that reads the error code json
import printReport  # module that prints Report.csv
import printSummary # module that prints Summary.txt
import unittest

definition = standardDefinition.standard()

# Function Get Error, parses the error jason object
# Takes flag, key, index, data_type, max_length as parameters
# Based on the parameters, the function returns the appropriate error code
def getErrors(flag, key, index, data_type, max_length):

    # Fetching the contents of error_codes.json
    errcode = errorCodes.error()

    """Since we have 5 different codes, we need at least 3 bits of boolean data 
     to evaluate the situation, based on the combination of True and false of the flag vales
     the error code is decided, 110 means error code 1, 010 represents error code 2 and so on"""

    if flag[0] and flag[1] and not flag[2]:
        for i in range(0, len(errcode)):
            if errcode[i]['code'] == 'E01':
                message = errcode[i]['message_template']     # Fetching the correct error msg for for the correct code
                message = message.replace("LX", key)         # Replacing the Lx in message with correct key
                message = message.replace("Y", str(index))   # Replacing letter y with correct subsection
                print(message)
                return 'E01', message

    elif not flag[0] and flag[1] and not flag[2]:
        for i in range(0, len(errcode)):
            if errcode[i]['code'] == 'E02':
                message = errcode[i]['message_template']
                message = message.replace("LX", key)
                message = message.replace("Y", str(index))
                message = message.replace("{data_type}", data_type)
                message = message.replace("{max_length}", str(max_length))
                print(message)
                return 'E02', message

    elif flag[0] and not flag[1] and not flag[2]:
        for i in range(0, len(errcode)):
            if errcode[i]['code'] == 'E03':
                message = errcode[i]['message_template']
                message = message.replace("LX", key)
                message = message.replace("Y", str(index))
                message = message.replace("{data_type}", data_type)
                message = message.replace("{max_length}", str(max_length))
                print(message)

                return 'E03', message

    elif not flag[0] and not flag[1] and not flag[2]:
        code = 'E04'
        for i in range(0, len(errcode)):
            if errcode[i]['code'] == 'E04':
                message = errcode[i]['message_template']
                message = message.replace("LX", key)
                message = message.replace("Y", str(index))
                print(message)
                return 'E04', message
    else:
        for i in range(0, len(errcode)):
            if errcode[i]['code'] == 'E05':
                message = errcode[i]['message_template']
                message = message.replace("LX", key)
                message = message.replace("Y", str(index))
                print(message)
                return 'E05', message


# This function finds the index of the key provided
# Since the standard definition has multiple dictionaries in the list
# It is essential to find its location
def getIndex(key):
    for i in range(0, len(definition)):
        if key == definition[i]["key"]:
            return i


# This is the most crucial function
# It takes the section as parameter and evaluates it
def parseSection(section, report, summary):
    definition = standardDefinition.standard()
    # print(definition)
    key = section[0]  # The first value in the section represents the key, for instance L1

    index = getIndex(key)  # Fetching the index of the key in the definition

    for i in range(0, len(definition[index]["sub_sections"])):  # Iterating through the sub-sections of the section

        # Flag/Boolean values representing different conditions with combination of true and false
        flag = [False, False, False]

        data_type = definition[index]["sub_sections"][i]["data_type"]    # Expected data type of the sub-section
        max_length = definition[index]["sub_sections"][i]["max_length"]  # Expected character length
        given_dt = 'others'       # Supposing that the given data type is others
        given_length = 0          # Supposing that the given length is 0

        # Exception handling using try and except
        try:

            # Checking if the value in given subsection is a an empty value
            if len(section[i + 1]) < 1:
                errcode, message = getErrors(flag, key, i+1, data_type, max_length) # Function call to fetch error code
                # Appending the error code and section details into the report object
                report.append(
                    [
                        key,
                        key + str(i + 1),
                        given_dt,
                        data_type,
                        given_length,
                        max_length,
                        errcode
                    ]
                )

                # Appending the error message in the summary object
                summary.append(message)
                continue

            # Checking if the given datatype is the expected data type
            if data_type == "digits":
                if section[i + 1].isdigit():
                    flag[0] = True
                    given_dt = 'digits'
                elif all(x.isalpha() or x.isspace() for x in section[i + 1]):
                    given_dt = 'word_characters'
            else:
                if all(x.isalpha() or x.isspace() for x in section[i + 1]):
                    flag[0] = True
                    given_dt = 'word_characters'
                elif section[i + 1].isdigit():
                    given_dt = 'digits'

            # Checking the length is under the max length
            given_length = len(section[i + 1])
            if given_length <= max_length:
                flag[1] = True

            # Fetching the error code based on section evaluation
            errcode, message = getErrors(flag, key, i+1, data_type, max_length)

    # Exception is raised when the given section is missing a sub-section since there would be no value at that index
        except IndexError:
            flag[2] = True
            errcode, message = getErrors(flag, key, i + 1, data_type, max_length)
            given_dt = ""
            given_length = ""

        # Appending the error code and section details into the report object
        report.append(
            [
                key,
                key+str(i+1),
                given_dt,
                data_type,
                given_length,
                max_length,
                errcode
            ]
        )

        # Appending the error message in the summary object
        summary.append(message)


# Main function to call the parse function
def main():

    f = open("input_file.txt", "r")

    # Declaring base objects to store the results
    report = [['Section', 'Sub-Section', 'Given DataType', 'Expected DataType', 'Given Length', 'Expected MaxLength',
               'Error Code']]

    summary = []

    # Reading from input file and splitting the text by & symbol since it represents the beginning
    for line in f:
        line = line.strip()
        sections = line.split("&")
        print(sections)  # Printing just for manual testing
        parseSection(sections, report, summary)   # Sending, sections to be parsed

    # Printing Report and summary
    printReport.report(report)
    printSummary.summary(summary)

    print("\nTesting through unit test \n")


class TestErrorCode(unittest.TestCase):

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


if __name__ == '__main__':
    main()
    unittest.main()
