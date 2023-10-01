import random
import sys

if len(sys.argv) > 1 and sys.argv[1].isnumeric() == True:
    repeats = int(sys.argv[1])
else:
    if sys.argv[1].isnumeric() == False:
        print("Invalid argument.")
        repeats = None
    else: 
        print("No argument given.")
        repeats = None

if repeats == None:
    repeats = (input("How many keys do you want to generate? "))
    while repeats.isnumeric() == False:
        print("Please enter a number!")
        repeats = (input("How many keys do you want to generate? "))
    repeats = int(repeats)

def keygen():      # the rng part, which is actually the only thing that matters lmfao
    # define var
    sum = 1 #i made the default value as 1 so the while loop can run. not efficient but how much is my losses
    ## ini semua buat rng
    pkey_end5 = random.randint(10000, 99999)
    pkey_date = random.randint(1, 366)
    if pkey_date < 100:
        pkey_date = str(pkey_date)
        pkey_date = pkey_date.zfill(3)
    pkey_year = random.randint(95, 103)
    if pkey_year >= 100:
        pkey_year = str(pkey_year)
        pkey_year = pkey_year[1:]


    # make proper pkey_div7. if sum is not divisible by 7, rng new pkey_div7 and check again
    while sum % 7 != 0:
        sum = 0                                     ##this both resets sum
        pkey_div7 = random.randint(10000, 99999)    ##AND pkey_div7
        for i in str(pkey_div7):
            sum += int(i)

    print(f"{pkey_date}{pkey_year}-OEM-00{pkey_div7}-{pkey_end5}")
    

for i in range(repeats):
    keygen()


