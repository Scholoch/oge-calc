def convert_to(number, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while number > 0:
        result = (digits[number % base] + result)
        number //= base
    return result


class CalcToNotation:
    def __init__(self, data, translate=10, printer=True):
        if not data or not isinstance(data, (list, tuple)):
            raise Exception(f'Incorrect input. {f'Was used {type(data)}.' if not isinstance(data, (list, tuple))
                            else 'Was transferred empty object.'}')
        elif isinstance(data, tuple):
            data = list((data,))
        if translate < 2 or translate > 36:
            raise Exception(f'Incorrect input. You entered translate "{translate}"')

        results = []
        for i in data:
            result = convert_to(int(i[0], i[1]), translate)
            results.append(result)
            if printer:
                print(f'{i[0]} ({i[1]}) = {result} ({translate})')

        print(f'Max: {convert_to(max([int(i, translate) for i in results]), translate)} |'
              f'| Min: {convert_to(min([int(i, translate) for i in results]), translate)}')


class CalcToPathUrl:
    def __init__(self, data, protocol, server, file):
        alfa = 'АБВГДЕЖ'
        data = data.split(' ')
        server, SExtension = server.split('.')
        file, FExtension = file.split('.')
        result, alfa_result, delta_result = '', '', ''
        for j in protocol, '://', server, '.' + SExtension, '/', file, '.' + FExtension:
            for i in range(len(data)):
                if j.lower() == data[i].lower():
                    result += str(i + 1)
                    alfa_result += alfa[i]
                    delta_result += j
                    break
        print(f'Output: "{delta_result}" || Answer "{result}" or "{alfa_result}"')


class CalcToB:
    def __init__(self, data, action, order):
        order = list(order)

        for i in range(len(action)):
            sub = action.pop(i)
            action.insert(i, sub.split(' '))

        f1, k, n = 0, 0, 0
        for i in order:
            if i == '2':
                f1 = 1
            elif f1 == 0:
                n += 1
            else:
                k += 1

        f2, y, u, o = 0, 0, 0, 0
        for i in order:
            if i == '1':
                u += 1
                f2 = 1
            elif f2 == 0:
                y += 1
            else:
                o += 1

        print(action)
        if action[1][0] == '*' and action[1][1] == '':
            alfa = int(action[0][0] + action[0][1])
            print(f'Answer -> {int((data[1] - k * alfa) / (data[0] + n * alfa))}')
        elif action[1][0] == '/' and action[1][1] == '':
            alfa = int(action[0][0] + action[0][1])
            print(f'Answer -> {int((data[0] + n * alfa) / (data[1] - k * alfa))}')
        elif action[0][1] == '' and action[0][0] == '*' and order == list('12221'):
            alfa = int(action[1][0] + action[1][1])
            print(f'Answer -> {int(max([(-3 * alfa + sqrt((3 * alfa)**2 - 4 * data[0] * (-data[1]))) / 2 * data[0],
                                        (-3 * alfa - sqrt((3 * alfa)**2 - 4 * data[0] * (-data[1]))) / 2 * data[0]]))}')
        elif action[0][1] == '' and action[0][0] == '*' and order == list('21212'):
            alfa = int(action[1][0] + action[1][1])
            print(f'Answer -> {int(max([(-alfa + sqrt(alfa**2 - 4 * (alfa + data[0]) * (alfa - data[1]))) / (2 * (alfa + data[0])),
                                        (-alfa - sqrt(alfa**2 - 4 * (alfa + data[0]) * (alfa - data[1]))) / (2 * (alfa + data[0]))]))}')
        elif action[1][0] == '+' and action[1][1] == '':
            alfa = int(action[0][1])
            print(u, y, o)
            print(f'Answer -> {int((data[1] - u * alfa * data[0]) / (o + y * u * alfa))}')
        elif action[1][0] == '-' and action[1][1] == '':
            alfa = int(action[0][1])
            print(f'Answer -> {int((u * alfa * data[0] - data[1]) / (y * u * alfa + o))}')
        else:
            raise Exception(f'Incorrect input action {action[1]}')


CalcToB([4, 28], ['* ', '+ 2'], '12221')