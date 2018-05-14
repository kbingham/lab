import cmd
from users import User


class UserCommands(cmd.Cmd):
    def do_whoami(self, line):
        print("You're user", User().name())

    def do_hello(self, line):
        print("Hello there %s" % line)

    def do_ls(self, line):
        print("ls files")

    def do_scp(self, line):
        print("SCP instance")

    def default(self, line):
        return False
