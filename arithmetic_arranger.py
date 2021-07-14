def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for i, problem in enumerate(problems):
        num1 = problem.split()[0]
        operator = problem.split()[1]
        num2 = problem.split()[2]
        length = max(len(num1), len(num2))

        if not(num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(num1) >= 5 or len(num2) >= 5:
            return 'Error: Numbers cannot be more than four digits.'

        if operator == "+":
            result = str(int(num1) + int(num2))

        elif operator == "-":
            result = str(int(num1) - int(num2))

        else:
            return "Error: Operator must be '+' or '-'."

        line1 = line1 + num1.rjust(length+2)
        line2 = line2 + operator + num2.rjust(length+1)
        line3 = line3 + ''.rjust(length+2, '-')
        line4 = line4 + result.rjust(length+2)

        if i < len(problems) -1:
            line1 += '    '
            line2 += '    '
            line3 += '    '
            line4 += '    '

        if solve:
            arranged_problems = f"{line1}\n{line2}\n{line3}\n{line4}"
        else:
            arranged_problems = f"{line1}\n{line2}\n{line3}"


    return arranged_problems