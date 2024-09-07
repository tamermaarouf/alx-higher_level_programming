#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 1:
        return None
    new_tuble = ()
    count = 0
    for ch in sentence:
        count += 1
    new_tuble = count, sentence[0]
    return (new_tuble)
