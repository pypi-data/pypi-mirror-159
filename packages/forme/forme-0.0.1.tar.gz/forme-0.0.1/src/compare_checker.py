def compare_checker(input_list, check_list):
    cflag = False

    for inval in input_list:
        for chval in check_list:
            if inval == chval:
                cflag == True
            else:
                cflag == False

    return cflag