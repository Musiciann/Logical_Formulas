import itertools

OPERATIONS = ['&', '>', '~', '|', '=']

def binary_to_decimal_direct_code(binary_num: str) -> tuple:
    decimal_value = 0
    sign = binary_num[0]
    binary_value = binary_num
    for i, digit in enumerate(reversed(binary_num[1:])):
        decimal_value += int(digit) * (2 ** i)

    if sign == '1':
        decimal_value *= -1

    return binary_value, decimal_value

def get_expression() -> str:
    expression = input("Insert formula >>> ")
    return expression

def parse_expression(expression: str) -> tuple:
    variables = []
    operations = []

    for char in expression:
        if char.isalpha() and char not in variables:
            variables.append(char)
        elif char in OPERATIONS:
            operations.append(char)

    return variables, operations

def evaluate_formula(expression: str, values: dict) -> int:
    for variable, value in values.items():
        expression = expression.replace(variable, str(value))

    expression = expression.replace('&', ' and ')
    expression = expression.replace('|', ' or ')
    expression = expression.replace('~', ' not ')
    expression = expression.replace('=', ' == ')
    expression = expression.replace('>', ' <= ')

    return int(eval(expression))

def truth_table(expression: str) -> tuple:
    variables, _ = parse_expression(expression)
    n = len(variables)

    combinations = list(itertools.product([0, 1], repeat=n))
    print("\t".join(variables) + f"\t{expression}")

    binary_result = []
    expr_result = []

    for combo in combinations:
        values = dict(zip(variables, combo))
        result = evaluate_formula(expression, values)
        binary_result.append(result)
        expr_result.append((values, result))
        print("\t".join(map(str, combo)) + "\t" + str(int(result)))

    resu = binary_result_decimal(tuple(binary_result))
    print(f"Decimal form: ", resu)

    return variables, expr_result, combinations

def generate_sdnf(variables, results) -> str:
    sdnf_terms = []
    for values, result in results:
        if result:
            term = []
            for variable in variables:
                if values[variable] == 1:
                    term.append(variable)
                else:
                    term.append('~' + variable)
            sdnf_terms.append('(' + ' & '.join(term) + ')')
    return ' | '.join(sdnf_terms)

def generate_sknf(variables: list, results: list):
    sknf_terms = []
    for values, result in results:
        if not result:
            term = []
            for variable in variables:
                if values[variable] == 0:
                    term.append(variable)
                else:
                    term.append('~' + variable)
            sknf_terms.append('(' + ' | '.join(term) + ')')
    return ' & '.join(sknf_terms)

def generate_sdnf_numeric(results: list, combinations: list) -> list:
    sdnf_terms = []
    result_combination = tuple(zip(results, combinations))
    for result in result_combination:
        if result[0][1]:
            numbers = []
            binary_number = ''
            for comb in result[1]:
                binary_number += str(comb)
            decimal = binary_to_decimal_direct_code(binary_number.zfill(8))
            sdnf_terms.append(decimal[1])
    return sdnf_terms

def generate_sknf_numeric(results: list, combinations: list) -> list:
    sknf_terms = []
    result_combination = tuple(zip(results, combinations))
    for result in result_combination:
        if not result[0][1]:
            numbers = []
            binary_number = ''
            for comb in result[1]:
                binary_number += str(comb)
            decimal = binary_to_decimal_direct_code(binary_number.zfill(8))
            sknf_terms.append(decimal[1])
    return sknf_terms

def binary_result_decimal(result: tuple) -> int:
    result_string = ""
    for num in result:
        result_string += str(num)
    result = "".join(result_string)
    decimal_result = binary_to_decimal_direct_code(result.zfill(8))
    return decimal_result[1]


