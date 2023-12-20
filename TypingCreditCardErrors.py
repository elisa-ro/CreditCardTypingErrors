#usage: python TypingCreditCardErrors.py <Credit Card Number>

import sys
import os

credit_card_number = sys.argv[1]


def LuhnAlgorithm(credit_card_number):
    sum = 0
    doubleBoolean = True
    for i in credit_card_number:
        if doubleBoolean:
            if (int(i)*2) > 9:
                for j in str(int(i)*2):
                    sum += int(j)
            else:
                sum += int(i)*2
            doubleBoolean = False
        else:
            sum+= int(i)
            doubleBoolean = True

    return (str(sum)[-1] == '0')

print(LuhnAlgorithm(credit_card_number))