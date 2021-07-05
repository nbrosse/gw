from pathlib import Path
from typing import List

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from data import extract_id_target_signals

DETECTOR_NAMES: List[str] = ["LIGO Hanford", "LIGO Livingston", "Virgo"]

XP_PATH: Path = Path("/home/nicolas/Documents/gw_project/")


def plot_signals_from_array(signals: np.ndarray,
                            id: str,
                            target: int,
                            subplots: bool,
                            ) -> go.Figure:
    x = np.arange(signals.shape[1])
    if subplots:
        fig = make_subplots(rows=3,
                            cols=1)
        for i in range(3):
            fig.add_trace(go.Scatter(x=x,
                                     y=signals[i],
                                     name=f"{DETECTOR_NAMES[i]}",
                                     ),
                          row=i + 1,
                          col=1)
    else:
        fig = go.Figure()
        for i in range(3):
            fig.add_trace(go.Scatter(
                x=x,
                y=signals[i],
                name=f"{DETECTOR_NAMES[0]}",
            ))
    fig.update_layout(
        title=f"id: {id}, target: {target}"
    )
    return fig


dict_res = extract_id_target_signals(idx=0)
fig = plot_signals_from_array(signals=dict_res["signals"],
                              id=dict_res["id"],
                              target=dict_res["target"],
                              subplots=True)

fig.write_html(str(XP_PATH / "figure.html"))
