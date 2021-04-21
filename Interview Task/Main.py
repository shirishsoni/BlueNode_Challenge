import standardDefinition
import errorCodes
import printReport
import printSummary


# flag, key, index, data_type, max_length
def getErrors(flag, key, index, data_type, max_length):
    errcode = errorCodes.error()

    if flag[0] and flag[1] and not flag[2]:
        for i in range(0, len(errcode)):
            if errcode[i]['code'] == 'E01':
                message = errcode[i]['message_template']
                message = message.replace("LX", key)
                message = message.replace("Y", str(index))
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


def getIndex(key, definition):
    for i in range(0, len(definition)):
        if key == definition[i]["key"]:
            return i


def parseSection(section,report, summary):
    definition = standardDefinition.standard()
    # print(definition)
    key = section[0]


    index = getIndex(key, definition)

    for i in range(0, len(definition[index]["sub_sections"])):

        flag = [False, False, False]

        data_type = definition[index]["sub_sections"][i]["data_type"]
        max_length = definition[index]["sub_sections"][i]["max_length"]
        given_dt = 'others'
        given_length = 0

        try:

            if len(section[i + 1]) < 1:
                errcode, message = getErrors(flag, key, i+1, data_type, max_length)
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
                summary.append(message)
                continue

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

            given_length = len(section[i + 1])
            if given_length <= max_length:
                flag[1] = True

            errcode, message = getErrors(flag, key, i+1, data_type, max_length)

        except IndexError:
            flag[2] = True
            errcode, message = getErrors(flag, key, i + 1, data_type, max_length)
            given_dt = ""
            given_length = ""
            # print("%s%d field under segment %s is missing" % (key, i + 1, key))

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

        summary.append(message)

def main():
    f = open("input_file.txt", "r")
    report = [['Section', 'Sub-Section', 'Given DataType', 'Expected DataType', 'Given Length', 'Expected MaxLength',
               'Error Code']]
    summary = []
    for line in f:
        line = line.strip()
        sections = line.split("&")
        print(sections)
        parseSection(sections,report,summary)

    printReport.report(report)
    printSummary.summary(summary)


if __name__ == '__main__':
    main()
