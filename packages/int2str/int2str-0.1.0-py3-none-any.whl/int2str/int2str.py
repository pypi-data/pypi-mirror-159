

#TODO: this function can be package inside a class for future upgrades.
numbers_alphabet = {
    0: 'zero', 
    1: 'one', 
    2: 'two',
    3: 'three', 
    4: 'four', 
    5: 'five', 
    6: 'six', 
    7: 'seven', 
    8: 'eight',
    9: 'nine', 
    10: 'ten',
    11: 'eleven', 
    12: 'twelve',
    13: 'thirteen', 
    14: 'fourteen',
    15: 'fifteen', 
    16: 'sixteen', 
    17: 'seventeen', 
    18: 'eighteen',
    19: 'nineteen', 
    20: 'twenty',
    30: 'thirty', 
    40: 'forty', 
    50: 'fifty', 
    60: 'sixty',
    70: 'seventy', 
    80: 'eighty', 
    90: 'ninety'
}


BASE_HUNDRED = 100
BASE_THOUSAND = BASE_HUNDRED * 10
DIGIT_GROUP_BASE = 1_000


BASE_MILLION = BASE_THOUSAND * DIGIT_GROUP_BASE
BASE_BILLION = BASE_MILLION * DIGIT_GROUP_BASE
BASE_TRILLION = BASE_BILLION * DIGIT_GROUP_BASE
BASE_QUADRILLION = BASE_TRILLION * DIGIT_GROUP_BASE
BASE_QUINTILLION = BASE_QUADRILLION * DIGIT_GROUP_BASE


def convert_big_numbers(number:int) -> str:
    """
        description: This utility function handled big positive integer numbers.
    """
        
    if number < BASE_THOUSAND:
        base, base_conector, linker_conector = BASE_HUNDRED, 'hundred', 'hundred and'

    elif number < BASE_MILLION:
        base, base_conector, linker_conector = BASE_THOUSAND, 'thousand', 'thousand,'

    elif number < BASE_BILLION:
        base, base_conector, linker_conector = BASE_MILLION, 'million', 'million'

    elif number < BASE_TRILLION:
        base, base_conector, linker_conector = BASE_BILLION, 'billion', 'billion'

    elif number < BASE_QUADRILLION:
        base, base_conector, linker_conector = BASE_TRILLION, 'trillion', 'trillion' 

    elif number < BASE_QUINTILLION:
        base, base_conector, linker_conector = BASE_QUADRILLION, 'quadrillion', 'quadrillion'

    elif number == BASE_QUINTILLION:
        base, base_conector, linker_conector = BASE_QUINTILLION, 'quintillion', 'quintillion'
        
    else:
        raise ValueError("Your number is too big!, to be handle by this version.")


    divisor:int = number // base
    module:int  = number % base 


    #call the function recursively based on the module result
    if module == 0:
        return f'{int2str(divisor)} {base_conector}'
    else:
        return f'{int2str(divisor)} {linker_conector} {int2str(module)}'
    

def int2str(number: int ) -> str:
    """
       Shows the string representation of a given positive integer number (N)


       :param number: number to be represented as string.
       :type number: int


       :return: string represetation of the given positive integer
       :rtype: str 
    """

    if isinstance(number, int) == False :
        raise ValueError("Type of input is not integer! Please enter a valid integer number  (eg. \'0,...,1_000_000_000_000_000_000)\')")
    elif number < 0:
        raise ValueError("This library only works with positive integers! (eg. \'0,...,1_000_000_000_000_000_000)\')")


    if number < 20:
        return numbers_alphabet[number]

    if number < 100:

        integer_base, digit = number // 10, number % 10

        if digit == 0:
            return numbers_alphabet[number]

        else:
            decimal_base = integer_base * 10
            return f"{numbers_alphabet[decimal_base]}-{numbers_alphabet[digit]}"
    else:
        return convert_big_numbers(number)
        
