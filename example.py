#step1 = Getting input
inches_str = input ("How many inches of rain have fallen: ")

inches_float =float (inches_str)

gallons=f'{inches_float:.0f}'
inches_int = int (gallons)


volume = (inches_int/12)*43560

volume2 = (inches_float/12)*43560

gallons = volume *7.48051945

gallons=f'{gallons:.0f}'
gallons2 = volume2 *7.48051945

print(inches_int," in rain on 1 acre is", gallons, "gallon")
print(inches_float," in rain on 1 acre is", gallons2, "gallon")
