#!/usr/bin/env python3

import os
import sys
from users import User
from boards import Board
from cmd_commands import UserCommands

command = os.environ.get('SSH_ORIGINAL_COMMAND')
if command is None:
    print("This utility must be run as an SSH agent")
    exit()

# As per the SSH authorized_keys authentication, the user is provided
# by the first argument only. No additional command line parsing is
# required.
user = User(sys.argv[1])

if user is None:
    print("Failed to authenticate user")
    exit()

if "LAB_DEBUG=1" in command:
    print(command)
    print(user.name)
    print(user.isAdmin())

command_args = command.split()
if len(command_args) < 1:
    print("No commands provided")
    exit()

# First identify any board commands
board = Board(command_args[0])
if board is not None:
    board.execute(command_args)
    exit()

# Fall back to 'system commands'
UserCommands().onecmd(command)

# Only allow 'admin' commands below this point
if not user.isAdmin():
    exit()
