from papercandy import *
from torch.nn import *


class Net(Module):
    def __init__(self):
        super().__init__()
        self.conv1 = Conv2d(1, 2, (3, 4))
        self.conv2 = Conv2d(1, 2, (3, 4))
        self.dropout = Dropout2d()
        self.pool = MaxPool2d(1)
        self.batch_norm = BatchNorm2d(20)


draw(NetworkC(Net()), interval=0.05).save("../structure.jpg").show()
