#to calculate the fibonacci series of a number
def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        series = [0, 1]
        while len(series) < n:
            next_fib = series[-1] + series[-2]
            series.append(next_fib)
        return series

a=int(input("Enter the number: "))
print(fibonacci_series(a))
