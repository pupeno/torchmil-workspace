#!/usr/bin/env python3
"""Reproduce CAMIL prediction changes caused by batch padding."""

import torch
from torchmil.data import collate_fn
from torchmil.models import CAMIL, MILModelWrapper


def make_bag(size):
    # Each tile is connected to itself and to the next tile.
    adj = torch.eye(size)
    adj[range(size - 1), range(1, size)] = adj[range(1, size), range(size - 1)] = 1
    return {"X": torch.randn(size, 8), "adj": adj.to_sparse(), "Y": torch.tensor(1.0)}


torch.manual_seed(0)
model = MILModelWrapper(
    CAMIL(in_shape=(8,), nystrom_att_dim=16, n_heads=2, n_landmarks=4).eval()
)
small_bag = make_bag(4)
large_bag = make_bag(9)

# Collating with the larger bag pads the small one with five masked zero tiles.
with torch.no_grad():
    expected = model(collate_fn([small_bag]))
    actual = model(collate_fn([small_bag, large_bag]))[:1]

print("These predictions should be the same.")
print(f"Small bag alone:              {expected.item():.9f}")
print(f"Small bag in a padded batch:  {actual.item():.9f}")
torch.testing.assert_close(actual, expected)
