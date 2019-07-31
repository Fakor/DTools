import tkinter as tk


class MainProgram(tk.Frame):

    def __init__(self, parent, config, width, height, output):
        tk.Frame.__init__(self, parent, width=width, height=height)
        self.config = config
        self.output = output

        self.command_index = 0
        self.commands = []

    def undo(self, it=1):
        for i in range(it):
            self.command_index = self.command_index - 1
            self.commands[self.command_index].undo()

    def redo(self, it=1):
        for i in range(it):
            if self.command_index >= len(self.commands):
                break
            self.commands[self.command_index].do()
            self.command_index = self.command_index + 1

    def add_command(self, command):
        self.commands.append(command)
        command.do()
        self.output.print_command(command)