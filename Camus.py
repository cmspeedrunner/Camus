replacements_dict = {
    "openbracket": "(",
    "closebracket": ")",
    "string": '\"',
    "plus": "+",
    "minus": "-",
    "divide": "/",
    "times": "*",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
    "comma": ",",
    "emark": "!",
    "qmark": "?",
    "equal": "=",
    " ": "",
    "wspace": " ",
    "commenthere": "#",
    "point": ".",
    "bslash": "\\",
    "fslash": "/",
    "hashtag": "#",
    "dollarsymbol": "$",
    "poundsymbol": "£",
    

}  # Dictionary of replacements

def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

fl = input("Enter name of Camus File to run: ")
with open(fl, "r") as f:  # Open file for reading
    file_contents = f.read()  # Read file contents
    for old_val, new_val in replacements_dict.items():
        file_contents = file_contents.replace(old_val, new_val)  # Replace all occurrences of old value with new value
        splittin = file_contents.splitlines()

def anal():
    try:
        if "(" in line:
            idx = line.split("(")[0]
    
            if idx == "display":
                print(eval(find_between(line, "(", ")")))
            if idx == "variableset":
                contentfeild = find_between(line, "(",")")
                varname = contentfeild.split(",")[0]
                vardata = contentfeild.split(",")[1]
                globals()[varname] = eval(vardata)
            if idx == "classof":
                varname = find_between(line, "(",")")
                print(type(globals()[varname]))
            if idx == "converttostr":
                actual = (find_between(line,"(",")"))
                globals()[actual] = str(globals()[actual])
            if idx == "converttoint":
                actual = (find_between(line,"(",")"))
                globals()[actual] = int(globals()[actual])
            if idx == "converttoflt":
                actual = (find_between(line,"(",")"))
                globals()[actual] = float(globals()[actual])
            if idx == "converttobool":
                actual = (find_between(line,"(",")"))
                globals()[actual] = bool(globals()[actual])
        if line == "":
            pass
    except SyntaxError as e:
        print("\033[1;31mCaught Syntax Error\033[0m")
        print("")
        print("\033[1;31mFile: "+fl+"\033[0m")
        print("\033[1;31m     "+"^"*len(fl)+"\033[0m")
        print("\033[1;31m"+e.msg+"\033[0m")
        print("\033[1;31mLN:"+str(e.lineno)+"\nCOL:"+str(e.offset)+"\033[0m")
        print("\033[1;35;3mHelp, Your code has a "+e.msg+"\nYour code that is causing this issue is '"+str(e.args[1])+"'\033[0m")
        print("\033[1;35;3m                                         "+"^"*len(str(e.args[1]))+"\033[0m")
for i, line in enumerate(splittin):
    anal()