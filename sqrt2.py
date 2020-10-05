# This is the raw file for the sqrt2 algorithm code
# The final version will go in the jupyter notebook

# This code uses the Newton-Raphson method to compute
# the roots of a function, which will be manipulated
# to calculate the square root.

# It is manipulated thus: finding the square root
# of 2 is equivalent to finding the roots of the 
# equation f(x) = x^2 - 2


aold = 1
anew = 0
bold = 1
bnew = 0

its = 100


for i in range(0, its):
    anew = aold + 2*bold
    bnew = aold + bold

    aold = anew
    bold = bnew

print(anew // bnew )
print(anew % bnew)

output_string = str(anew // bnew) + "."

anew = (anew % bnew) * 10

for i in range(1, 66):
    output_string += str(anew//bnew)
    anew = (anew % bnew) * 10

    

print(output_string)






#print(a)
#print(a*a)






