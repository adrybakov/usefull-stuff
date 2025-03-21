# MIT License

# Copyright (c) 2025 Andrey Rybakov (rybakov.ad@icloud.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
from argparse import ArgumentParser
from multiprocessing import Pool, cpu_count


def wait_some_do_some(input1, input2):

    time.sleep(1)

    return input1 + input2


def main(number_processors):

    inputs1 = [i for i in range(40)]
    inputs2 = [i for i in range(40)]
    start_time = time.time()
    if number_processors == 1:
        outputs = list(map(wait_some_do_some, inputs1, inputs2))
    else:
        with Pool(number_processors) as p:
            outputs = p.starmap(
                wait_some_do_some,
                zip(inputs1, inputs2),
            )

    execution_time = time.time() - start_time

    print(
        f"Execution time : {execution_time:5.2f} seconds with {number_processors} processors."
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-np", "--number-processors", type=int, help="Number of processors"
    )
    args = parser.parse_args()

    print(f"Available cpus : {cpu_count()}")
    for np in range(1, 11):
        main(np)


# user@host ~  $ python test.py
      
# Available cpus : 4
# Execution time : 40.12 seconds with 1 processors.
# Execution time : 20.20 seconds with 2 processors.
# Execution time : 16.18 seconds with 3 processors.
# Execution time : 12.15 seconds with 4 processors.
# Execution time :  8.27 seconds with 5 processors.
# Execution time :  8.22 seconds with 6 processors.
# Execution time :  6.26 seconds with 7 processors.
# Execution time :  6.29 seconds with 8 processors.
# Execution time :  6.32 seconds with 9 processors.
# Execution time :  4.36 seconds with 10 processors.
