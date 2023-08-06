# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import datetime as dt
from .api import quantim

class energy_data(quantim):
    def __init__(self, username, password, secretpool, env="qa"):
        super().__init__(username, password, secretpool, env)

    def get_sector_data(self, country, date_ini="", date_last=""):
        data={"cod_pais":country, "metrica":"","fec_ini":date_ini, "fec_fin":date_last}
        resp = self.api_call('energy_data', method="post", data=data, verify=False)
        resp_df = pd.DataFrame(resp).set_index('Date')
        return pd.DataFrame(resp).set_index('Date')
