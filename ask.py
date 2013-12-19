#!/usr/bin/env python
# Copyright 2013 paul.whipp@gmail.com
# Do what you like with it though ;)


def ask(question,
        responses={'yes': True,
                   'y': True,
                   'ye': True,
                   'n': False,
                   'no': False},
        retries=3):
    """ask question and return match in responses"""

    # Add a space at the end of question if absent
    if question[-1] != ' ':
        question += ' '

    answer = raw_input(question).lower()

    try:
        return responses[answer]
    except KeyError:
        print('Your answer must be one of {0}'.format(responses.keys()))
        if retries > 0:
            return ask(question, responses, retries - 1)
        else:
            raise
