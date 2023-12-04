def evaluate_rpn(expression):
    stack = []

    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(float(token))
        elif token in {'+', '-', '*', '/'}:
            operand2, operand1 = stack.pop(), stack.pop()
            result = eval(f"{operand1} {token} {operand2}")
            stack.append(result)
        elif token == '=':
            print(f"Result: {stack.pop()}")
        else:
            print("Invalid token:", token)
            return

# Przykładowe użycie
try:
    rpn_expression = input("Podaj wyrażenie w odwrotnej notacji polskiej (oddzielaj spacją): ")
    evaluate_rpn(rpn_expression)
except Exception as e:
    print(f"Wystąpił błąd: {e}")