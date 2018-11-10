import re
import random

base62chars = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

def generate_short():
    return ''.join(random.choice(base62chars) for i in range(6))


class TimeoutFormatException(Exception):
    pass


def parse_timeout(timeout):
    timeout_match = re.match(r'([0-9]+)(s|m|h|d|w|y)', timeout)

    if not timeout_match:
        raise TimeoutFormatException(f"Could not parse {timeout}")

    duration = int(timeout_match.group(1))
    unit = timeout_match.group(2)

    if unit == "s":
        return duration
    elif unit == "m":
        return duration * 60
    elif unit == "h":
        return duration * 60 * 60
    elif unit == "d":
        return duration * 60 * 60 * 24
    elif unit == "w":
        return duration * 60 * 60 * 24 * 7
    else: 
        return duration * 60 * 60 * 24 * 365 
