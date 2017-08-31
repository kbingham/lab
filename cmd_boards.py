import cmd


class BoardCommands(cmd.Cmd):
    def do_on(self, board):
        print("switching on", board)

    def do_off(self, board):
        print("switching off", board)

    def do_reboot(self, board):
        print("rebooting ", board)

    def do_serial(self, board):
        print("Connecting to Serial...")

    def default(self, line):
        return False
