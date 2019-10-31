MOD = 100007

def _count_strict_numbers_helper(num_digits, last_digit):
    if num_digits == 0:
        return 0

    # because of the way we're calling recursively
    if last_digit == -1 or last_digit == 10:
        return 0

    # base case
    if num_digits == 1:
        if last_digit == 0 or last_digit == 9:
            return 1
        return 2

    sum = _count_strict_numbers_helper(num_digits - 1, last_digit + 1) % MOD + \
        _count_strict_numbers_helper(num_digits - 1, last_digit - 1) % MOD
    return sum % MOD


def count_strict_numbers_recursive(num_digits):
    if num_digits == 0:
        return 0
    if num_digits == 1:
        return 9

    # Numbers can only start with 1
    return sum([
        _count_strict_numbers_helper(num_digits - 1, ix)
        for ix in range(1, 10)
    ]) % MOD


def count_strict_numbers(num_digits):
    if num_digits == 0:
        return 0

    # For 1 digit
    counts = [1] * 10
    counts[0] = 0

    for n in range(num_digits - 1):
        new_counts = [0] * 10
        new_counts[0] = counts[1]
        new_counts[9] = counts[8]

        for last_digit in range(1, 9):  # digits 1-8
            new_counts[last_digit] = counts[last_digit - 1] % MOD + counts[last_digit + 1] % MOD

        counts = new_counts

    rval = sum(counts) % MOD
    print(rval)
    return rval


def test_func(func):
    assert (func(0)) == 0
    assert (func(1)) == 9
    assert (func(2)) == 17
    print('1')
    assert (func(3)) == 32
    assert (func(10)) == 2986
    assert (func(13)) == 21053
    assert (func(20)) == 16986

    print('2')
    assert (func(50)) == 21498
    assert (func(100)) == 31182
    print('3')
    assert (func(
        1000)) == 20278
    print('4')
    assert (func(
        2000)) == 39966
    print('5')

print(count_strict_numbers(4))
