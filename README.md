[![License](https://img.shields.io/github/license/Quantizr/RandomStreamAlgorithm?style=for-the-badge)](https://github.com/Quantizr/RandomStreamAlgorithm/blob/master/LICENSE)

# Random-Stream Algorithm
A Python implementation of the Random-Stream Algorithm from Zhou and Bruck's 
Paper "Streaming Algorithms for Optimal Generation of Random Bits." 

[arXiv:1209.0730](https://arxiv.org/abs/1209.0730)


I originally wrote this implementation as part of my science fair project,
which was to create a low cost quantum random number generator (QRNG). The
original code received a heavily biased input stream from a serial port, where
the input values were actually the amount of 0s between the amount of 1s.
This wasn't a generally applicable form, and, seeing as there was no other
implementation of the Random-Stream algorithm online, I thought it might be
useful to others to rewrite the relevant portions and post them here.

## Introduction

For a complete understanding of the algorithm, read the original paper here:
[Streaming Algorithms for Optimal Generation of Random Bits](https://arxiv.org/abs/1209.0730)

As a quick summary, what this algorithm does is receive a binary input stream
of unknown bias and output a stream of unbiased binary values. (Bias in this
case would be an uneven amount of 0s and 1s.)

Traditionally, Von Neumann's algorithm is used to do this, however, Von
Neuman's algorthm discards and wastes a large number of values, especially
for heavily biased input streams.

Other algorithms, such as Peres's and Elias's extract maximum entropy
(randomness) from an input, however the input for their algorithms must be a
fixed number of input bits and not a streaming input. The Random-Stream
algorithm allows for a streaming output, while simultaneously approaching
the upper bound in extracting entropy. This may be useful for things such as
random number generators where a streaming, unbiased output is needed.

## Example Usage
The code should be relatively straight-forward. The code iterates through
a string, "inputFlips" as if it were a streaming input, processing each value
one-by-one. Because the paper uses input values of "H" and "T", representing
H(eads) and T(ails), the code also does so.

If you would like to use a binary input instead of "H" and "T", simply replace
```python
inputFlips = "HTTTHT"

for value in inputFlips: 
    RandomStream(root, value, depth)
```

with 

```python
inputBinary = "011101"
        
for binary in inputBinary: 
    if binary == "0": value = "H"
    elif binary == "1": value = "T" 
    RandomStream(root, value, depth)
```

If you would like to use a different input, simply change the value of
"inputFlips". The default value of "HTTTHT" is the value used in Ex. 1 and
Fig. 1 in the paper.

You can also change the maximum depth of the binary status tree used by
the algorithm by changing the value of "depth" from the default value of -1,
which allows for infinite depth.

There are two files, RandomStream.py and RandomStreamWithVisualization.py.
RandomStream.py simply prints the output stream to the console, while
RandomStreamWithVisualization.py shows each step, the output (if any) after
each step, along with a visualization.

Below are the example outputs for the two files, based on the input "HTTTHT",
which is used in the Ex. 1 and Fig. 1 of the paper.

#### RandomStream.py Example Output
inputFlips = "HTTTHT", depth = -1

Output:
```
11
```

#### RandomStreamWithVisualization.py Example Output
inputFlips = "HTTTHT", depth = -1

Output:
```
Step: 1
psi

Step: 2
H

Step: 3
 1_  
/  \ 
H psi

Step: 4
Output: 1
 T_  
/  \ 
H psi

Step: 5
  ___psi 
 /      \
 1_     T
/  \     
H psi    

Step: 6
  ___H 
 /    \
 1_   T
/  \   
H psi  

Step: 7
Output: 1
  ___1 
 /    \
 H_   T
/  \   
H psi  
```