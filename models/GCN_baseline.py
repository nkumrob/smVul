import torch
import torch.nn as nn
import torch.nn.functional as F
from models.layers import GraphConvolutionNetwork

"""
Simple GCN
"""
class GCN_Baseline(nn.Module):
    def __init__(self, n_feature, n_hidden, n_class, dropout):
        super(GCN_Baseline, self).__init__()
        self.gc1 = GraphConvolutionNetwork(n_feature, n_hidden)
        self.gc2 = GraphConvolutionNetwork(n_hidden, n_class)
        self.dropout = dropout

    def forward(self, x, adj):
        x = self.gc1(x, adj)
        x = F.relu(x)
        x = F.dropout(x, self.dropout, training=self.training)
        x = self.gc2(x, adj)
        x = torch.max(x, dim=1)[0].squeeze()  # max pooling over nodes (usually performs better than average)
        return x