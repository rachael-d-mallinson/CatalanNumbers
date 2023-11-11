#Rachael Mallinson
#Catalan Numbers Memoized Implementation

#global variable to count the number of multiplications
numberOfMultiplications = 0;

def _IncrementMultiplicationCount():
    """ Function to increment the global variable that counts the number of multiplcations calculated
    """
    global numberOfMultiplications;
    numberOfMultiplications += 1;


#Catalan function------------------------------------------------------
def _CatalanMM(n, c):
    """ Function to find the nth catalan number 
    :param n: number given to calculate
    :param c: array to store memoization results
    """
    if (n == 0):
        return 1;
    if (c[n] != -1):
        return c[n];

    sum = 0;
    for i in range(1, n+1):
        sum += _CatalanMM(i-1, c) * _CatalanMM(n-i, c);
        _IncrementMultiplicationCount();
    c[n] = sum;
    return sum;


#Section to get input and call functions ----------------------------------------------
print("Catalan Numbers Computed -- Memoized.");
while True :
    given = input("Please provide number below\n");
    if (given.isnumeric()):
        n = int(given);
        break;
    else :
        print("Input not valid. Please try again.");


#create array initilized with value -1 since we are using it to compare in code
c = [-1] * (n+1);

num = _CatalanMM(n, c);
print("Catalan Number: ", num);
print("Number of multiplications calculated: ", numberOfMultiplications);
print("--End--");

 ## END OF FILE ##