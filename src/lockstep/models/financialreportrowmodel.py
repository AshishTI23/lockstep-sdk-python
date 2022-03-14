#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass
from __future__ import annotations
from lockstep.models.financialreportcellmodel import FinancialReportCellModel

@dataclass
class FinancialReportRowModel:
    """
    Represents a row of a financial Report report
    """

    rowType: str | None = None
    label: str | None = None
    rows: list[FinancialReportRowModel] | None = None
    cells: list[FinancialReportCellModel] | None = None
