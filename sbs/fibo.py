def fibo_recur(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_iter(n - 1) + fibo_iter(n - 2)


def fibo_tail(n, a=0, b=1):
    # Tail Recursion
    # A tail recursive function to
    # calculate n th fibnacci number
    if n == 0:
        return a
    if n == 1:
        return b
    return fibo_tail(n - 1, b, a + b)


def fibo_iter(n):
    # Iterative
    prev, next_ = 0, 1
    for i in range(n):
        prev, next_ = next_, (prev + next_)
    return prev


def fibo_memo(n):
    # Memoization & Dynamic Programming
    list_nums = [0, 1]
    for i in range(n - 1):
        next_val = list_nums[i] + list_nums[i + 1]
        list_nums.append(next_val)
    return list_nums[n]


def main():
    result = [fibo_iter(10), fibo_memo(10), fibo_tail(10), fibo_recur(10)]
    print(result)


if __name__ == "__main__":
    main()
