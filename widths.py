estim1 = [
0.1349,0.4495,0.2812,0.3313,0.2591,0.2967,0.2151,0.2117,0.2970
0.8744,0.5780,0.5756,0.5187,0.3942,0.3873,
0.4523,0.4303,0.4091,0.3832,0.3166,0.3688,
0.2346,0.1723,0.1670,0.2607,0.2537,0.1811,0.1652,0.2511
]


real1 = [
0.0497,0.1942,0.2583,0.3167,0.1644,0.2788,0.1540,0.1707,0.2766
0.7998,0.4229,0.5062,0.4359,0.2620,0.2820,
0.3772,0.3502,0.3237,0.2300,0.2032,0.2745,
0.2219,0.1289,0.1227,0.2581,0.2529,0.1407,0.1122,0.2446
]

diff1 = estim1-real1
perc1 = diff1/real1
print(perc1.mean(), perc1.min(), perc1.max())

comb_real1 = [
0.3026,0.2547,0.2584,0.2760,0.5266,
0.4723,0.4763,0.4133,
0.3834,0.3522,0.3373,0.3552,0.3466,
0.1897,0.1905,0.2580,0.2529,0.1945,0.1943,0.2217]

comb_cqr1 = [
0.3225,0.2861,0.2860,0.2965,0.6345,
0.5346,0.5439,0.4943,
0.4385,0.4242,0.4104,0.4344,0.4277,
0.2085,0.2085,0.2605,0.2537,0.2141,0.2124,0.2306]

comb_min1 = [
0.3230,0.2747,0.2764,0.2938,0.6432,
0.5196,0.5334,0.4708,
0.4293,0.4023,0.3937,0.4165,0.4003,
0.2060,0.2069,0.2606,0.2546,0.2093,0.2099,0.2293]

comb_union1 = [
0.3169,0.2815,0.2850,0.3336,0.6308,
0.5884,0.5384,0.5289,
0.4864,0.4674,0.4595,0.4295,0.4468,
0.2271,0.2240,0.2795,0.2789,0.2341,0.2215,0.2428]