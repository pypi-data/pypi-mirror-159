from rpy2.robjects import r, globalenv

# Function to calculate the pr
def calc_prime_numbers(number: int) -> list:
    assert number>=1 , f'the number must be between 1 and {number}'
    assert type(number) == int, "the number must be integer"
    globalenv['number'] = number
    code = """
      result <- list()  
      for (j in 2:number) {
      f = 1
      i = 2
      n = j
      while (i <= n / 2) {
        if (n %% i == 0) {
          f = 0
          break
        }
        i = i + 1
      }
      if (f == 1) {
        result <- append(result, n) 
      }
    }
    print(paste(result))
      """
    result = r(code)
    result = [int(x) for x in list(result)]
    return result 


print(calc_prime_numbers(200))
