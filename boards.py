#!/usr/bin/env python3


class Board(object):
    def __new__(self, boardname):
        # Verify this is a valid board
        print("Looking for board %s" % boardname)
        return None

    def __init__(self, boardname):
        self.name = boardname
