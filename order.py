import re


def order(sentence):
    t = sentence.split();
    l = {}
    for n in t:
        l[n] = int(re.findall(r'\d+', n)[0])

    l = dict(sorted(l.items(), key=lambda item: item[1]))

    return ' '.join(l)
