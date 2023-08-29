#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    z = 0
    listt = []
    for i in range(list_length):
        try:
            z = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            z = 0
        except (ValueError, TypeError):
            print("wrong type")
            z = 0
        except IndexError:
            print("out of range")
            z = 0
        finally:
            listt.append(z)
    return listt
