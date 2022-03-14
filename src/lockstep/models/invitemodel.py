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
from lockstep.models.useraccountmodel import UserAccountModel

@dataclass
class InviteModel:
    """
    Model from the User invite process
    """

    email: str | None = None
    success: bool | None = None
    invitedUser: UserAccountModel | None = None
    errorMessage: str | None = None

