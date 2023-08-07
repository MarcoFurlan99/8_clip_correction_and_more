# clip correction

As noticed by Sylvain, clipping was excessively distorting the generated datasets, as an example with parameters $(\mu, \sigma) = (10,50)$ around 40% of the pixels were clipped. Consequently I adjusted the parameters in such a way that clipping does not distort the data in a meaningful way. In the following [desmos project](https://www.desmos.com/calculator/gcopjnc7t2) I set the constraints $64 \leq \mu \leq 192$ and $0 < \sigma \leq 30$.

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/images/clipping_normal_distr.png?raw=true">

In the worst case <2% of pixels is clipped:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/images/clipping_normal_distr_value.png?raw=true">

I therefore readjusted all parameters to respect the constraints $64 \leq \mu \leq 192$ and $0 < \sigma \leq 30$ and rerun the experiments.

You can play around with [this](https://www.desmos.com/calculator/ni6mms7ztn) to verify how the distributions interact with each other with different parameters.



# The 1-800 experiment

Since the code is already done and working, I went for a huge experiment with one source dataset and 800 target dataset. The source dataset has parameters $(96, 18, 138, 18)$, which put it at the center of the target datasets essentially. The target datasets have the following parameters:

- $\mu_1 \in \{64,80,96,112,128,144,160\}$

- $\mu_2 \in \{ \mu_1 + d | d \in \{24,32,42,55,73,97,128\} \land \mu_1+d \leq 192\}$

- $\sigma_1 \in \{6,12,18,24,30\}$

- $\sigma_2 \in \{6,12,18,24,30\}$

This totals to 32 possible combinations of $(\mu_1, \mu_2)$ and 25 possible combinations of $(\sigma_1, \sigma_2)$, totalling 32x25 = 800 target datasets. All parameter combinations respect the constraints above.

