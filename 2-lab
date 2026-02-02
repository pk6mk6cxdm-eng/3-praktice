class Tizbek:
    def n_member(self, n):
        pass

    def first_k_members(self, k):
        pass

    def sum_k_members(self, k):
        pass

class Arithmetic(Tizbek):
    def __init__(self, a1, d):
        self.a1 = a1
        self.d = d

    def n_member(self, n):
        return self.a1 + (n - 1) * self.d

    def first_k_members(self, k):
        return [self.n_member(i) for i in range(1, k + 1)]

    def sum_k_members(self, k):
        return k / 2 * (2 * self.a1 + (k - 1) * self.d)
class Geometric(Tizbek):
    def __init__(self, b1, q):
        self.b1 = b1
        self.q = q

    def n_member(self, n):
        return self.b1 * (self.q ** (n - 1))

    def first_k_members(self, k):
        return [self.n_member(i) for i in range(1, k + 1)]

    def sum_k_members(self, k):
        if self.q == 1:
            return self.b1 * k
        return self.b1 * (self.q ** k - 1) / (self.q - 1)
class Fibonacci(Tizbek):
    def n_member(self, n):
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return a

    def first_k_members(self, k):
        result = []
        a, b = 1, 1
        for _ in range(k):
            result.append(a)
            a, b = b, a + b
        return result

    def sum_k_members(self, k):
        return sum(self.first_k_members(k))
a = Arithmetic(2, 3)
g = Geometric(2, 2)
f = Fibonacci()

print("Арифметикалық тізбек:")
print("5-мүше:", a.n_member(5))
print("Алғашқы 5 мүше:", a.first_k_members(5))
print("Қосындысы:", a.sum_k_members(5))

print("\nГеометриялық тізбек:")
print("5-мүше:", g.n_member(5))
print("Алғашқы 5 мүше:", g.first_k_members(5))
print("Қосындысы:", g.sum_k_members(5))

print("\nФибоначчи тізбегі:")
print("5-мүше:", f.n_member(5))
print("Алғашқы 5 мүше:", f.first_k_members(5))
print("Қосындысы:", f.sum_k_members(5))
