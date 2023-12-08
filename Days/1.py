listofnumber = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

my_string = "51pvmcdzbnxtsevenqrvmmfhchthree"
my_dict ={
 'one': 'on1e',
 'two': 'tw2o',
 'three': 'thr3e',
 'four': 'fo4ur',
 'five': 'fi5ve',
 'six': 'si6x',
 'seven': 'sev7en',
 'eight': 'ei8ght',
 'nine': 'ni9ne'}


def convertstring(string):
    for key, value in my_dict.items():
        if key in string:
            string = string.replace(key, value)

    return (string)


def check_if_digit(string):
    digit_list = [char for char in string if char.isdigit()]
    return digit_list


def get_first_and_last(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) > 1:
        return lst[0], lst[-1]
    else:
        return None


def read_file(filename):
    runningtotal = 0
    with open(filename, 'r') as file:
        finallistresult = []
        for line in file:
            finalresult = 0

            line = line.strip()

            convertstringstoint = convertstring(line)
            print(convertstringstoint)
            print(" ")

            result = check_if_digit(convertstringstoint)

            finalresult = get_first_and_last(result)

            print("list  " + str(finalresult))
            print(" ")

            if len(finalresult) == 2:
                combined_string = ''.join(finalresult)
            else:
                finalresult = finalresult + finalresult[0]
                combined_string = ''.join(finalresult)

            print("stringcombine " + combined_string)
            print(" ")
            combined_string = int(combined_string)

            runningtotal = runningtotal + combined_string
            print(runningtotal)
            print(" ")
        return runningtotal


mainthing = read_file("1.txt")
print(mainthing)
