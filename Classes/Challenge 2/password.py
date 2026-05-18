import random

class Password:

    def __init__(self, strength):
        self.strength = strength
        self.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        self.numbers = "1234567890"
        self.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    def low_strength(self):
        generated_password = []

        for x in range(0,4):
            generated_password.append(self.ascii_lowercase[random.randint(0,25)])

        for i in range(0,4):
            generated_password.append(self.ascii_lowercase[random.randint(0,25)].upper())

        random.shuffle(generated_password)

        return "".join(generated_password)

    def mid_strength(self):
        generated_password = []

        for x in range(0, 4):
            generated_password.append(self.ascii_lowercase[random.randint(0, 25)])

        for i in range(0, 4):
            generated_password.append(self.ascii_lowercase[random.randint(0, 25)].upper())

        for n in range(0, 4):
            generated_password.append(self.numbers[random.randint(0, 9)])

        random.shuffle(generated_password)

        return "".join(generated_password)

    def high_strength(self):
        generated_password = []

        for x in range(0, 4):
            generated_password.append(self.ascii_lowercase[random.randint(0, 25)])

        for i in range(0, 4):
            generated_password.append(self.ascii_lowercase[random.randint(0, 25)].upper())

        for n in range(0, 4):
            generated_password.append(self.numbers[random.randint(0, 9)])

        for n in range(0, 4):
            generated_password.append(self.punctuation[random.randint(0, len(self.punctuation)-1)])

        random.shuffle(generated_password)

        return "".join(generated_password)

    def random_password(self):
        if self.strength == "low":
            return self.low_strength()

        elif self.strength == "mid":
            return self.mid_strength()

        elif self.strength == "high":
            return self.high_strength()

        else:
            pass