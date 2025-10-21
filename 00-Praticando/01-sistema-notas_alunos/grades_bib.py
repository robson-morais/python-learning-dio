def calculate_average(grades):
    return sum(grades)/3

def result(average):
    result = ""
    if average < 5:
        result = "Failed"
    elif average >= 5 and average < 7:
        result = "Retake"
    else:
        result = "Passed"
    return result