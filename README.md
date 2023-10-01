# Windows-95-Product-KeyGen
Basic Windows 95 Key generator written in Python/

how to use:
`python ./keygen.py {arguments (optional)}`

## Explanation

The Windows 95 OEM product key uses a certain algorithm to determine if the provided key is valid. The OEM key has 4 segments in its string of keys:

![The Windows 95 OEM Key input menu. There are 4 sections, first section being 5 character long, second section being a fixed string "OEM", third being a 7 character long section, and the last section being 5 character long.](https://github.com/putraporfiriko/Windows-95-Product-KeyGen/blob/main/assets/ProductKey.png)

From the key input menu above, we can dissect the key again into the following form: `XXXYY-OEM-ZZZZZZZ-AAAAA`

each X, Y, and Z represents a different thing in making the product key. For example, we're gonna take the key 
`19203-OEM-0063793-47815` as an example.

- XXX represents the date on which the key was generated. In this example, we have the numbers 192. This means that the key was generated on the 192nd day of the year, which is July 11th.

- YY represents the year on which the key was generated. The year can range between 95 (representing 1995) and 03 (representing 2003). In this example, we have the number 03, which means that the key was generated in 2003.

- ZZZZZZZ represents a unique identifier for the key. This part of the key that determines if the key is valid or no. Determining if this string is valid or no can be done by adding up all the numbers in the string. If the sum of the numbers is divisible by 7, then the key is valid. Another requirement for the key to be valid is that the first number in this sequence must be a 0. For this example, we have the string 0063793. Adding up all the numbers in this string, we get 28. 28 is divisible by 7, so this key is valid.

- The final 5 characters doesn't have a check for validity, so we can technically put any number we want, as long as it's 5 characters long.
