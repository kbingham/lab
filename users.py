#!/usr/bin/env python3

#
# User definition singleton module
#


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class User(object):
    def __init__(self):
        self.__name = None

    def login(self, username):
        if self.__name is None:
            self.__name = username
        else:
            print("Fatal: Tried to login multiple times")
            exit()

    def name(self):
        return self.__name

    def isAdmin(self):
        if self.__name == "admin":
            return True

        return False
