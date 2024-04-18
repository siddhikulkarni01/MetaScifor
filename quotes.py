import random

def random_quotes():

    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Don't judge each day by the harvest you reap but by the seeds that you plant. - Robert Louis Stevenson"
    ]

    result = random.choices(quotes)

    return result

print(random_quotes())