
def summary(summary):

    text_file = open("Summary.txt", "w")
    for element in summary:
        text_file.write(element + "\n")
    text_file.close()
