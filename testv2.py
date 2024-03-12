def decode(message_file):

    file_coded = open(message_file, "r")
    data = file_coded.readlines()
    file_coded.close()
    list_of_lines_coded = []
    numbers = []
    numbers_keys = []
    list_of_correct_lines = []
    output = []
    final_message = ""

    for i in data:
        i = i[:-1]
        list_of_lines_coded.append(i)

    for item in list_of_lines_coded:
        item = item.split()
        numbers.append(int(item[0]))
    numbers.sort()

    i = 0
    while i < len(numbers):
        numbers_keys.append(numbers[i])
        i = i + len(numbers_keys) + 1

    for item in list_of_lines_coded:
        item = item.split()
        list_of_correct_lines.append(item)

    for item in list_of_correct_lines:
        if int(item[0]) in numbers_keys:
            output.append(item)
            output.sort(key=lambda x: int(x[0]))

    for element in output:
        final_message = final_message + element[1] + " "

    return final_message


def main():
    print(decode("data.txt"))


if __name__ == '__main__':
    main()

