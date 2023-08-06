from enum import Enum


class PostMetadataEmbedsItemType(str, Enum):
    IMAGE = "image"
    MESSAGE_ATTACHMENT = "message_attachment"
    OPENGRAPH = "opengraph"
    LINK = "link"

    def __str__(self) -> str:
        return str(self.value)
