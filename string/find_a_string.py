def count_substring(string,sub_string):
    # for sub_string in string:
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count +=1
    return count

print(count_substring('I am an Indian by birth','am'))
