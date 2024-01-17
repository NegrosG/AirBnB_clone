#!/usr/bin/python3
"""Defining the HBNB console"""
import cmd
from models.base_model import BaseModel
import shlex
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Defining the hbnb command prompt"""
    prompt = "(hbnb)"

    valid_class = ["BaseModel", "User", "Amenity",
                   "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        functions does nothing when an emptyline is
        entered
        """
        pass

    def do_quit(self, arg):
        """defining the quit function
        to exit the console"""

        return True

    def do_EOF(self, arg):
        """Defining the End of life function
        for the console"""

        print()
        return True

    def do_create(self, arg):
        """
        creates an instance of a class and prints it's id
        and saves to JSON file
        Usage: Create <class_name>
        """
        arguments = shlex.split(arg)
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.valid_class:
            print("** class doesn't exist **")
        new_inst = eval(f"{arguments[0]}()")
        storage.save()
        print(new_inst.id)

    def do_show(self, arg):
        """
        Prints a string representation of an instance
        based on the class and id
        usage: show <class_name> <id>
        """
        arguments = shlex.split(arg)
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.valid_class:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(arguments[0], arguments[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Method Deletes an instance based on the class name
        and id, saves to JSON
        Usage: destroy <class_name> <id>
        """
        arguments = shlex.split(arg)

        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.valid_class:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(arguments[0], arguments[1])
            for key in objects:
                del object[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances or not
        on the class name
        Usage: <user>.all
        """
        objects = storage.all()
        arguments = shlex.split(arg)

        if len(arguments) == 0:
            for key, value in objects.items():
                print(str(value))
        elif arguments[0] not in self.valid_class:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split(".")[0] == arguments[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class
        usage: <class name>.count()
        """
        objects = storage.all()

        arguments = shlex.split(arg)

        if arg:
            class_nm = arguments[0]

        count = 0

        if arguments:
            if class_nm in self.valid_class:
                for obj in objects.values():
                    if obj.__class__.__name__ == class_nm:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        updates an instance of the class name based on the class
        and <id> by adding or updating attribute
        Usage: Update <class_name> <id <attribute_name> <attribute_value>
        """
        arguments = shlex.split(arg)

        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.valid_class:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(arguments[0], arguments[1])
            if key not in objects:
                print("** no instance found **")
            elif len(arguments) < 3:
                print("** attribute name missing **")
            elif len(arguments) < 4:
                print("** value missing **")
            else:
                objs = objects[key]

                att_name = arguments[2]
                att_value = arguments[3]
                try:
                    att_value = eval(att_value)
                except Exception:
                    pass
                setattr(objs, att_name, att_value)

                objs.save()

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid
        """
        arg_list = arg.split('.')

        class_nm = arg_list[0]  # incoming class name

        command = arg_list[1].split('(')

        pre_method = command[0]  # incoming command method

        e_arg = command[1].split(')')[0]  # extra arguments

        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if pre_method in method_dict.keys():
            if pre_method != "update":
                return method_dict[pre_method]("{} {}".format(class_nm, e_arg))
            else:
                if not class_nm:
                    print(" **class name missing** ")
                    return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
