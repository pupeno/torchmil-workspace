#!/usr/bin/env python3
"""Reproduce DTFDMIL prediction changes caused by masked zero padding."""

import numpy as np
import torch
from torchmil.models import DTFDMIL

torch.manual_seed(0)
model = DTFDMIL(in_shape=(3,), att_dim=2, n_groups=1, distill_mode="maxmin").eval()
X = torch.randn(1, 2, 3)
mask = torch.ones(1, 2, dtype=torch.bool)
padded_X = torch.nn.functional.pad(X, (0, 0, 0, 2))
padded_mask = torch.nn.functional.pad(mask, (0, 2), value=False)

# One group keeps every real tile together regardless of the shuffle.
with torch.no_grad():
    np.random.seed(0)
    expected = model(X, mask)
    np.random.seed(0)
    actual = model(padded_X, padded_mask)

print("These predictions should be the same.")
print(f"Unpadded logit:           {expected.item():.9f}")
print(f"Masked zero-padded logit: {actual.item():.9f}")
torch.testing.assert_close(actual, expected)
