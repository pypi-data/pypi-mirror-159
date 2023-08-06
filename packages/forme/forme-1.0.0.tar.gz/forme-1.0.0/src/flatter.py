def flatter(input_list):
    try:
        flatList = [item for elem in input_list for item in elem]
        return flatList

    except TypeError:
        print("U pick a wrong type, foo. Please check a input type")
    