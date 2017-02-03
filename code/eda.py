import numpy as np
import pandas as pd
import h5py

# docker run -it kagglegym
# python
# >>> import kagglegym
# >>> kagglegym.test()

train = pd.read_hdf("../data/train.h5")
