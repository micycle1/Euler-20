def euler_41():
    return sum(((8 * sum(ord(letter) - 96 for letter in item) + 1) ** 0.5).is_integer() for item in [x.strip(' "').lower() for x in open("p042_words.txt").read().split(",")])
