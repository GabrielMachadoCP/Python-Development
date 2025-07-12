maior = ""
meio = ""
menor = ""
print("Digite 3 valores reais:")
A = int(input())
B = int(input())
C = int(input())

if A > B and A > C:
    A = maior
elif B > A and B > C:
    B = maior
elif C > A and C > B:
    C = maior

elif A > B and A < C:
    A = meio
elif A < B and A > C:
    A = meio
elif B > A and B < C:
    B = meio
elif B < A and B > C:
    B = meio
elif C > A and C > B:
    C = meio
elif C < A and C > B:
    C = meio
