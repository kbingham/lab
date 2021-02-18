import cmd
import os

power = "energenie-power"
serial = "serial"

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

    def default(self, line):
        return False
