import re

def hardSurname(s):
    c = re.findall(r'[^aeiouAEIOU]+', s)

    return max([len(x) for x in c], default = 0)