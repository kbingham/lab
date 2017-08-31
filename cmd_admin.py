import cmd


class AdminCommands(cmd.Cmd):
    def do_adduser(self, line):
        print("Adding a new user")

    def do_upgrade(self, line):
        print("Upgrading installation")

    def default(self, line):
        return False
