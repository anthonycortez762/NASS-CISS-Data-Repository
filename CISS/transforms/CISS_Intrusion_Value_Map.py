import Global_Constants
import pandas as pd

ciss_intrusion_col_specific_value_maps = {
    'INTMAG': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {9: pd.NA}
        }
    ],
    'INTRUSION': [
        {
            'ranges': Global_Constants.common_ciss_year_range,
            'mapping': {888: pd.NA, 999: pd.NA}
        }
    ],
}
