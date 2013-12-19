#!/usr/bin/env python
# Copyright 2013 paul.whipp@gmail.com
# Do what you like with it though ;)
import os
import pickle

from animal_game.ask import ask


def play_games():
    tree_root = load_tree()
    question = 'Would you like to play the animal game?'
    while ask(question):
        play_game(tree_root)
        question = 'Would you like to play again?'
    print('ok then, bye!')
    save_tree(tree_root)


def play_game(tree):
    if 'animal' in tree:  # Make the guess
        print('You are thinking of a {0}.'.format(tree['animal']))
        if ask('Am I right?'):
            print("I've won!")
        else:
            if ask('Oh dear, can you help me do better?'):
                learn(tree)
    else:  # Ask the question and continue
        if ask(tree['question']):
            play_game(tree['yes'])
        else:
            play_game(tree['no'])


def learn(tree):
    animal = raw_input('What animal were you thinking of? ')
    question = raw_input('What yes/no question will tell between a {0} and a {1}? '.format(
        animal, tree['animal']))
    tree['question'] = question
    if ask('If you are thinking of a {0}, and I ask you "{1}", what would you answer?'.format(
            animal, question)):
        tree['yes'] = dict(animal=animal)
        tree['no'] = dict(animal=tree['animal'])
    else:
        tree['yes'] = dict(animal=tree['animal'])
        tree['no'] = dict(animal=animal)
    del (tree['animal'])


kb_file = 'animal_knowledge.pickle'


def load_tree():
    try:
        with open(kb_file, 'rb') as f:
            tree = pickle.load(f)
        print('Loaded "{0}"'.format(kb_file))
        return tree
    except IOError:
        print('Could not load "{0}", using default animal knowledge'.format(kb_file))
        return {'question': 'Does it have a long neck?',
                'yes': {'animal': 'giraffe'},
                'no': {'animal': 'sheep'}}


def save_tree(tree):
    try:
        with open(kb_file, 'wb') as f:
            pickle.dump(tree, f)
        print('Saved "{0}"'.format(kb_file))
    except:
        print('Could not save "{0}".'.format(kb_file))
        raise


if __name__ == "__main__":
    play_games()
