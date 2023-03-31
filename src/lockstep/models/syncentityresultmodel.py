#
# Lockstep Platform SDK for Python
#
# (c) 2021-2023 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2023 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class SyncEntityResultModel:
    """
    Contains information about a sync process for an entity.
    """

    insertCount: int | None = None
    updateCount: int | None = None
    deleteCount: int | None = None
    skipCount: int | None = None
    errorCount: int | None = None
    errors: object | None = None
    skips: object | None = None

