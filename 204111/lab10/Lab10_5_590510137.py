def main():
    code_table = str(input())
    text = str(input())
    decode(code_table,text)

def decode(code_table,text):

    ### @ blackspece
    ### _ spece

    code_table = code_table.strip()
    ## create a list of code_table ##
    lst_code = list(code_table)
    ## place + instead of \n  ##
    text_ = text.replace("\n"," @ ")
    text_sp = text_.split()
    total_text_sp = len(text_sp)
    ## compare between to list of text_ and list of code_table ###
    for i in range (total_text_sp):
        ## convert a "+" to \n ###
        if text_sp[i] == "@":
            text_sp[i] = "\n"
            continue
        ## check a digit ##
        elif text_sp[i].isdigit():
            ## check not more total of code table ##
            if int(text_sp[i]) >= len(code_table):
                text_sp[i] = "_"
                continue
            ## relative od list of text and list of code table ##
            text_sp[i] = lst_code[int(text_sp[i])]
        else:
            text_sp[i] = "_"
            continue

    ## convert a str ##
    text_sp = "".join(text_sp)
    ## cut head and tail down ##
    text_sp = text_sp.strip()

    print(text_sp)

if __name__ == '__main__':
    main()
