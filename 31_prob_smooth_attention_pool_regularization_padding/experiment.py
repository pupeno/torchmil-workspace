#!/usr/bin/env python3

import torch
from torchmil.nn import ProbSmoothAttentionPool

torch.manual_seed(0)
pool = ProbSmoothAttentionPool(in_dim=3, att_dim=2)
X = torch.randn(1, 2, 3)
adj = torch.full((1, 2, 2), 0.5)
_, expected = pool(X, adj, return_kl_div=True, n_samples=1)

padded_X = torch.nn.functional.pad(X, (0, 0, 0, 2), value=10)
padded_adj = torch.nn.functional.pad(adj, (0, 2, 0, 2))
mask = torch.tensor([[1, 1, 0, 0]])
_, actual = pool(padded_X, padded_adj, mask, return_kl_div=True, n_samples=1)

print("These regularizers should be the same.")
print(f"Unpadded regularizer:      {expected.item():.9f}")
print(f"Masked padded regularizer: {actual.item():.9f}")
torch.testing.assert_close(actual, expected)
