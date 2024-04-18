def create_secret_language(sentence):

    words = sentence.split()
    secret_words = []


    for word in words:

        characters = list(word)

        odd_chars = []
        even_chars = []

        for index, char in enumerate(characters):
            if index % 2 == 0:
                even_chars.append(char)
            else:
                odd_chars.append(char)

        secret_word = ''.join(odd_chars) + ''.join(even_chars)

        secret_words.append(secret_word)


    secret_language = ' '.join(secret_words)
    return secret_language

def decode_secret_language(secret_language):

    secret_words = secret_language.split()
    normal_words = []

    for secret_word in secret_words:

        midpoint = len(secret_word) // 2

        odd_chars = secret_word[:midpoint]
  
        even_chars = secret_word[midpoint:]

        normal_word = ''.join(''.join(pair) for pair in zip(even_chars, odd_chars))
    
        normal_words.append(normal_word)

    original_sentence = ' '.join(normal_words)
    return original_sentence


sentence = "siddhi is great"
secret_language = create_secret_language(sentence)
print("Secret language:", secret_language)


decoded_sentence = decode_secret_language(secret_language)
print("Decoded sentence:", decoded_sentence)
