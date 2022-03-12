def read_list_from_file(filepath):
    file = open(filepath, 'r')
    orig_list = [int(x) for x in file.read().strip().split(" ")]
    file.close()
    return orig_list


def write_list_to_file(filepath, new_list: list):
    file = open(filepath, 'w')
    file.write(" ".join([str(x) for x in new_list]))
    file.close()


def remove_duplicates(initial_list: list):
    new_list = []
    for element in initial_list:
        if element not in new_list:
            new_list.append(element)
    return [new_list]


if __name__ == '__main__':
    write_list_to_file("output/output_1.txt", remove_duplicates(read_list_from_file("input/input_1.txt")))
