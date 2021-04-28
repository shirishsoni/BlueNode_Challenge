from decouple import config

def summary(summary):

    text_file = open(config('SUMMARY'), "w")
    for element in summary:
        text_file.write(element + "\n")
    text_file.close()
