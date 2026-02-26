from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Info:  # pylint:disable=too-many-instance-attributes
    type: str
    # Отсюда можно взять родной чат адаптера
    _adapter_chat: Any
    # Тут слишком много параметров.
    # По хорошему надо разбить на несколько классов
    # Это too-many-instance-attributes - нельзя игнорировать
    # Должно быть 7 атрибутов класса максимум
    title: str = None
    username: str = None
    first_name: str = None
    last_name: str = None
    is_forum: bool = None
    max_reaction_count: int = None
    # photo: Optional[ChatPhoto] = photo
    bio: str = None
    join_to_send_messages: bool = None
    join_by_request: bool = None
    has_private_forwards: bool = None
    has_restricted_voice_and_video_messages: bool = None
    description: str = None
    invite_link: str = None
    # pinned_message: Optional[Message] = pinned_message
    # permissions: Optional[ChatPermissions] = permissions
    slow_mode_delay: int = None
    message_auto_delete_time: int = None
    has_protected_content: bool = None
    sticker_set_name: str = None
    can_set_sticker_set: bool = None
    linked_chat_id: int = None
    # location: Optional[ChatLocation] = location
    # active_usernames: Optional[List[str]] = active_usernames
    emoji_status_custom_emoji_id: str = None
    has_hidden_members: bool = None
    has_aggressive_anti_spam_enabled: bool = None
    emoji_status_expiration_date: int = None
    # available_reactions: Optional[List[ReactionType]] = available_reactions
    accent_color_id: int = None
    background_custom_emoji_id: str = None
    profile_accent_color_id: int = None
    profile_background_custom_emoji_id: str = None
    has_visible_history: bool = None
    unrestrict_boost_count: int = None
    custom_emoji_sticker_set_name: str = None
    # business_intro: Optional[BusinessIntro] = business_intro
    # business_location: Optional[BusinessLocation] = business_location
    # business_opening_hours: Optional[BusinessOpeningHours] = business_opening_hours
    # personal_chat: Optional[Chat] = personal_chat
    # birthdate: Optional[Birthdate] = birthdate
    can_send_paid_media: bool = None
