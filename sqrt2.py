# sqrt2 function definition, calculates sqrt(2)
# through long division and returns a string 
# with the digits of sqrt(2). sqrt2 takes in its, 
# which is number of iterations of
# the continued fractions recursive algorithm
# and prec which indicates to how many decimal
# places the string with the digits of sqrt(2)
# to be returned has
def sqrt2(its, prec):

    # pold is the numerator at previous step, pnew is numerator at next step
    pold = 1
    pnew = 0

    # qold is the denominator at previous step, qnew is denominator at next step
    qold = 1
    qnew = 0

    # This calculates an approximation of sqrt(2) as a rational number
    # with pnew and pold as numerators (in the next and previous step
    # respectively) and qnew and qold as denominators (in the next and 
    # previous steps respectively) for its iterations 
    for i in range(0, its):

        # This is the recursion algorithm, derived from
        # the formula for continued fractions
        pnew = pold + 2*qold
        qnew = pold + qold

        # Make the new numerator and denominator
        # equal the old numerator and denominator
        # for the next step in the loop
        pold = pnew
        qold = qnew

    # This appends the first digit of sqrt(2)
    # to output_string (the string to be
    # returned)
    output_string = str(pnew // qnew) + "."

    # This is the first step in the long division algorithm
    # pnew is set to the remainder of pnew and qnew after
    # division and multipled by ten for the first decimal
    # place
    pnew = (pnew % qnew) * 10

    # This performs the long division algorithm for each decimal place
    # (defined by prec) and appends the digits of sqrt(2) 
    # digit by digit to the output_string, which is returned 
    # at the end of the function
    for i in range(1, prec+1):
        output_string += str(pnew//qnew)
        pnew = (pnew % qnew) * 10

    # This returns the string, which has prec decimal places
    # of sqrt(2)
    return output_string