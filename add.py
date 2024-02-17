def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))

        print("[", end="")
        for i in range(0, len(print_list)):
            print(print_list[i].strip('"'), end="")
            if i != len(print_list) - 1:
                print(", ", end="")
        print("]")
