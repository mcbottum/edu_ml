import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

path = Path(os.getcwd())
achieve_df = pd.read_csv(path/"data"/"2020-21_school_reportcard_data.tsv", sep="\t")
act_df = pd.read_csv(path/"data"/"act_statewide_certified_2020-21.csv")
