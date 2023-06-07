FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    :param filepath: Text file
    :return: A list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write a to-do items list in the text file.
    :param todos_arg: To-do list
    :param filepath: Text file
    """
    with open(filepath, 'w+') as file_local:
        file_local.writelines(todos_arg)



if __name__ == "__main__":
    print(__name__)
    print("Hello from functions")
