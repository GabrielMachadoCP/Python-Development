print("Digite a altura de 5 girafas:")
g1 = float(input())
g2 = float(input())
g3 = float(input())
g4 = float(input())
g5 = float(input())

if g1>g2 and g1>g3 and g1>g4 and g1>g5:
    print("A primeira girafa é a maior!")
elif g2>g1 and g2> g3 and g2> g4 and g2>g5:
    print("A Segunda girafa é a maior!")
elif g3>g1 and g3>g2 and g3>g4 and g3> g5:
    print("A terceira girafa é a maior!")
elif g4>g1 and g4>g2 and g4>g3 and g4>g5:
    print("A quarta girafa é a maior!")
else:
    print("A quinta girafa é a maior!")