def swap_case(s):
    modify_chars = []
    for letter in s:
        if letter.isupper():
            modify_chars.append(letter.lower())
        else:
            modify_chars.append(letter.upper())
    return ''.join(modify_chars)
    

if __name__ == '__main__':
    string = input()
    new_string = swap_case(string)
    print(new_string)