# Tool 3: Password Cracking Suite
Overview

## The Password Cracking Suite is a comprehensive toolset for performing brute-force and dictionary attacks on hashed passwords. It supports various hashing algorithms and utilizes GPU acceleration for faster cracking.
Features

    Hash Identification: Automatically identify the hashing algorithm used.
    Brute-Force Attack: Perform brute-force attacks with customizable character sets.
    Dictionary Attack: Use wordlists to perform dictionary attacks.
    Rainbow Table Attack: Utilize precomputed rainbow tables for efficient cracking.
    GPU Acceleration: Leverage GPU power for faster password cracking.

Usage
bash

## Clone the repository
git clone https://github.com/hak193/Password-Cracking-Suite
cd password-cracking-suite

### Install dependencies
pip install -r requirements.txt

## Run the tool
python crack.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --method dictionary --wordlist rockyou.txt

Example Output
Code

Hash: 5f4dcc3b5aa765d61d8327deb882cf99
Identified algorithm: MD5

Starting dictionary attack...
Cracked password: password

Time taken: 5 seconds
