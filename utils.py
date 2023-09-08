class utils:
    def reversed(number: int) -> int:
        result = 0
        while number != 0:
            result = (result * 10) + (number % 10)
            number //= 10
        return result

    def formatter(number: int) -> tuple:
        return bin(number), oct(number)