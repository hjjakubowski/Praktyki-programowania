def Add(numbers):
    if ",\n" in numbers or "\n," in numbers:
        raise ValueError("Nieprawidłowy format danych wejściowych")

    numbers = numbers.replace("\n", ",")
    if not numbers:
        return 0
    try:
        parts = numbers.split(",")
        return sum(int(n) for n in parts)

    except ValueError:
        raise ValueError("Nieprawidłowe dane wejściowe")