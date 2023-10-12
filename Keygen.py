import random
import sys

# argument handling

if len(sys.argv) > 1 and sys.argv[1].isnumeric() == True:
    repeat = int(sys.argv[1])
else:
    if len(sys.argv) == 1:
       print("No argument given.")
       repeat = None

# no arguments?

if repeat == None:
    repeat = (input("How many keys do you want to generate? (press enter for 1 key) "))
    if repeat == "":
        repeat = 1
    elif repeat.isnumeric() == True:
        repeat = int(repeat)
    elif repeat == "weed":
        print("06900-OEM-0694207-80085")
        exit()
    else: 
        while repeat.isnumeric() == False:
            print("Please enter a number!")
            repeat = (input("How many keys do you want to generate? "))
            repeat = repeat
        repeat = int(repeat)

# making the actual key

def keygen(): 
    # define var
    sum = 1 #i made the default value as 1 so the while loop can run.
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
        pkey_div7 = random.randint(1, 999999)       ##AND pkey_div7
        pkey_div7 = str(pkey_div7)
        if len(pkey_div7) < 6:
            pkey_div7 = pkey_div7.zfill(6)          ##dumbass learns about zfill
        for i in pkey_div7:
            sum += int(i)

    print(f"{pkey_date}{pkey_year}-OEM-0{pkey_div7}-{pkey_end5}")
    

# print the key

print(f"Printing {repeat} keys.\n")

for i in range(repeat):
    keygen()


