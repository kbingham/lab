#!/usr/bin/env python3


class User(object):
    def __init__(self, username):
        self.name = username

    def isAdmin(self):
        if self.name == "admin":
            return True

        return False
