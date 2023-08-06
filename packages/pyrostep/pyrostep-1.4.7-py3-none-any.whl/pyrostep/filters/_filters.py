from pyrogram.filters import create, Filter
from pyrogram.types import Message

#region ttl_message_filter
async def ttl_message_filter(_, __, m: Message) -> bool:
    return (m.photo and m.photo.ttl_seconds) or (m.video and m.video.ttl_seconds)

ttl_message = create(ttl_message_filter)
"""Filter ttl messages ( ttl photo message or ttl video message )."""
#endregion


#region video_sticker_filter
async def video_sticker_filter(_, __, m: Message) -> bool:
    return m.sticker and m.sticker.is_video

video_sticker = create(video_sticker_filter)
"""Filter video sticker messages."""
#endregion


#region entities_filter
async def entities_filter(_, __, m: Message) -> bool:
    return bool(m.entities or m.caption_entities)

entities = create(entities_filter)
"""Filter messages include entities."""
#endregion


#region photo_size_filter
def photo_size(width: int, height: int) -> Filter:
    """
    Filter photo messages with width and height.
    
    Example:
        >>> @app.on_message(photo_size(512, 512))
    """
    async def photo_size_filter(_, __, m: Message) -> bool:
        return m.photo and m.photo.width == width and m.photo.height == height

    return create(photo_size_filter)
#endregion
