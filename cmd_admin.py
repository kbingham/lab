import cmd
import os


class AdminCommands(cmd.Cmd):
    def do_adduser(self, line):
        print("Adding a new user")

    def do_upgrade(self, line):
        print("Upgrading installation")
        os.system("git fetch && git reset --hard origin/master")

    def do_logs(self, line):
        os.system("tail -f lab.log")

    def default(self, line):
        return False
