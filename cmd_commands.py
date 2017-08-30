import cmd


class UserCommands(cmd.Cmd):
    def do_hello(self, line):
        print("Hello there %s" % line)

    def do_ls(self, line):
        print("ls files")

    def do_scp(self, line):
        print("SCP instance")

    def default(self, line):
        return False
