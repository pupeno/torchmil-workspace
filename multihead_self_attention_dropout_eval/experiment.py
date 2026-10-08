#!/usr/bin/env python3
import torch
from torchmil.nn import MultiheadSelfAttention

torch.manual_seed(0)
model = MultiheadSelfAttention(in_dim=4, att_dim=4, dropout=0.5).eval()
x = torch.ones(1, 8, 4)

a, b = model(x), model(x)
assert torch.equal(a, b), "Eval outputs differ"
