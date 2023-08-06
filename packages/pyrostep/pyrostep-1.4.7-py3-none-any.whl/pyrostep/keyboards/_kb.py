import typing
from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

def split_list(lst: list, rows: int) -> list:
    """
    split_list splites lst list.

    Parameters:
        lst (``list``):
            list.
        
        rows (``int``):
            count of rows.
    
    Example:
        >>> split_list([1, 2, 3, 4, 5, 6], 2) # [[1, 2], [3, 4], [5, 6]]
        >>> split_list([1, 2, 3], 2) # [[1, 2], [3]]
    """
    return [ lst[i:i+rows] for i in range(0, len(lst), rows) ]

def keyboard(lst: typing.List[typing.List[typing.List[str]]], **kwargs) -> ReplyKeyboardMarkup:
    """
    keyboard creates ReplyKeyboardMarkup from your list.

    Parameters:
        lst (``list[list[list]]``):
            your list.
        
        resize_keyboard (``bool``, *optional*):
            Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if
            there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of
            the same height as the app's standard keyboard.

        one_time_keyboard (``bool``, *optional*):
            Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available,
            but clients will automatically display the usual letter-keyboard in the chat – the user can press a
            special button in the input field to see the custom keyboard again. Defaults to false.

        selective (``bool``, *optional*):
            Use this parameter if you want to show the keyboard to specific users only. Targets:
            1) users that are @mentioned in the text of the Message object;
            2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
            Example: A user requests to change the bot's language, bot replies to the request with a keyboard to
            select the new language. Other users in the group don't see the keyboard.

        placeholder (``str``, *optional*):
            The placeholder to be shown in the input field when the keyboard is active; 1-64 characters.

    Example:
        >>> buttons = [
        ...     [
        ...         ["Top Left"], ["Top Right"]
        ...     ],
        ...     [
        ...         ["Bottom | Request Contact", True, "request_contact"]
        ...     ]
        ... ]
        >>> keyboard(buttons)
    """
    return ReplyKeyboardMarkup([ [_button(*kb) for kb in line] for line in lst ], **kwargs)

def inlinekeyboard(lst: typing.List[typing.List[typing.List[str]]]) -> InlineKeyboardMarkup:
    """
    inlinekeyboard creates InlineKeyboardMarkup from your list.

    Parameters:
        lst (``list[list[list]]``):
            your list.
    
    Example:
        >>> buttons = [
        ...     [
        ...         ["Top Left", "data_1"], ["Top Right", "data_2"]
        ...     ],
        ...     [
        ...         ["Bottom", "Your URL", "url"]
        ...     ]
        ... ]
        >>> inlienkeyboard(buttons)
    """
    return InlineKeyboardMarkup([ [_inline_button(*kb) for kb in line] for line in lst ])

def _button(text: str, value = None, _type: str = "request_contact") -> KeyboardButton:
    """
    _button returns KeyboardButton
    """
    return KeyboardButton(text) if value == None else KeyboardButton(text, **{_type:value})

def _inline_button(text: str, value = None, _type: str = "callback_data") -> InlineKeyboardButton:
    """
    _inline_button returns InlineKeyboardButton
    """
    return InlineKeyboardButton(text) if value == None else InlineKeyboardButton(text, **{_type:value})
