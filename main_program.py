import tkinter as tk


class MainProgram(tk.Frame):

    def __init__(self, parent, config, width, height):
        tk.Frame.__init__(self, parent, width=width, height=height)
        self.config = config

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
            self.commands[self.command_index].run()
            self.command_index = self.command_index + 1

    def add_command(self, command, *args, **kwargs):
        self.commands.append(command(self, *args, **kwargs))