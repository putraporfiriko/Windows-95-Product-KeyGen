# key generating part
def keygen(): 
    # define var
    sum = 1 #i made the default value as 1 so the while loop can run.
    ## ini semua buat rng
    pkey_end5 = random.randint(1, 99999)
    if pkey_end5 < 10000:
        pkey_end5 = str(pkey_end5)
        pkey_end5 = pkey_end5.zfill(5)
    pkey_date = random.randint(1, 366)
    if pkey_date < 100:                         # syarat 1: percabangan
        pkey_date = str(pkey_date)
        pkey_date = pkey_date.zfill(3)
    pkey_year = random.randint(95, 103)
    if pkey_year >= 100:                        # percabangan 2
        pkey_year = str(pkey_year)
        pkey_year = pkey_year[1:]


    # make proper pkey_div7. if sum is not divisible by 7, rng new pkey_div7 and check again
    while sum % 7 != 0:                             # syarat 2: looping
        sum = 0                                     ##this both resets sum
        pkey_div7 = random.randint(1, 999999)       ##AND pkey_div7
        pkey_div7 = str(pkey_div7)
        if len(pkey_div7) < 6:
            pkey_div7 = pkey_div7.zfill(6)          ##dumbass learns about zfill
        for i in pkey_div7:
            sum += int(i)

    print(f"{pkey_date}{pkey_year}-OEM-0{pkey_div7}-{pkey_end5}") # syarat 3: i/o

# argument handling and easter egg for funnies
def noargs():
    global repeat      # genuinely just learnt about this after i published to a repo
    repeat = input("How many keys do you want to generate? (press enter for 1 key) ")
    if repeat == "":                             #syarat 1: percabangan
        repeat = 1
    elif repeat.isnumeric() == True:
        repeat = int(repeat)
    elif repeat == "weed":
        print("great choice.\n")
        print("06900-OEM-0694207-80085")        #"Highly mature people may want to forgo simplicity..."
        exit()
    else:
        while repeat.isnumeric() == False:
            print("Invalid Input!")
            repeat = input("How many keys do you want to generate? (press enter for 1 key) ")
            if repeat == "":
                repeat = 1
                return
        
# main function. handles argchecks and handoff to keygen() or noargs(), then to keygen()
def main():
    global repeat
    if len(sys.argv) > 1 and sys.argv[1].isnumeric() == True: # sys.arg check. no arguments? go to noargs()
        repeat = int(sys.argv[1])           
    elif len(sys.argv) == 1:                                  # syarat 1: percabangan
        print("No argument given.")
        noargs()
    elif len(sys.argv) > 1 and sys.argv[1].isnumeric() == False:
        print("Invalid argument.")                            # syarat 3: i/o
        noargs()
    print(f"Printing {repeat} keys.\n")
    for i in range(int(repeat)):                              # syarat 2: perulangan
        keygen()

if __name__ == "__main__":
    import random, sys
    main()

