#!/usr/bin/python3
for alpha_letter in range(97, 123):
    if(alpha_letter != 101) and (alpha_letter != 113):
        print("{:c}".format(alpha_letter), end='')
