# BlueNode_Challenge

This repository consists of the solution developed by Shirish Soni for the coding test requested by Blue Node.
The test and solution, both, mainly focuses on efficient programming and correct outcome.

The test has 3 crucial parts:
1) standard_definition.json: contains the rules and definitions for evaluating the input
2) error_code.json: contains the set of desired outputs
3) input_file.txt: This file contains the test cases provided by Blue Node

The solution has 4 crucial parts:
1) standardDefinition.py: code to read from standard_definition.json
2) errorCodes.py: code to read from error_codes.json
3) Main.py: This file contains the major processing and decision making code
4) UnitTest.py: Contains custom test case designed to test each unit independently 

Description of Main.py

The crucial tasks of the solution included parsing the standard_definition rules and evaluating the input based on that.
Once the evaluation is done, based on that the error code is decided. The final output is displayed, added to Report.csv and Summary.txt.

Before testing the code for the inputs from the input_file.txt, it was crucial to individually test the functions.
There are 3 functions that play major role, parseSection(section, report, summary), getIndex(key), getErrors(flag, key, index, data_type, max_length).
Therefore test cases were defined for each of those and tested. Once the test cases proved to be successful, the code read from the input file and produced 
the output for each input.

Main Logic:

Sample input: L1&99&.&A
This input is to be divided into subsection, the first section would be from the beginning of the string till the first ampersand(&).
The remaining subsection begin with &. Therefore , the sample gets divided into 4 subsections : {'L1' , '99' , '.' , 'A'}

Once sub-sections are obtained, they are evaluated by the standard definitions, if they fall into the conditions a flag is set to true.
Depending on how many flags are set to true for each subsection, the error code for it is decided.

The final output can be found on the user terminal or Report.csv or Summary.txt.
However, Report.csv has the most detailed output.
