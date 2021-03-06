import cmd
from users import User


class UserCommands(cmd.Cmd):
    def do_whoami(self, line):
        print("You are user", User().name())

    def do_hello(self, line):
        print("Hello there %s" % line)

    def do_ls(self, line):
        print("ls files")

    def do_scp(self, line):
        print("SCP instance %s" % line)

    def default(self, line):
        return False
