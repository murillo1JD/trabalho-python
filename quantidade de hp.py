hp = 75
pocao = 50
maxhp = 100
HPcura = hp + pocao

#hp maior que 100?
if HPcura > maxhp:
    HPcura = maxhp

print(f'o hp apos usar a cura sera {HPcura}')
