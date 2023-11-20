class FibIterator:

    """Итератор, который возвращает числа в последовательности Фибоначчи"""

    def __init__(self, n: int):
        self.n = n

    def __iter__(self):
        return FibonacciIterator(self.n)


class FibonacciIterator:

    """Итератор для перебора чисел Фибоначчи"""

    def __init__(self, n: int):
        self.n = n  # Нужное количество чисел Фибоначчи
        self.current, self.next = 0, 1

    def __next__(self) -> int:
        if self.n <= 0:
            # Итератор исчерпан
            raise StopIteration()
        self.n -= 1
        current = self.current
        self.current, self.next = self.next, self.next + current
        return current

    def __iter__(self):
        """
        Чтобы соответствовать протоколу, каждый итератор должен
        одновременно быть итерируемым объектом.
        """
        return self


class FibGenerator:

    """Генератор, который возвращает числа в последовательности Фибоначчи"""

    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.n = n

    def fib(self):
        for __ in range(self.n):
            yield self.a
            self.a, self.b = self.b, self.a + self.b
