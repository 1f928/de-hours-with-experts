#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])

def int_to_digit_array(num): return [int(ch) for ch in str(num)]
def digit_array_to_int(arr): return int("".join(str(n) for n in arr))
    
def next_biggest_number(num):
    digits = int_to_digit_array(num)

    # Reading right-to-left:
    for i in range(len(digits) - 2, -1, -1):

        # Find first digit lower than prior digit
        if (digits[i] < digits[i + 1]):

            # Swap low number with seen higher number closest in value
            # And sort digits below the swap-line before reassembling
            left_digits = digits[:i]
            right_digits = sorted(digits[i:])
            low = digits[i]
            high = [n for n in right_digits if n > low][0]
            right_digits.remove(high)
            
            return digit_array_to_int(left_digits + [high] + right_digits)

    # Fail case
    return -1

if __name__ == "__main__":
    main()



