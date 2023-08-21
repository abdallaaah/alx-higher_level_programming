#!/usr/bin/python3
def multiple_returns(sentence):
    sentencee = None
    if sentence:
        sentencee = sentence[0]
    return len(sentence), sentencee
