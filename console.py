"""Console module

This module contains the HBNBCommand class which extends cmd.Cmd to create a simple command-line interface.
"""
#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class extends cmd.Cmd to create a simple command-line interface.
    """

    prompt = "(hbnb)"  # Sets the prompt for the command line interface

    def emptyline(self):
        """
        Overrides emptyline method from cmd.Cmd to do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, line):
        """
        Overrides do_EOF method from cmd.Cmd to handle EOF (Ctrl+D) input.
        """
        return True  # Signals the program to exit

    def help_EOF(self):
        """
        Provides help information for the EOF command.
        """
        print("Quit command to exit the program\n")

    def do_quit(self, line):
        """
        Defines the quit command to exit the program.
        """
        raise SystemExit

    def help_quit(self):
        """
        Provides help information for the quit command.
        """
        print("Quit command to exit the program\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()  # Starts the command line interface loop
