##AlexNet fot CIFAR-100
##Taken from https://github.com/bearpaw/pytorch-classification/blob/master/models/cifar/alexnet.py
##Planning to also try this https://github.com/AbhishekTaur/AlexNet-CIFAR-10/blob/master/alexnet.py
##Also check https://github.com/icpm/pytorch-cifar10/blob/master/models/AlexNet.py
##For MobileNet https://github.com/kuangliu/pytorch-cifar/blob/master/models/mobilenet.py

import torch.nn as nn
import torch.nn.functional as F

'''
modified to fit dataset size
'''

__all__ = ['alexnet_cifar100'] ##edited by ffk

NUM_CLASSES = 100

class AlexNet(nn.Module):
    def __init__(self, num_classes=NUM_CLASSES):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=2, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(64, 192, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2),
        )
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 2 * 2, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), 256 * 2 * 2)
        x = self.classifier(x)
        return x

def alexnet_cifar100(): ##edited by ffk
    model = AlexNet()
    return model
