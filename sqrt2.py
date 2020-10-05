# This is the raw file for the sqrt2 algorithm code
# The final version will go in the jupyter notebook

# This code uses the Newton-Raphson method to compute
# the roots of a function, which will be manipulated
# to calculate the square root.

# It is manipulated thus: finding the square root
# of 2 is equivalent to finding the roots of the 
# equation f(x) = x^2 - 2



output_string = "1."

b = 0
c= 1

a = 1
tmp = 1 

while(tmp*tmp <= 2):
    tmp = a + (b * 10**(-c))
    b +=1
    
output_string += str(b-2)
print(output_string)

a = tmp - 1 * 10**(-c)
b = 0
c += 1
tmp = 1

#print(a)
#print(a*a)

while(tmp*tmp <= 2):
    tmp = a + (b * 10**(-c))
    b +=1

output_string += str(b-2)
print(output_string)

a = tmp - 1 * 10**(-c)
b = 0
c += 1
tmp = 1

print(a)
print(a*a)

while(tmp*tmp <= 2):
    tmp = a + (b * 10**(-c))
    b +=1

output_string += str(b-2)
print(output_string)

a = tmp - 1 * 10**(-c)
b = 0
c += 1

