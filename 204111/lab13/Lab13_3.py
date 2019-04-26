import string

def main():
    text = "###d?he### is not Dog D^og dog"
    print(word_count(text))


def word_count(text):
    lst_text = text.split()


    ## strip on original list ##
    for i in range(len(lst_text)):
        lst_text[i] = lst_text[i].strip(string.punctuation)
        lst_text[i] = lst_text[i].lower()


    ## create dict ##
    dic_ = dict()
    for text_ in lst_text:
        if text_ in dic_:
            dic_[text_] += 1
        else:
            dic_[text_] = 1
    return dic_


if __name__ == '__main__':
    main()