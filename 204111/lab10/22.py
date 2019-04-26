code_table = "aceiklmr-"
text ="""
3
5 3 4 2
3 1 2 8 1 7 2 0 86
"""
### back_ blackspece
### _ spece

lst_code = list(code_table)
text_ = text.replace("\n"," back_ ")
text_sp = text_.split()
total_text_sp = len(text_sp)

for i in range (total_text_sp):
    if text_sp[i] == "back_":
        text_sp[i] = "\n"
        continue

    elif text_sp[i].isdigit():
        if int(text_sp[i]) > len(code_table):
            text_sp[i] = "_"
            continue

        text_sp[i] = lst_code[int(text_sp[i])]


text_sp = "".join(text_sp)
text_sp = text_sp.strip()

print(text_sp)
