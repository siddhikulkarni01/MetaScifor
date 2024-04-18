import random

def generate_password():
    res = random.randrange(1000,9999)
    return res
    
print(generate_password())