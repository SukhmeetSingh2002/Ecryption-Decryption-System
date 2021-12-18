# Ecryption Decryption System 
This is a randomized encryption system made using a **LFSR** (Linear Feedback Shift Register) which encrptes the data given by user and decrptes a data encrypted by it.    

## Functionality 
It can do the following tasks which uses a random number generator (**LFSR** : Linear Feedback Shift Register) implemented in `Verilog`
- [x] It can encrypt the data given by the user and decrypts the encrypted data.
- [x] It can decrypt data encrypted by it.
- [x] It can generate a secure password.

> Currently input data supports `(A-Z,a-z,0-9,_, )`,If input is from file it also supports `("\n",",",".")`
## Usage 
To use, run the following command
```
python main.py
```

- `main.py` will ask to *encrypt*, *decrypt* or *generate* a secure password then it runs the `verilog` modules.
-  It takes input from a `file` but if input is small it can take input from `console` as well 
-  It takes `input file` and store the *encrypted* or *decrypted* data in a `text file` specified by the user. 

---

## Brief Implementaion Details  

### Encryption
- Data is grouped in a lenght of 10 characters
- Each character of data is converted to `6 bit` binary representaion making a group of `60 bit`
- `bit_ran_6` and `bit_ran_11` module keeps generating random numbers of widht *6* and *11* bit at each *posedge* of clock.
- Based on these random numbers computation is done on the input (`60-bit`) and output is stored in `78-bit` binary number.
- `78-bit` output is divided in `6-bit` numbers and each `6-bit` number is converted back into characters
- These characters are taken together and written in a file specified by the user

### Decryption
- Data is grouped in a length of 13 characters
- Two characters extra help to decrypt it using the reverse computations 
- The decrypt data is written in a file specified by the user
### Password Generation
- `bit_ran_6` and `bit_ran_11` are used to generate a random password of 10 characters.

---

## Contributors

| Name            | Entry Number |
| --------------- | ------------ |
| Sukhmeet Singh | 2020CSB1129  |
| Sourabh Sanganwar | 2020CSB1121  |
