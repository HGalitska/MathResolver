def add_new_module(package, module):
    all_modules = package.__all__
    all_modules.append(module)
    package_init = open(r"" + package.__name__.replace(".", "/") + "/__init__.py", "w")
    package_init.write("__all__ = " + str(all_modules))
    package_init.close()


def get_modules(package):
    return package.__all__


def generate_module_name(package, expression):
    data = get_modules_for_expr(package, expression, True)
    return data[0] + str(len(data[1]))


def get_modules_for_expr(package, expression, prefix_flag=False):
    prefix = str(len(expression)) + "_"
    modules = get_modules(package)
    same_length_names = []

    for module in modules:
        if module.startswith(prefix):
            same_length_names.append(module)

    if prefix_flag:
        return prefix, same_length_names

    return same_length_names


def find_solution(package, expression):
    modules = get_modules_for_expr(package, expression)
    import importlib
    for module_name in modules:
        module = importlib.import_module(package.__name__ + "." + module_name)
        doc = module.__doc__
        if doc == "":
            return None
        if expression in doc:
            print("Already have it!", doc)
            return doc
    return None


def get_path(package, module):
    return r"" + package.__name__.replace(".", "/") + "/" + module + ".py"


def open_doc_string(path, expression):
    module_file = open(path, "w")
    module_file.write('"""\n' + expression + '\n')
    module_file.close()


def close_doc_string(path, package, expression):
    module_file = open(path, "a")
    module_file.write('\n"""\n')
    module_file.write("if __name__ == '__main__':\n")
    module_file.write('     from ' + package.__name__.replace('solutions', 'algorithms') + ' import solve\n')
    module_file.write('     solve("' + expression + '")\n')
    module_file.close()


def add_to_doc(path, string):
    module_file = open(path, "a")
    module_file.write(string)
    module_file.close()


def print_doc(path):
    print(path.split())
    module_file = open(path, "r")
    print(module_file.read().replace('"""', ''))
    module_file.close()


def clear_doc(path):
    module_file = open(path, "w")
    module_file.write("")
    module_file.close()

