def append_to_file(data, file_name):
    with open(file_name, 'a') as file:
        string_to_append = file.write(data)
    return string_to_append


if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    data = "\nDon't Panic"

    print(f"Number of chars added: {append_to_file(data, file_name)}")

    data = "\nDon't Panic!!!"

    print(f"Number of chars added: {append_to_file(data, file_name)}")
