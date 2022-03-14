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
class PaymentDetailModel:
    """
    Contains detailed information about a Payment.
    """

    groupKey: str | None = None
    paymentId: str | None = None
    customerId: str | None = None
    customerName: str | None = None
    memoText: str | None = None
    referenceCode: str | None = None
    primaryContact: str | None = None
    email: str | None = None
    paymentAmount: float | None = None
    unappliedAmount: float | None = None
    paymentType: str | None = None
    paymentDate: str | None = None
    postDate: str | None = None
    phone: str | None = None
    fax: str | None = None
    address1: str | None = None
    address2: str | None = None
    address3: str | None = None
    city: str | None = None
    stateRegion: str | None = None
    postalCode: str | None = None
    countryCode: str | None = None

