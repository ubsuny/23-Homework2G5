# Comparing exexcution time for 3 different implementation functions
 ## using time.time()
### Colab
#### for loops:
9.3 micro seconds
#### einsum:
0.7 milli seconds
#### numpy inner and outer built in functions:
0.14 milli seconds

### Jupyter Notebook
#### for loop:
16 micro seconds
#### einsum:
0.017 seconds
#### numpy inner and outer built in functions:
0.015 seconds

## Quantum Lab
#### for loop:
8.8 micro seconds
#### einsum:
56 micro seconds
#### numpy inner and outer built in functions:
0.12 milli seconds


## using tiemit
#### for loop:
2.69 µs ± 11.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
so for the run, it shall be 0.269 seconds
#### einsum:
**for inner product**: 2.77 µs ± 17.2 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
so for the run it shall be 0.277 seconds per run
**for outer product**: 2.96 µs ± 20.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
it shall be 0.296 seconds per run
#### numpy inner and outer built in functions:
**for inner product**: 2.36 µs ± 10.5 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
for run, it will be 0.236 seconds
**for outer product**:3.29 µs ± 8.58 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
for run, it will be 0.329 seconds

# conclusion:
The fastest platform among all is the Quantum lab.
The fastest function to calculate the inner and outer product as it is clear from the time results we got is the for loops, followed by either numpy inner and outer functions or numpy einsum
# Histograms to illustrate the comparison 


![output_2_0](https://github.com/yasmensarhan27/23-Homework2G5/assets/38404107/c5b681f8-88e8-4a52-9920-ccd294c41e9c)
![output_1_0](https://github.com/yasmensarhan27/23-Homework2G5/assets/38404107/47c63fa1-99ce-4df2-ac21-db37eb417ba2)
![output_0_0](https://github.com/yasmensarhan27/23-Homework2G5/assets/38404107/1d7ff0c8-ae56-45ac-b4ec-35b88baebca3)
![output_3_0](https://github.com/yasmensarhan27/23-Homework2G5/assets/38404107/e7e301d6-e72f-4a1d-afb1-11764869bd9c)
