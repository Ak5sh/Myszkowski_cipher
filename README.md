# Myszkowski Cipher

## Overview

The Myszkowski Cipher is a classical transposition cipher that rearranges characters based on a keyword. Unlike simple columnar transposition, repeated letters in the key are treated specially — columns with the same letter are read together row-wise.

---

## Usage

### Menu Options:

1. Encrypt a message
2. Decrypt a message
3. Exit program

---

### To Encrypt a Message:

* Choose option `1`
* Enter plaintext (no restrictions, spaces allowed)
* Enter a key (alphabets only)

---

### To Decrypt a Message:

* Choose option `2`
* Enter ciphertext
* Enter the same key used during encryption

---

## How Myszkowski Cipher Works

1. A key is chosen (e.g., `banana`)
2. Each letter is assigned a rank:

   * Repeated letters share the same rank
3. Plaintext is written row-wise in a grid
4. Columns are read based on rank:

   * Unique rank → column-wise
   * Repeated rank → row-wise across those columns

---

## Example

Key: `banana`
Ranks: `2 1 3 1 3 1`

Plaintext:

```
HELLOWORLD
```

Matrix:

```
H E L L O W
O R L D X X
```

Ciphertext is generated based on rank ordering.

---

## Example Hashing Function

```python
def example_hash_function(input_string):
    ranks = []
    current_rank = 1

    for i in range(len(input_string)):
        found = False
        for j in range(i):
            if input_string[i] == input_string[j]:
                ranks.append(ranks[j])
                found = True
                break

        if not found:
            ranks.append(current_rank)
            current_rank += 1

    return ranks
```

---

## Custom Hashing Function Notes

* You can modify the `custom_hash_function()` in the code
* Do NOT use built-in sorting functions
* Logic must manually assign ranks
* Same characters → same rank

---

## Input Validation

* Key must contain only alphabets
* Program handles invalid menu choices
* Automatically pads plaintext with 'x' if needed

---

## Prompt

You are a proficient Python developer who specializes in implementing cryptographic algorithms and creating user-friendly applications.
Your expertise lies in designing code that is both efficient and easy to understand, ensuring that users can easily interact with the 
program. Your task is to generate a complete, menu-driven code implementation for the Myszkowski Cipher in Python, which includes both 
encryption and decryption functionalities. Additionally, the code should allow the user to input their own hashing function,
which must be implemented as raw code rather than using built-in functions. The output should be structured as runnable
Python code suitable for execution in Visual Studio Code. It should also include a comprehensive README file that 
explains how to use the program, the principles behind the Myszkowski Cipher,
and instructions for implementing the hashing function. 
--- In the code, ensure that: - The menu options are clearly displayed and easy to navigate. 
- Input validation is implemented to handle incorrect inputs gracefully. 
def example_hash_function(input_string):
    # Your hashing logic here

---

