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
class AttachmentLinkModel:
    """
    An Attachment Link represents a single link between any nestable
    object and an attachment
    """

    groupKey: str | None = None
    attachmentId: str | None = None
    objectKey: str | None = None
    tableKey: str | None = None
    created: str | None = None
    createdUserId: str | None = None
