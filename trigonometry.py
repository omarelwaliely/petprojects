import math

opposite = input("opposite: ")
adjacent = input("adjacent: ")
if opposite:
    opp_pow_two = float(opposite)**2
elif not opposite:
    opposite = False
if adjacent:
    adj_pow_two = float(adjacent)**2
elif not adjacent:
    adjacent = False
if opposite and adjacent:
    hypotoneuse = math.sqrt((opp_pow_two) + (adj_pow_two))
elif not opposite and adjacent:
    hypotoneuse = input("hypotoneuse: ")
    if hypotoneuse and adjacent:
        sqr_hypotoneuse = float(hypotoneuse) ** 2
        opposite = math.sqrt(sqr_hypotoneuse - adj_pow_two)
    else:
        hypotoneuse = False
elif not adjacent and opposite:
    hypotoneuse = input("hypotoneuse: ")
    if not adjacent and opposite and hypotoneuse:
        sqr_hypotoneuse = float(hypotoneuse) ** 2
        adjacent = math.sqrt(sqr_hypotoneuse - opp_pow_two)
elif not(opposite and adjacent):
    hypotoneuse = input("hypotoneuse: ")
    sqr_hypotoneuse = float(hypotoneuse) ** 2
    angle = input("angle: ")
    sin_angle = math.sin(math.radians(float(angle)))
    opposite = sin_angle * float(hypotoneuse)
    opp_pow_two = float(opposite)**2
    adjacent = math.sqrt(sqr_hypotoneuse - opp_pow_two)


else:
    hypotoneuse = False
if not(hypotoneuse and adjacent) and opposite:
    angle = input("angle: ")
    sin_angle = math.sin(math.radians(float(angle)))
    hypotoneuse = float(opposite)/sin_angle
    sqr_hypotoneuse = float(hypotoneuse) ** 2
    adjacent = math.sqrt(sqr_hypotoneuse - opp_pow_two)
elif not(hypotoneuse and opposite) and adjacent:
    angle = input("angle: ")
    cos_angle = math.cos(math.radians(float(angle)))
    hypotoneuse = float(adjacent)/cos_angle
    sqr_hypotoneuse = float(hypotoneuse) ** 2
    opposite = math.sqrt(sqr_hypotoneuse - adj_pow_two)

sin = float(opposite)/float(hypotoneuse)
cos = float(adjacent)/float(hypotoneuse)
tan = float(opposite)/float(adjacent)
sec = float(hypotoneuse)/float(adjacent)
cosec = float(hypotoneuse)/float(opposite)
cotan = float(adjacent)/float(opposite)
print(f"opposite: {opposite} , adjacent: {adjacent} , hypotoneuse: {hypotoneuse}, sin: {sin} , cos: {cos} , tan: {tan} ,  cosec: {cosec} , sec: {sec}, cotan: {cotan}")
