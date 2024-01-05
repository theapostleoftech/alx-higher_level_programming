#!/usr/bin/python3.8
import importlib.util


def print_hidden_names(module_path):
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = [name for name in dir(module) if not name.startswith("__")]

    for name in sorted(names):
        print(name)

#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: {} <module_path>".format(sys.argv[0]))
#         sys.exit(1)
#
#     module_path = sys.argv[1]
#     print_hidden_names(module_path)
