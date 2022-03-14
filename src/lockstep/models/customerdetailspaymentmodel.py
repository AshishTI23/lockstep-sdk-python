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

@dataclass
class CustomerDetailsPaymentModel:
    """
    Customer payment collected information
    """

    groupKey: str | None = None
    paymentId: str | None = None
    paymentAppliedId: str | None = None
    paymentType: str | None = None
    invoiceId: str | None = None
    invoiceTypeCode: str | None = None
    invoiceReferenceCode: str | None = None
    invoiceTotalAmount: float | None = None
    paymentDate: str | None = None
    paymentAmount: float | None = None

