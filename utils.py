class utils:
    def reversed(self, number: int) -> int:
        result = 0
        while number != 0:
            result = (result * 10) + (number % 10)
            number //= 10
        return result

    def formatter(self, number: int) -> tuple:
        return bin(number), oct(number)