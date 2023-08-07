# clip correction

As noticed by Sylvain, clipping was excessively distorting the generated datasets, as an example with parameters $(\mu, \sigma) = (10,50)$ around 40% of the pixels were clipped. Consequently I adjusted the parameters in such a way that clipping does not distort the data in a meaningful way. In the following [desmos project](https://www.desmos.com/calculator/gcopjnc7t2) I set the constraints $64 \leq \mu \leq 192$ and $0 < \sigma \leq 30$.

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/images/clipping_normal_distr.png?raw=true">

In the worst case <2% of pixels is clipped:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/images/clipping_normal_distr_value.png?raw=true">

I therefore readjusted all parameters to respect the constraints $64 \leq \mu \leq 192$ and $0 < \sigma \leq 30$ and rerun the experiments.

You can play around with [this](https://www.desmos.com/calculator/ni6mms7ztn) to verify how the distributions interact with each other with different parameters.



# The 1-800 experiment

Since the code is already done and working, I went for a huge experiment with one source dataset and 800 target dataset. The target datasets have the following parameters:

- $\mu_1 \in \lbrace 64,80,96,112,128,144,160 \rbrace$

- $\mu_2 \in \lbrace \mu_1 + d : d \in \lbrace 24,32,42,55,73,97,128\rbrace \land \mu_1+d \leq 192 \rbrace$

- $\sigma_1 \in \lbrace 6,12,18,24,30 \rbrace$

- $\sigma_2 \in \lbrace 6,12,18,24,30 \rbrace$

This totals to 32 possible combinations of $(\mu_1, \mu_2)$ and 25 possible combinations of $(\sigma_1, \sigma_2)$, totalling 32x25 = 800 target datasets. All parameter combinations respect the constraints above.

The source dataset is chosen to have parameters $(96, 18, 138, 18)$.

It is to be noted that these parameters are relatively much easier than previous experiments: $\min\limits_{\mu_1, \mu_2} (\mu_2 - \mu_1) = 24$ and $\max\limits_{\sigma \in \sigma_1 \cup \sigma_2} \sigma = 30$ [^1].

[^1]: with abuse of notation on $\sigma_1$ and $\sigma_2$.

The usual graphs, before BN adaptation:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/graph_2d.png?raw=true">

After BN adaptation:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/graph_2d_adapted.png?raw=true">

Results without clipping are homogeneous, as S. expected !

New graphs: these are the same values but I graph them wrt $\mu_1, \mu_2$ externally and $\sigma_1, \sigma_2$.

before BN adaptation:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/graph_2d_sigma.png?raw=true">

After BN adaptation:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/graph_2d_adapted_sigma.png?raw=true">

The difference graphs are in the folder [1_800](https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/).


