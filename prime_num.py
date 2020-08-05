# Function to check prime numbers
def is_prime(number):
    """
    Checking number is prime

    :param number: number to check
    :return: bool
    """
    for divider in range(2, number):
        if number % divider == 0:
            return False

    return True


# getting prime numbers within a specified range
def get_primes_from_range(start, end):
    """
    Getting all primes numbers in the list

    :param start: from number
    :param end: to number
    :return: list
    """
    result = []

    for number in range(start, end + 1):
        if is_prime(number):
            result.append(number)

    return result

user_start=2
user_end=30

print(get_primes_from_range(user_start, user_end))