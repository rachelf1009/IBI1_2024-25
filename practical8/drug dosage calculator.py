def paracetamol_volume (weight,strength):
    if not 10<weight<100  :
        print('your weight is out of range')
        return
    if strength not in [120, 250]:
        print('Invalid strength')
        return
    else:
        i=15*weight/strength*5
    return i

weight=int(input('Your weight(kg) is:(kg)'))
strength=int(input('Your paracetamol strength(mg/5ml) is:(_mg/5ml)'))
print('suggested volume is', paracetamol_volume(weight,strength))