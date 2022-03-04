import math


def base_y(x: float) -> float:
    return math.pow(x, 3) + 3 * x + 4


def get_input(param) -> float:
    while True:
        print(f"Введите значение {param}:")
        try:
            return float(input())
        except ValueError as exc:
            print(f"Введеная строка не является числом. Попробуйте заново.\nПодробнее: {exc}")


def calculation(x: float, eps: float) -> float:
    count = 3
    res = x
    iteration = math.pow(x, 3) / (2 * 3)
    plus = False

    while iteration > eps:
        if plus:
            res += iteration
            plus = False
        else:
            res -= iteration
            plus = True

        count += 2
        iteration *= x*x / ((count - 1) * count)

    return res


def print_output(y: float):
    print(f"Результат вычисления суммы ряда = {y}")


def main():
    input_X, input_eps, output = None, None, None

    while True:
        print("1 - Запустить программу \n2 - Ввести значения \n3 - Показать историю \n4 - Выйти")
        get_move = get_input("")

        match get_move:
            case 1:
                if input_X != None and input_eps != None:
                    output = calculation(input_X, input_eps)
                    print_output(output)
                else:
                    print("Для начала введите значения")
            case 2:
                input_X = get_input("X")
                input_eps = get_input("точности E")
            case 3:
                if output != None:
                    print(f"X: {input_X}, eps: {input_eps}, Результат: {output}")
                else:
                    print("В истории ничего не найдено")
            case 4:
                return
            case _:
                print("Данные введены неверно")

        print("\n")



if __name__ == "__main__":
    main()