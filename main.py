# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    my_list = [1, 5, 12, 17, 5, 20, 1, 17, 1, 5, 12, 17, 12]
    a = 5
    index_a = -1
    already_in_list = False

    for i in range(len(my_list)):
        if my_list[i] == a:
            if not already_in_list:
                already_in_list = True
                continue
        if my_list[i] == a and already_in_list:
            index_a = i
            break

    print(index_a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
