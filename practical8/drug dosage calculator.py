def paracetamaol_volume (weight,strength):
    if not 10<weight<100  :
        print('your weight is out of range')
    else:
        i=15*weight/strength*5
    return i

weight=int(input('Your weight(kg) is:(kg)'))
strength=int(input('Your paracetamol strength(mg/5ml) is:(_mg/5ml)'))
print('suggested volume is', paracetamaol_volume(weight,strength))