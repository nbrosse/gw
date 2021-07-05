from pathlib import Path
from typing import Dict, Any

import numpy as np
import pandas as pd

data_path = Path("/home/nicolas/Data/gw_data/small_training_data/")

df = pd.read_parquet(str(data_path / "df.parquet"))


def extract_id_target_signals(idx: int) -> Dict[str, Any]:
    return dict(
        id=df.loc[idx, "id"],
        target=df.loc[idx, "target"],
        signals=np.load(str(data_path / f"{df.loc[idx, 'id']}.npy")),
    )
