from math import ceil
from typing import Tuple

import numpy as np
from scipy import optimize


def max_out_loss(vested: Tuple[float, float], outcome: float, price: float):
    max_capital_loss = 3000

    if all(map(lambda x: x < price, vested)):
        raise Exception("no loss to claim")

    def gain_loss(x, nx):
        return (price - x) * nx

    units = int(ceil(float(outcome) / price))
    return lambda params: [
        sum(params) - units,
        sum([gain_loss(p[0], p[1]) for p in zip(vested, params)]) + max_capital_loss,
    ]


if __name__ == "__main__":
    sale_price = 193
    sale_outcome = 19050
    options = (
        123.94,
        440.69,
    )

    seed_values = np.array([1.0, 1.0])
    result = optimize.fsolve(
        max_out_loss(options, sale_outcome, sale_price), seed_values
    )
    print(result)
