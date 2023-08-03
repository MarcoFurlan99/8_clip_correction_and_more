# clip correction

As noticed by Sylvain, clipping was excessively distorting the generated datasets, as an example with parameters $(\mu, \sigma) = (10,50)$ around 40% of the samples were clipped. Consequently I adjusted the parameters in such a way that clipping does not distort the data in a meaningful way. In the following [desmos project](https://www.desmos.com/calculator/gcopjnc7t2) I show that with the constraints $64 \leq \mu \leq 192$ and $0 < \sigma \leq 30$ in the worst case <2% of pixels is clipped.

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/images/cclipping_normal_distr.png?raw=true">

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/images/cclipping_normal_distr_value.png?raw=true">
