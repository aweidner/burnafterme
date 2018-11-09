import random

base62chars = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

def generate_short():
    return ''.join(random.choice(base62chars) for i in range(6))
