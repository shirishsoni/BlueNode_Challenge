import standardDefinition
import errorCodes
import printReport


# flag, key, index, data_type, max_length
def getErrors(flag, key, index, data_type, max_length):
    errcode = errorCodes.error()


    if flag[0] and flag[1]:
        for i in range(0, len(errcode)):
            if errcode[i]['code'] == 'E01':
                message = errcode[i]['message_template']
                message = message.replace("LX", key)
                message = message.replace("Y", str(index))
                print(message)
                return 'E01', message

    elif not flag[0] and flag[1]:
        for i in range(0, len(errcode)):
            if errcode[i]['code'] == 'E02':
                message = errcode[i]['message_template']
                message = message.replace("LX", key)
                message = message.replace("Y", str(index))
                message = message.replace("{data_type}", data_type)
                message = message.replace("{max_length}", str(max_length))
                print(message)
                return 'E02', message

    elif flag[0] and not flag[1]:
        for i in range(0, len(errcode)):
            if errcode[i]['code'] == 'E03':
                message = errcode[i]['message_template']
                message = message.replace("LX", key)
                message = message.replace("Y", str(index))
                message = message.replace("{data_type}", data_type)
                message = message.replace("{max_length}", str(max_length))
                print(message)

                return 'E03', message

    else:
        code = 'E04'
        for i in range(0, len(errcode)):
            if errcode[i]['code'] == 'E04':
                message = errcode[i]['message_template']
                message = message.replace("LX", key)
                message = message.replace("Y", str(index))
                print(message)
                return 'E04', message


def getIndex(key, definition):
    for i in range(0, len(definition)):
        if key == definition[i]["key"]:
            return i


def parseSection(section):
    definition = standardDefinition.standard()
    # print(definition)
    key = section[0]
    report = [['Section', 'Sub-Section', 'Given DataType', 'Expected DataType', 'Given Length', 'Expected MaxLength', 'Error Code']]
    summary = []

    index = getIndex(key, definition)

    for i in range(0, len(definition[index]["sub_sections"])):

        flag = [False, False]

        data_type = definition[index]["sub_sections"][i]["data_type"]
        max_length = definition[index]["sub_sections"][i]["max_length"]
        given_dt = ''
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
                continue

            if data_type == "digits":
                if section[i + 1].isdigit():
                    flag[0] = True
                    given_dt = 'digits'
            else:
                if all(x.isalpha() or x.isspace() for x in section[i + 1]):
                    flag[0] = True
                    given_dt = 'word_characters'

            given_length = len(section[i + 1])
            if given_length <= max_length:
                flag[1] = True


            errcode, message = getErrors(flag, key, i+1, data_type, max_length)
            # if errcode == 'E01':
            #     message = message.replace("LX", key)
            #     message = message.replace("Y", str(i+1))

            #print(message)
            # if flag[0] and flag[1]:
            #     #errcode, message = getErrors(flag)
            #     #printError(key, i + 1, errcode)
            #     # print("%s%d field under segment %s passes all the validation criteria." % (key, i + 1, key))
            #
            # elif not flag[0] and flag[1]:
            #     print("%s%d field under section %s fails the data type (expected: %s) validation, "
            #           "however it passes the max length (%d) validation" % (key, i + 1, key, data_type, max_length))
            #
            # elif flag[0] and not flag[1]:
            #     print("%s%d field under section %s fails the max length (expected: %d) validation, "
            #           "however it passes the data type (%s) validation" % (key, i + 1, key, max_length, data_type))
            #
            # else:
            #     print("%s%d field under section %s fails all the validation criteria." % (key, i + 1, key))

        except IndexError:
            print("%s%d field under segment %s is missing" % (key, i + 1, key))

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
        print(report)
    printReport.report(report)

def main():
    f = open("input_file.txt", "r")
    for line in f:
        line = line.strip()
        sections = line.split("&")
        print(sections)
        parseSection(sections)


if __name__ == '__main__':
    main()
