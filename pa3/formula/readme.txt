FORMULA:
  Takes a single integer as an argument with interface formula <power>. This argument is then
  used as the exponent, n, in the formula (1+x)^n, which is then expanded and printed.

  functions:
    nCr.h:
      Factorial: Takes a single integer argument and returns it's factorial value in integer form.
                 Note that larger numbers will not work in this function as they may be too large
                 for an integer variable. The function is defined externally in assembly in nCr.s.

      nCr: Takes two integer arguments, n and r, and returns an integer calculated by n!/(r!(n-r)!).
           The factorial values are defined with calls to the Factorial function defined in nCr.h.
           It is defined externally in assembly in nCr.s.
           
    formula.h:
      usage: A void function that simply prints the usage interface (formula <power>).

      charDecimalToIntDecimal: Takes a char pointer string and returns it's numeric form. Note that
                               the string must contain only digits to work (and the number must be
                               positive).
