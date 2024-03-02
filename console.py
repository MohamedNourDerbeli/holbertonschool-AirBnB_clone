#!/usr/bin/python3
"""Console module

This module contains the HBNBCommand class which extends
cmd.Cmd to create a simple command-line interface.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class extends cmd.Cmd to create a
    simple command-line interface.
    """

    prompt = "(hbnb) "  # Sets the prompt for the command line interface

    def emptyline(self):
        """
        Overrides emptyline method from cmd.Cmd to do
        nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, line):
        """
        Overrides do_EOF method from cmd.Cmd to handle EOF (Ctrl+D) input.
        """
        return True  # Signals the program to exit

    def do_quit(self, line):
        """Usage:  quit
        Exit the application.
        """
        return True

    def do_create(self, line):
        """Usage: create <classname>
        Starts a new instance of specified class and saves it with a unique id.
                        Prints the newly created object's id.
        """
        if not line:
            print("** class name missing **")
            return
        if line in globals():
            cls = globals()[line]()
            cls.save()
            print(cls.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Usage: show [<classname>.<instance-id> | <classname> ]
        Displays information about an individual object\
or all objects of a particular class.
        """
        split_line = line.split()
        if not line:
            print("** class name missing **")
        elif split_line[0] not in globals():
            print("** class doesn't exist **")
        elif len(split_line) < 2:
            print("** instance id missing **")
        else:
            key = f"{split_line[0]}.{split_line[1]}"
            obj = storage.all()
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroy an object by its ID."""
        split_line = line.split()
        if not line:
            print("** class name missing **")
        elif split_line[0] not in globals():
            print("** class doesn't exist **")
        elif len(split_line) < 2:
            print("** instance id missing **")
        else:
            key = f"{split_line[0]}.{split_line[1]}"
            obj = storage.all()
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """List all instances of a given class."""
        class_name = line.split(".")[0]
        if class_name not in globals().keys() and len(line) != 0:
            print("** class doesn't exist **")
        else:
            obj = storage.all()
            print([str(obj[key]) for key in obj if class_name in key])

    def onecmd(self, line):
        """
        Override the onecmd method to handle commands
        in the format specific fromat
        """
        split_line = re.split("\\.|\\(", line)
        if line.endswith(".all()"):
            class_name = line.split(".")[0]
            self.do_all(class_name)
        elif line.endswith(".count()"):
            class_name = line.split(".")[0]
            if class_name not in globals().keys() and len(line) != 0:
                print("** class doesn't exist **")
            else:
                obj = storage.all()
                count = 0
                for key in obj:
                    if class_name in key:
                        count += 1
                print(count)
        if len(split_line) >= 2:
            if split_line[1] == "show":
                class_name_id = f"{split_line[0]} {split_line[2].strip(')')}"
                self.do_show(class_name_id)
        else:
            # Fallback to the default onecmd behavior
            return cmd.Cmd.onecmd(self, line)

    def do_update(self, line):
        """Usage: update <class name> <id> <attribute name> \
"<attribute value>"
        """
        split_line = line.split()
        if not line:
            print("** class name missing **")
        elif split_line[0] not in globals():
            print("** class doesn't exist **")
        elif len(split_line) < 2:
            print("** instance id missing **")
        elif len(split_line) < 3:
            print("** attribute name missing **")
        elif len(split_line) < 4:
            print("** value missing **")
        else:
            key = f"{split_line[0]}.{split_line[1]}"
            obj = storage.all()
            if key in obj:
                obj[key].__dict__[split_line[2]] = split_line[3]
                storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()  # Starts the command line interface loop
