import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

FILE_DIR = Path(__file__).parent / "active_volcanos.csv"

df = pd.read_csv(FILE_DIR)
print(df.hazard.unique())

df_clean = df.dropna(subset=["hazard"])
print(df_clean)

print(df_clean[df_clean.hazard > 1])
