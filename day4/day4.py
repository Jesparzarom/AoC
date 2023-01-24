import numbers

with open("day4\input.txt") as f:
    elements = f.readlines()
st = [element.strip("\n-,").split("-") for element in elements]

delcom = [am[0].split(",") + am[1].split(",") 
          + am[2].split(",") for am in st]

values = []
values2 = []

for idx in delcom:  
    min1, max1 = int(idx[0]), int(idx[1])
    min2, max2 = int(idx[2]), int(idx[3])
    
    # PART 1
    values.append(
        ([(min1 <= min2 and max1 >= max2)]   # Si el resultado de A > B 
         != [min2 <= min1 and max2 >= max1]) # es distinto de B > A
         or (max1 == max2 and min1 == min2)  # O los min y max son iguales
    )
    
    # PART 2
    if max2 < min1 or max1 < min2:  # Si B<-A o A<-B (fuera del rango)
        values2.append(1)

print(sum([yes for yes in values if yes != False]))
print(len(delcom) - sum(values2))