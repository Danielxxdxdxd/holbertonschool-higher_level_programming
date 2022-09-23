#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for indx in matrix:
        for value in range(len(indx)):
            if value < (len(indx) - 1):
                print("{:d} ".format(indx[value]), end="")
            else:
                print("{:d}".format(indx[value]), end="")
        print("")
