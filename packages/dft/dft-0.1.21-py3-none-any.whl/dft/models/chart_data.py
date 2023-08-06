import json
from typing import Dict, Any

import pandas as pd

from dft.models.chart_options.chart_options import ChartOptions


class ChartData:
    options: ChartOptions
    raw_data: pd.DataFrame

    def __init__(self, options=None, raw_data=None):
        self.options = options
        self.raw_data = raw_data

    def prepare_raw_data(self) -> Dict[str, Any]:
        result = json.loads(self.raw_data.to_json(orient="split"))
        final_result = {}
        for i in range(len(result["columns"])):
            final_result[result["columns"][i]] = result["data"][i]

        return final_result


