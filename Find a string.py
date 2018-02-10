def count_substring(string, sub_string):
    kol = 0
    for i in range(0, len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            kol = kol + 1
    return kol