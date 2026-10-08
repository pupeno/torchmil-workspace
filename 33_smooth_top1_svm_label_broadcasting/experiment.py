#!/usr/bin/env python3
"""One sample reproduces SmoothTop1SVM's incorrect loss."""

import torch
from torchmil.nn.utils import SmoothTop1SVM

scores = torch.tensor([[2.0, 0.0]])
targets = torch.tensor([[0]])  # CLAM passes class indices as columns.
loss_fn = SmoothTop1SVM(n_classes=2)  # Default alpha=1, tau=1.

# Margins: true class = 2 - 2 = 0; other class = 0 + 1 - 2 = -1.
expected = torch.logsumexp(torch.tensor([0.0, -1.0]), dim=0)
actual = loss_fn(scores, targets)

print(f"actual loss: {actual.item():.6f}; expected: {expected.item():.6f}")
torch.testing.assert_close(actual, expected)
