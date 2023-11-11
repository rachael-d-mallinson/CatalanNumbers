#Rachael Mallinson
#Catalan Numbers Top-Down Implementation

#global variable to count the number of multiplications
numberOfMultiplications = 0;

def _IncrementMultiplicationCount():
    """ Function to increment the global variable that counts the number of multiplcations calculated
    """
    global numberOfMultiplications;
    numberOfMultiplications += 1;


#Catalan function------------------------------------------------------
def _CatalanTD(n):
    """ Function to find the nth catalan number 
    :param n: number given to calculate
    """
    if (n == 0):
        return 1;
    else:
        sum = 0;
        for i in range(1, n+1):
            sum += (_CatalanTD(i-1) * _CatalanTD(n-i));
            _IncrementMultiplicationCount();
        return sum;


#Section to get input and call functions ----------------------------------------------
print("Catalan Numbers Computed -- Top-Down.");
while True :
    given = input("Please provide number below\n");
    if (given.isnumeric()):
        n = int(given);
        break;
    else :
        print("Input not valid. Please try again.");

num = _CatalanTD(n);
print("Catlan Number: ", num);
print("Number of multiplications calculated: ", numberOfMultiplications);


 ## END OF FILE ##