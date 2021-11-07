# Tasks completed
All modules are created and width of all the bits are defined and module hierarchy is also well defined.

# Ongoing Tasks 
Currently making random generator of 6 bit and 11 bit is ongoing.

# Tasks Remaining 
Taking a file as input and improving password generator.

Currently module hierarchy is as follows:

TestBench
├── Solver
├── Decrypter
│   ├── decrypt_function_1
│   ├── decrypt_function_2
│   ├── decrypt_function_3
│   └── decrypt_function_4
├── Encrypter
│   ├── bit_rand_6
│   ├── bit_rand_11
│   ├── encrypt_function_1
│   ├── encrypt_function_2
│   ├── encrypt_function_3
│   └── encrypt_function_4
└── password_gen
    ├── bit_rand_6
    ├── Gen_1
    │   └── bit_rand_11
    ├── Gen_2
    │   └── bit_rand_11
    ├── Gen_3
    │   └── bit_rand_11
    └── Gen_4
        └── bit_rand_11