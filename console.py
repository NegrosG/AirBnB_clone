#!/usr/bin/python3
"""Defining the HBNB comsole"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defining the hbnb command prompt"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """defining the quit function
        to exit the console"""

        return True

    def help_quit(self, arg):
        """initializing the help function
        of the console"""

        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Defining the End of life function
        for the console"""

        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
