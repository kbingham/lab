import cmd
import fnmatch
import os

power = "energenie-power"
serial = "serial"

dirs = [
    "tftp",
    "nfs",
]

boards = [
    "eagle-v3m",
    "falcon-v3u",
    "salvator-x",
    "salvator-xs",
]

def paths(pattern="*"):
    for d in dirs:
        for b in boards:
            yield "/" + d + "/" + b

class BoardCommands(cmd.Cmd):
    def do_on(self, board):
        print("switching on", board)
        os.system(power + " " + board + " on")

    def do_off(self, board):
        print("switching off", board)
        os.system(power + " " + board + " off")

    def do_reboot(self, board):
        print("rebooting ", board)
        os.system(power + " " + board + " reboot")

    def do_serial(self, board):
        print("Connecting to Serial...")
        os.system(serial + " " + board)

    def do_pwd(self, cmd):
        print("/")

    def do_command(self, args):
        args = args.split()

        if args[0] != "ls":
            print("Not LS?")
            return False

        if args[-1] == "/*":
            print("\n".join(paths()))
        else:
            matches = fnmatch.filter(paths(), args[-1])
            print("\n".join(matches))


    def default(self, line):
        return False
