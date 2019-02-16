#!/usr/bin/env python

def hello(g='Hello'):
    print('{} from {} @ {} [{}]'.format(g,__name__,__package__,__file__))

hello(g='Importing')

def func():
    hello(g='Calling')

if __name__ == '__main__':
    func()
