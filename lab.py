#!/usr/bin/env python3

import os
import sys
from users import User
from cmd_boards import BoardCommands
from cmd_commands import UserCommands
from cmd_admin import AdminCommands
from logger import log

command = os.environ.get('SSH_ORIGINAL_COMMAND')

# As per the SSH authorized_keys authentication, the user is provided
# by the first argument only. No additional command line parsing is
# required.
user = User(sys.argv[1])

if user is None:
    print("Failed to authenticate user")
    exit()

if command is None:
    if User().isAdmin():
        print("Ok just this once... Admin")
        os.system("bash -l")
        exit()
    else:
        print("This utility must be run as an SSH agent")
        exit()

if "LAB_DEBUG=1" in command:
    print(command)
    print(user.name)
    print(user.isAdmin())

command_args = command.split()
if len(command_args) < 1:
    print("No commands provided")
    command = "help"
    command_args = command.split()

# Log commands
log(user.name, command)

# First identify any board commands
completed = BoardCommands().onecmd(command)
if completed is not False:
    exit()

# Fall back to 'system commands'
completed = UserCommands().onecmd(command)
if completed is not False:
    # A command was handled
    exit()

# Only allow 'admin' commands below this point
if not user.isAdmin():
    print("I couldn't handle:", command)
    exit()

# Handle administrator commands
completed = AdminCommands().onecmd(command)
if completed is False:
    print("I couldn't handle:", command)
