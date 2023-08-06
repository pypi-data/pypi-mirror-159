from papercandy.universal.drawing import *
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


draw(NetworkC(Net())).show()
LossesDrawer(1920, 1080)([0.12, 0.35, 0.59, 0.34, 0.20, 0.00041]).save("../trainer.jpg").show()
