"""Probability functions for distributions commonly used in differential privacy."""

# SPDX-License-Identifier: Apache-2.0
# Copyright Tumult Labs 2022

from functools import lru_cache
from typing import overload

import numpy as np


@overload
def double_sided_geometric_pmf(k: int, alpha: float) -> float:
    ...


@overload
def double_sided_geometric_pmf(k: np.ndarray, alpha: float) -> np.ndarray:
    ...


def double_sided_geometric_pmf(
    k, alpha
):  # pylint: disable=missing-type-doc, missing-return-type-doc
    r"""Returns the pmf for a double sided geometric distribution at k.

    For :math:`k \in \mathbb{Z}`

    .. math::

        f(k)=
        \frac
            {e^{1 / \alpha} - 1}
            {e^{1 / \alpha} + 1}
        \cdot
        e^{\frac{-\mid k \mid}{\alpha}}

    A double sided geometric distribution is the difference between two geometric
    distributions (It can be sampled by sampling two values from a geometric
    distribution, and taking their difference).

    See section 4.1 in :cite:`BalcerV18` or scipy.stats.geom for more information (Note
    that the parameter :math:`p` used in scipy.stats.geom is related to :math:`\alpha`
    through :math:`p = 1 - e^{-1 / \alpha}`).

    Args:
        k: The values to calculate the pmf for.
        alpha: The scale of the geometric distribution.
    """
    return (
        (np.exp(1 / alpha) - 1) / (np.exp(1 / alpha) + 1) * np.exp(-np.abs(k) / alpha)
    )


@overload
def double_sided_geometric_cmf(k: int, alpha: float) -> float:
    ...


@overload
def double_sided_geometric_cmf(k: np.ndarray, alpha: float) -> np.ndarray:
    ...


def double_sided_geometric_cmf(
    k, alpha
):  # pylint: disable=missing-type-doc, missing-return-type-doc
    r"""Returns the cmf for a double sided geometric distribution at k.

    For :math:`k \in \mathbb{Z}`

    .. math::

        F(k) = \begin{cases}
        \frac{e^{1 / \alpha}}{e^{1 / \alpha} + 1} \cdot e^\frac{k}{\alpha} &
        \text{if k} \le 0 \\
        1 - \frac{1}{e^{1 / \alpha} + 1}\cdot e^{\frac{-k}{\alpha}} &
        \text{otherwise} \\
        \end{cases}

    See :func:`double_sided_geometric_pmf` for more information.

    Args:
        k: The values to calculate the pmf for.
        alpha: The scale of the geometric distribution.
    """
    if isinstance(k, int):
        return double_sided_geometric_cmf(np.array([k]), alpha)[0]
    return np.where(
        k <= 0,
        np.exp(1 / alpha) / (np.exp(1 / alpha) + 1) * np.exp(k / alpha),
        1 - np.exp(-k / alpha) / (np.exp(1 / alpha) + 1),
    )


@lru_cache(None)
def _discrete_gaussian_normalizing_constant(sigma_squared: float):
    """Returns the normalizing factor for :func:`discrete_gaussian_pmf`."""
    # This method for calculating the upper/lower bound to consider is used in
    # https://github.com/IBM/discrete-gaussian-differential-privacy/blob/master/testing-kolmogorov-discretegaussian.py
    # They say
    # "Compute the normalizing constant from -bounds to bounds instead of -inf to inf:
    # negligible error, as bounds is at least 50 standard deviations from 0,
    # and the tails decay exponentially."
    bound = max(10000, int(sigma_squared * 50))
    # +1 is the contribution from y = 0
    # The factor of 2 is because y/-y contribute the same for y != 0
    return 1 + 2 * np.sum(np.exp(-np.arange(1, bound) ** 2 / (2 * sigma_squared)))


@overload
def discrete_gaussian_pmf(k: int, sigma_squared: float) -> float:
    ...


@overload
def discrete_gaussian_pmf(k: np.ndarray, sigma_squared: float) -> np.ndarray:
    ...


def discrete_gaussian_pmf(k, sigma_squared):
    r"""Returns the pmf for a discrete gaussian distribution at k.

    For :math:`k \in \mathbb{Z}`

    .. math::
        :label: discrete_gaussian_pmf

        f(k) = \frac
        {e^{k^2/2\sigma^2}}
        {
            \sum_{n\in \mathbb{Z}}
            e^{n^2/2\sigma^2}
        }

    See :cite:`Canonne0S20` for more information. The formula above is based on
    Definition 1.

    The implementation also referenced the paper's implementation, which can be found at
    https://github.com/IBM/discrete-gaussian-differential-privacy.
    """
    return np.exp(
        -(k ** 2) / (2 * sigma_squared)
    ) / _discrete_gaussian_normalizing_constant(sigma_squared)


@overload
def discrete_gaussian_cmf(k: int, sigma_squared: float) -> float:
    ...


@overload
def discrete_gaussian_cmf(k: np.ndarray, sigma_squared: float) -> np.ndarray:
    ...


def discrete_gaussian_cmf(k, sigma_squared):
    """Returns the cmf for a discrete gaussian distribution at k.

    See :eq:`discrete_gaussian_pmf` for the probability mass function.
    """
    if isinstance(k, int):
        return discrete_gaussian_cmf(np.array([k]), sigma_squared)[0]
    # _discrete_gaussian_normalizing_constant explains calculating the bound this way
    lower_bound = min(-10000, -int(sigma_squared * 50), np.min(k))
    unnormalized_cmf = np.cumsum(
        np.exp(
            -(np.abs(np.arange(lower_bound, np.max(k) + 1) ** 2)) / (2 * sigma_squared)
        )
    )
    return unnormalized_cmf[k - lower_bound] / _discrete_gaussian_normalizing_constant(
        sigma_squared
    )
