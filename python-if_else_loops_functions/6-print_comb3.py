#!/usr/bin/python3
def run():
    for numbers1 in range(0, 9):
        for numbers2 in range(1, 10):
            if numbers2 > numbers1:
                if not (numbers1 == 8 and numbers2 == 9):
                    print("{}{}, ".format(numbers1, numbers2), end="")
                if numbers1 == 8 and numbers2 == 9:
                    print("{}{}".format(numbers1, numbers2))

if __name__ == '__main__':
    run()
