# console.py
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_create(self, args):
        """Creates a new instance of BaseModel or a specified class."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        class_name = args_list[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        new_instance = self.class_dict[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Shows an instance of a specified class based on id."""
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")
            return
        if args_list[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = f"{args_list[0]}.{args_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """Destroys an instance of a specified class based on id."""
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")
            return
        if args_list[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = f"{args_list[0]}.{args_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """Shows all instances of a specified class, or all instances."""
        if args and args not in self.class_dict:
            print("** class doesn't exist **")
            return
        instances = storage.all()
        instance_list = []
        if not args:
            for instance in instances.values():
                instance_list.append(str(instance))
        else:
            for key, instance in instances.items():
                if key.split('.')[0] == args:
                    instance_list.append(str(instance))
        print(instance_list)

    def do_update(self, args):
        """Updates an instance of a specified class based on id."""
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")
            return
        if args_list[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = f"{args_list[0]}.{args_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        if len(args_list) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args_list[2], args_list[3])
        obj.save()


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
