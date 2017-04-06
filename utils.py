def take_after(_list, start, end=False):
    output = []
    take = False
    for item in _list:
        if end != False:
            if item == end:
                return output

        if take:
            output.append(item)
        elif item == start:
            take = True
    return output

def destroy_substring(string, substring):
    if substring in string:
        split = string.split(substring)
        concat = ''
        for section in split:
            concat += section
        return concat
    else:
        return string

def get_bracketed_value(string):
    step1 = string.split('(', 1)[1]
    step2 = step1.split(')', 1)[0]
    return step2
