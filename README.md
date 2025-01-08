# Tool 3: Password Cracking Suite
Overview

## The Password Cracking Suite is a comprehensive toolset for performing brute-force and dictionary attacks on hashed passwords. It supports various hashing algorithms and utilizes GPU acceleration for faster cracking.
Features

    Hash Identification: Automatically identify the hashing algorithm used.
    Brute-Force Attack: Perform brute-force attacks with customizable character sets.
    Dictionary Attack: Use wordlists to perform dictionary attacks.
    Rainbow Table Attack: Utilize precomputed rainbow tables for efficient cracking.
    GPU Acceleration: Leverage GPU power for faster password cracking.


# Installation and usage instructions for the Password Cracking Suite, including the steps to create a rainbow table and use GPU acceleration with CUDA.

### Installation Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/hak193/Password-Cracking-Suite
    cd Password-Cracking-Suite
    ```

2. **Create and Populate `requirements.txt`**

    Create a file named `requirements.txt` in the root directory with the following content:

    ```plaintext
    numpy
    pandas
    scipy
    tensorflow
    pycuda
    ```

3. **Install Dependencies**

    Use the following command to install the dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Install CUDA Toolkit (for GPU Acceleration)**

    Follow the instructions on NVIDIA's website to download and install the CUDA toolkit appropriate for your system: [CUDA Toolkit Download](https://developer.nvidia.com/cuda-downloads)

### Usage Instructions

1. **Create a Rainbow Table**

    Use the following script to create a rainbow table from a wordlist file (e.g., `rockyou.txt`):

    ```python
    import hashlib

    def create_rainbow_table(wordlist_file, output_file):
        with open(wordlist_file, 'r') as infile, open(output_file, 'w') as outfile:
            for word in infile:
                word = word.strip()
                hash = hashlib.md5(word.encode()).hexdigest()
                outfile.write(f"{hash}:{word}\n")

    if __name__ == "__main__":
        create_rainbow_table('rockyou.txt', 'rainbow_table.txt')
    ```

    Save this script as `create_rainbow_table.py` and run it:

    ```bash
    python create_rainbow_table.py
    ```

2. **Run the Password Cracking Suite**

    Here is an example of how to run the `crack.py` script with different methods:

    **Dictionary Attack:**

    ```bash
    python crack.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --method dictionary --wordlist rockyou.txt
    ```

    **Brute-Force Attack:**

    ```bash
    python crack.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --method brute-force
    ```

    **Rainbow Table Attack:**

    ```bash
    python crack.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --method rainbow --rainbow rainbow_table.txt
    ```

    **GPU Accelerated Attack:**

    ```bash
    python crack.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --method gpu
    ```

### Example Output

Example output for a dictionary attack:

```plaintext
Hash: 5f4dcc3b5aa765d61d8327deb882cf99
Identified algorithm: MD5

Starting dictionary attack...
Cracked password: password

Time taken: 5 seconds
```

With these updated installation and usage instructions, users should be able to easily set up and use the Password Cracking Suite, including creating rainbow tables and leveraging GPU acceleration with CUDA.
