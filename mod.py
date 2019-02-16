__package__ = 'lolwut'
__name__ = 'lolwut.mod'

def hello(g='Hello'):
    print('{} from {} @ {} [{}]'.format(g,__name__,__package__,__file__))

hello(g='Importing')

def func():
    hello(g='Calling')
