**Table of contents**

- clip correction

- The 1-800 experiment

- The 1-90 experiment without skip-connections

- Ideas

# clip correction

As noticed by Sylvain, clipping was excessively distorting the generated datasets, as an example with parameters $(\mu, \sigma) = (10,50)$ around 40% of the pixels were clipped. Consequently I adjusted the parameters in such a way that clipping does not distort the data in a meaningful way. In the following [desmos project](https://www.desmos.com/calculator/gcopjnc7t2) I set the constraints $64 \leq \mu \leq 192$ and $0 < \sigma \leq 30$.

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/images/clipping_normal_distr.png?raw=true">

In the worst case <2% of pixels is clipped:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/images/clipping_normal_distr_value.png?raw=true">

I therefore readjusted all parameters to respect the constraints $64 \leq \mu \leq 192$ and $0 < \sigma \leq 30$ and rerun the experiments.

You can play around with [this](https://www.desmos.com/calculator/ni6mms7ztn) to verify how the distributions interact with each other with different parameters.



# The 1-800 experiment

## parameters

Since the code is already done and working, I went for a huge experiment with one source dataset and 800 target dataset. The objective of this is closing the experimentation with the four parameters $(\mu_1, \sigma_1, \mu_2, \sigma_2)$ with a single, complete experiment which encapsulates all possible cases.

The target datasets have the following parameters:

- $\mu_1 \in \lbrace 64,80,96,112,128,144,160 \rbrace$

- $\mu_2 \in \lbrace \mu_1 + d : d \in \lbrace 24,32,42,55,73,97,128\rbrace \land \mu_1+d \leq 192 \rbrace$

- $\sigma_1 \in \lbrace 6,12,18,24,30 \rbrace$

- $\sigma_2 \in \lbrace 6,12,18,24,30 \rbrace$

This totals to 32 possible combinations of $(\mu_1, \mu_2)$ and 25 possible combinations of $(\sigma_1, \sigma_2)$, totalling 32x25 = 800 target datasets. All parameter combinations respect the constraints above.

The source dataset is chosen to have parameters $(96, 18, 138, 18)$.

It is to be noted that these parameters are relatively much easier than previous experiments: $\min\limits_{\mu_1, \mu_2} (\mu_2 - \mu_1) = 24$ and $\max\limits_{\sigma \in \sigma_1 \cup \sigma_2} \sigma = 30$ [^1].

[^1]: with abuse of notation on $\sigma_1$ and $\sigma_2$.

## Training history

Unable to graph it because of the code crashing at every training but I checked by eye that it had the classic downward trend (no irregularities in the training).

## Results

The usual graphs, before BN adaptation:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/graph_2d.png?raw=true">

After BN adaptation:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/graph_2d_adapted.png?raw=true">

Results without clipping are homogeneous, as S. expected !

The following are *new graphs*: they have the same values as above but arranged differently, w.r.t. $\mu_1, \mu_2$ externally and $\sigma_1, \sigma_2$ internally.

before BN adaptation:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/graph_2d_sigma.png?raw=true">

After BN adaptation:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/graph_2d_adapted_sigma.png?raw=true">

The difference graphs are in the folder [1_800](https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/).

## Wasserstein

I plotted only the 0th latent space. Didn't get the 1st and 2nd latent spaces for loss of hope on my part to find a meaningful pattern after seeing the 0th; the 3rd and 4th were shown to be too sparse to give reliable results with the Wasserstein in the [previous report](https://github.com/MarcoFurlan99/7_Wasserstein_computation_and_more).

Nonetheless, there seems to be some sort of hyperbola-shaped pattern which I don't know how to interpret but is kinda cool to see.

**Raw Wasserstein**

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/Prometheus_0.png?raw=true">

**Target adapted Wasserstein** (as in Luc's experiment in [your paper](https://publis.icube.unistra.fr/docs/17711/ISBI_paper_559.pdf)).

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/Prometheus_TA_0.png?raw=true">

## Observations

- answer to [previous reunion](https://github.com/MarcoFurlan99/7_Wasserstein_computation_and_more) "extra": bc parameters $\mu$ and $\text{Var}$ can be very different but ending results can be really good, as seen in the example with different brightnesses. The point of taking the latent spaces is that we expect the features to be similar after the BN correction.

- Results change in a continuous way w.r.t. to the parameters $\mu$ and $\sigma$, which means clipping was to blame likely for discontinuous behaviour and for the upper-triangle and lower-triangle patterns of the experiment in the [results of previous reunion](https://github.com/MarcoFurlan99/7_Wasserstein_computation_and_more).

- I can't really conclude anything meaningful on the Wasserstein.

## extra: trying to predict performance with the original parameters

An accurate prediction of IoU_adapted with the original parameters $(\mu_1, \sigma_1, \mu_2, \sigma_2)$ would be a good starting point (essentially in my opinion if we can't do this there's really no need to try to do all the messy process to get the latent spaces and interpret them as multidimensional distributions and finding a distance between the two ecc ecc).

It's something I've been trying to do since forever and failed but in this experiment the regularity that arised from preventing the clipping gave me better hope.

Let us call $N(\mu_{1s}, \sigma_{1s})$ and $N(\mu_{2s}, \sigma_{2s})$ the distributions of background and mask on the source dataset, and similarly for the target dataset $N(\mu_{1t}, \sigma_{1t})$ and $N(\mu_{2t}, \sigma_{2t})$.

I tried computing different distance measures between the two target distributions $N(\mu_{1t}, \sigma_{1t})$ and $N(\mu_{2t}, \sigma_{2t})$, essentially ignoring the source parameters because the source is the same for all target dataset [^2], here are the results:

[^2]: ofc there should be a way to use it! But anyways this entire subsection is not really the point of my internship it's more of a sidenote.

**coefficient of overlapping**

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/distance_graphs/coefficient_of_overlapping.png?raw=true">

**log_Wasserstein**

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/distance_graphs/log_Wasserstein.png?raw=true">

**log_Wasserstein_sourcenorm**

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/distance_graphs/log_Wasserstein_sourcenorm.png?raw=true">

**log_Wasserstein_targetnorm**

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_800/distance_graphs/log_Wasserstein_targetnorm.png?raw=true">

So there are definitely patterns arising but also a good amount of outliers. If someone has ideas on how to include the source parameters as well it may be an interesting extra result to include.

# The 1-90 experiment without skip-connections

## How did I remove skip connections?

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_90/unet_without_skc.png?raw=true">

I did the simplest thing possible code-wise and replaced the concatenation step :

```
x = torch.cat([x2, x1], dim=1)
```

With a concatenation with itself:

```
x = torch.cat([x1, x1], dim=1)
```

It's a very simple and unimpactful way to make this change. This of course causes some redundancy of information, but I'm convinced it doesn't change anything in the core working of the algorithm (w.r.t. to if I removed the concatenation entirely). If you prefer that I remove the concatenation entirely you can let me know.


## parameters

This is a subexperiment of the experiment above, in the sense that the set of parameters is a subset of the set of parameters of the experiment above. I did it like this so that I can keep an eye if performance changes drastically after removing the skip-connections.

The target datasets have the following parameters:

- $\mu_1 \in \lbrace 64,96,128,160 \rbrace$

- $\mu_2 \in \lbrace \mu_1 + d : d \in \lbrace 24,42,73,128\rbrace \land \mu_1+d \leq 192 \rbrace$

- $\sigma_1 \in \lbrace 6,18,30 \rbrace$

- $\sigma_2 \in \lbrace 6,18,30 \rbrace$

This totals to 10 possible combinations of $(\mu_1, \mu_2)$ and 9 possible combinations of $(\sigma_1, \sigma_2)$, totalling 10x9 = 90 target datasets.

The source dataset is chosen to have parameters $(96, 18, 138, 18)$.

## Training history

Very unstable from a point onwards. The model saved is the one with the best preformance before early stopping kicks in, so this is not really an issue performance-wise.

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_90/training_history.png?raw=true">

## Results

Without BN adaptation:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_90/graph_2d.png?raw=true">

With BN adaptation:

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_90/graph_2d_adapted.png?raw=true">

## Wasserstein

The hope was that removing the skip-connections would assist the similarity between the latent spaces. This unfortunately was not the case. Plotting:

**Target-normalized Wasserstein - 0th ls**

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_90/Prometheus_0.png?raw=true">


**Target-normalized Wasserstein - 4th ls**

<img src="https://github.com/MarcoFurlan99/8_clip_correction_and_more/blob/master/1_90/Prometheus_4.png?raw=true">

No pattern at all.

# Ideas

- The U-Net is essentially a massive monster of parameters and changing the input likely changes all latent spaces in a non trivial way. I seriously doubt there is any relationship to be found there, it's too much of a mess between the input image and the latent spaces. It's been a couple months since I've had this feeling and now with the results in hand confirming it I'm quite demotivated, if there is anything else I should know about why this may work now it would be a good time to know it.

- Maybe checking in the brightness shift case as a very basic case and see if I can find some meaningful correlation there.

- why are we interpreting latent spaces as probability distributions w.r.t. the channels? It's matrices let's just use a distance between matrices before getting fancy with probability distributions (what about a simple L1 distance, was it ever tried? It's literally the first thing that should be tried before doing anything else). If I can get a re-explanation of why probability distributions, other than using the Wasserstein in this, let me know.
