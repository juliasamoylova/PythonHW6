# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print(tuple(((not(x and y and z) == (not(x) or not(y) or not(z))) for z in range(2) for y in range(2) for x in range(2))))