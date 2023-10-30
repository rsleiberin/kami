# Penalty Parameters Details

## Frequency and Presence Penalties

The frequency and presence penalties, which are features in both the Chat completions API and Legacy Completions API, serve as mechanisms to reduce the likelihood of producing repetitive sequences of tokens. These penalties function by adjusting the logits (un-normalized log-probabilities) with an additive contribution.

The formula for this adjustment is:

```math
mu[j] -> mu[j] - c[j] * alpha_frequency - float(c[j] > 0) * alpha_presence
```

Where:

- `mu[j]`: Logits of the j-th token.
- `c[j]`: Represents how frequently that token was sampled before the current position.
- `float(c[j] > 0)`: Yields 1 if `c[j] > 0` and 0 otherwise.
- `alpha_frequency`: The frequency penalty coefficient.
- `alpha_presence`: The presence penalty coefficient.

In essence, the presence penalty introduces a one-time additive contribution that's applied to all tokens sampled at least once. Meanwhile, the frequency penalty offers a contribution proportional to the recurrence of a specific token.

Typically, penalty coefficients within the range of 0.1 to 1 are considered reasonable if the goal is to mildly reduce repetitive outputs. However, if the objective is to significantly suppress repetition, the coefficients can be increased up to 2, although it's worth noting that doing so might compromise the quality of the generated samples. To promote repetition, negative values can be utilized.
