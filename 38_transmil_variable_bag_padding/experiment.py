#!/usr/bin/env python3
"""Reproduce TransMIL prediction changes caused by batch padding."""

import torch
from torchmil.data import collate_fn
from torchmil.models import MILModelWrapper, TransMIL

torch.manual_seed(0)
model = MILModelWrapper(
    TransMIL(in_shape=(8,), att_dim=16, n_heads=2, n_landmarks=4).eval()
)
small_bag = {"X": torch.randn(4, 8), "Y": torch.tensor(1.0)}
large_bag = {"X": torch.randn(9, 8), "Y": torch.tensor(0.0)}

# Collating with the larger bag pads the small one with five masked zero tiles.
with torch.no_grad():
    expected = model(collate_fn([small_bag]))
    actual = model(collate_fn([small_bag, large_bag]))[:1]

print("These predictions should be the same.")
print(f"Small bag alone:              {expected.item():.9f}")
print(f"Small bag in a padded batch:  {actual.item():.9f}")
torch.testing.assert_close(actual, expected)
