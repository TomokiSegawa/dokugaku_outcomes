import re

text = "I am __age__ years old __tall__ cm and __weight__ kg, which is __evaluation__"

def mad_libs(mls):
    hints = re.findall("__.*?__",text)
    if hints is not None:
        for word in hints:
            new = input("input {}: ".format(word))
            mls = mls.replace(word,new,1)
        print(mls)
    else:
        print("input is wrong.")


mad_libs(text)
