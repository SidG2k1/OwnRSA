# run on python 3
def PrimeQ(n):
    import math
    if n == 2: return True
    if n % 2 == 0 or n <= 1: return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0: return False
    return True
def EEA(a, b, m):
    import math
    # Solves ax+by=m for x
    x0, y0, r0, q0 = 0, 1, b, 0
    x1, y1, r1, q1 = 1, 0, a, 0
    while r1 != 0:
        xt, yt, rt, qt = x0, y0, r0, q0 # temp vars
        x0, y0, r0, q0 = x1, y1, r1, q1
        q1 = math.floor(rt / r0)
        r1 = rt - q1 * r0
        y1 = yt - q1 * y0
        x1 = xt - q1 * x0
    return x0
def encode(text):
    # converts string text to string num
    import encode
    o = ""
    while text != "":
        o += encode.translateFwd[text[0]]
        text = text[1:]
    return o
def expMod(n, e, m):
    # Uses square and reduce method to find n**e % m
    mu = 1
    while e >= 1:
        mu *= n
        e -= 1
        mu = mu % m
    return mu
class RSA:
    def __init__(self, secLvl = 8):
        """
        secLvl is min prime digit size
        """
        self.secLvl = 10**secLvl
        self.p = self.p()
        self.q = self.q()
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.e()
        self.d = self.d()
        self.n = self.p * self.q
        self.pub = [self.e, self.n]
        self.priv = {"key" : [self.d, self.n],
                     "primes" : [self.p, self.q]}
    def p(self):
        from random import randint as rand
        while True:
            p = rand(self.secLvl, self.secLvl**2)
            if PrimeQ(p): return p
    def q(self):
        from random import randint as rand
        while True:
            q = rand(self.secLvl, self.secLvl**2)
            if q != self.p and PrimeQ(q): return q
    def e(self):
        from math import gcd
        from random import randint as rand
        while True:
            e = rand(1, self.phi)
            if gcd(e, self.phi) == 1: return e
    def d(self):
        return EEA(self.e, self.phi, 1) % self.phi
    def crypt(self, message):
        # message is string. Convert to int
        # break into correct size, return as list
        message = message.lower()
        toCrypt = []
        low, hi = 0, 5
        while message != "":
            toCrypt.append(encode(message[low : hi]))
            message = message[hi:]
            low, hi = low + 5, hi + 5
        toCrypt = map(int, toCrypt)
        crypt = []
        for m in toCrypt:
            crypt.append(expMod(m, self.e, self.n))
        return crypt
    def decrypt(self, message):
        # check if message in list
        # convert message to string
        pass
def main():
    code = RSA()
    #print("this should be unreadable", code.crypt("test"))
    #print("this should say \" test\"", code.decrypt(code.crypt("test")))
    print(code.priv)
    print(code.pub)
main()
