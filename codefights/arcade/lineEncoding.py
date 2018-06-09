def lineEncoding(s):
    split_list = []
    temp_string = s[0]

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            temp_string += s[i]
        else:
            split_list.append(temp_string)
            temp_string = s[i]

    # for the last element
    split_list.append(temp_string)

    line_encoding = ''

    for i in range(len(split_list)):
        line_encoding += str(split_list[i].count(split_list[i][0])) if split_list[i].count(split_list[i][0]) > 1 else ''
        line_encoding += split_list[i][0]
    
    return line_encoding