"""
The MIT License (MIT)

Copyright (c) 2015-2021 Rapptz
Copyright (c) 2021-present Disnake Development

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

from typing import List, Literal, Optional, TypedDict, Union

from .appinfo import PartialAppInfo
from .channel import ChannelType
from .components import Component
from .embed import Embed
from .emoji import PartialEmoji
from .interactions import InteractionMessageReference
from .member import Member, UserWithMember
from .snowflake import Snowflake, SnowflakeList
from .sticker import StickerItem
from .threads import Thread
from .user import User


class ChannelMention(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    type: ChannelType
    name: str


class Reaction(TypedDict):
    count: int
    me: bool
    emoji: PartialEmoji


class _AttachmentOptional(TypedDict, total=False):
    height: Optional[int]
    width: Optional[int]
    content_type: str
    ephemeral: bool
    description: str


class Attachment(_AttachmentOptional):
    id: Snowflake
    filename: str
    size: int
    url: str
    proxy_url: str


MessageActivityType = Literal[1, 2, 3, 5]


class _MessageActivityOptional(TypedDict, total=False):
    party_id: str


class MessageActivity(_MessageActivityOptional):
    type: MessageActivityType


class MessageReference(TypedDict, total=False):
    message_id: Snowflake
    channel_id: Snowflake
    guild_id: Snowflake
    fail_if_not_exists: bool


class _MessageOptional(TypedDict, total=False):
    guild_id: Snowflake
    member: Member
    mention_channels: List[ChannelMention]
    reactions: List[Reaction]
    nonce: Union[int, str]
    webhook_id: Snowflake
    activity: MessageActivity
    application: PartialAppInfo
    application_id: Snowflake
    message_reference: MessageReference
    flags: int
    sticker_items: List[StickerItem]
    referenced_message: Optional[Message]
    interaction: InteractionMessageReference
    components: List[Component]
    thread: Thread


MessageType = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 19, 20, 21]


class Message(_MessageOptional):
    id: Snowflake
    channel_id: Snowflake
    author: User
    content: str
    timestamp: str
    edited_timestamp: Optional[str]
    tts: bool
    mention_everyone: bool
    mentions: List[UserWithMember]
    mention_roles: SnowflakeList
    attachments: List[Attachment]
    embeds: List[Embed]
    pinned: bool
    type: MessageType


AllowedMentionType = Literal["roles", "users", "everyone"]


class AllowedMentions(TypedDict):
    parse: List[AllowedMentionType]
    roles: SnowflakeList
    users: SnowflakeList
    replied_user: bool
