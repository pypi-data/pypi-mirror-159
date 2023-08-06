from genericpath import exists
from src.mufid.do_nothing import f as do_nothing
from os.path import exists
from os import mkdir

def f(path) : [mkdir(path) if not exists(path) else do_nothing(), path][1]
