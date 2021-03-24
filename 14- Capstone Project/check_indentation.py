with open('/content/english_python_data.py', 'r') as f_reader:
    text = f_reader.readlines()

def white_space_counter(_string):
    count = 0
    string_list = list(_string)
    for i in range(len(string_list)):
        if string_list[i] == ' ':
            count += 1
        else:
            break
    return count

key_set = ['if', 'while', 'for','try', 'elif', 'except', 'class', 'with', 'def']

for i in range(len(text)):
    # if current line starts with if, while, for and ends with :\n, the next line should have 4 white spaces.
    if text[i].startswith(('if', 'while', 'for','try', 'elif', 'except', 'class', 'with', 'def')) and text[i][-2:] == ':\n':
        if text[i+1][:4] != '    ':        
            print(f"Wrong indentation at line: {i+1}")
            print(f"Missing {4-white_space_counter(text[i+1])} spaces.")
            # text[i+1] = ' ' * (4-white_space_counter(text[i+1])) + text[i+1]

    # if current line starts with indentation, contains either of 'for', 'if', 'while' and 
    # ends with :\n, the next line should 2 indentations.
    if text[i].startswith('    ') and any(x in text[i] for x in key_set) and text[i][-2:]==':\n':
        if text[i+1][:8] != ' ' * 8:
            print(f"Wrong indentation at line: {i+1}")
            print(f"Missing {8-white_space_counter(text[i+1])} spaces.")