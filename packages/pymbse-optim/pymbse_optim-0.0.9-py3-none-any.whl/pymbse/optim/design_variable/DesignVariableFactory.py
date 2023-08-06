from typing import List

import pandas as pd

from pymbse.optim.design_variable.DesignVariable import DesignVariable
from pymbse.optim.design_variable.GeneticDesignVariable import GeneticDesignVariable


def init_design_variables_with_csv(csv_path: str) -> List[GeneticDesignVariable]:
    """

    :param csv_path:
    :return:
    """
    # todo: add description of columns in the dataframe
    design_variables_df = pd.read_csv(csv_path)
    return init_design_variables_with_df(design_variables_df)


def init_design_variables_with_df(design_variables_df: pd.DataFrame) -> list:
    design_variables = []
    for _, row in design_variables_df.iterrows():
        if 'bits' in row:
            dv = GeneticDesignVariable(**row)
        else:
            dv = DesignVariable(**row)
        design_variables.append(dv)

    return design_variables
