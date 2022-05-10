import random
import string


def get_random_alphabetical_strings():
    """Generates random alphabetical strings."""
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10))])


def get_random_real_numbers():
    """Generates random real numbers."""
    length = random.randint(1, 10)
    return str(round(random.uniform(0.0, 10000.0), length))


def get_random_integers():
    """Generates random integers."""
    return str(random.randint(0, 10000))


def get_random_alphanumerics():
    """Generates random alphanumerics."""
    return ''.join(random.choice(
        string.ascii_uppercase + string.ascii_lowercase + string.digits
    ) for _ in range(10))
