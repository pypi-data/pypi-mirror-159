import functools

from collections import defaultdict
from typing import Callable, Any

from pyrogram.client import Client
from pyrogram.types import Update, Message

class StepHandler:

    def __init__(self) -> None:
        self.handlers = defaultdict()
    
    async def _step_listener(self, _c: Client, _u: Update) -> Any:
         if hasattr(_u, "from_user") and hasattr(_u.from_user, "id"):
            try:
                fn = self.handlers[_u.from_user.id]
            except KeyError:
                pass
            else:
                return await fn(_c, _u)

    def set_step_listener(self, app: Client, filters=None, group: int = 0, on_update: str = "on_message") -> None:
        """
        set_step_listener sets a listener decorator to get better result, and dont need to use first_step
        decorator.

        #### Recommended use after all decorators

        Parameters:
            app (``pyrogram.Client``):
                which client you want to listen.
            
            filters (``pyrogram.filters``):
                filters for listener.
            
            group (``int``):
                which group number you want to set listener.

            on_update (``str``):
                set listener on which decorator. default on_message.
        
        Example:
            >>> set_step_listener(app)
        """
        getattr(app, on_update)(filters=filters, group=group)(self._step_listener)

    def _first_step_decorator(self, cls: Callable[[Client, Update], Any]) -> Callable[[Client, Update], Any]:
        """
        _first_step_decorator works like middleware for handlers.

        Parameters:
            cls (``Callable[[Client, Update], Any]``):
                handler.
        """

        @functools.wraps(cls)
        async def wrapper(_c: Client, _u: Update):

            if hasattr(_u, "from_user") and hasattr(_u.from_user, "id"):
                try:
                    fn = self.handlers[_u.from_user.id]
                except KeyError:
                    return await cls(_c, _u)
                else:
                    return await fn(_c, _u)
            
            return await cls(_c, _u)

        return wrapper
    
    def first_step(self, cls: Callable = None) -> Callable[[Client, Update], Any]:
        """
        first_step sets middleware for your handler to check listens.

        Parameters:
            cls (``Callable[[Client, Update], Any]``):
                handler.

        Example:
            >>> @app.on_message(...)
            >>> @first_step() # or @first_step
            >>> async def handler(client, msg):
            ...     # code ...
            ...     register_next_step(msg.from_user.id, handler2)
            ...
            >>> async def handler2(client, msg):
            ...     # code ...
            ...     # register_next_step(msg.from_user.id, handler3)
            ...     # or
            ...     # unregister_steps(msg.from_user.id)
        """
        if cls == None:
            def wrap(func): return self._first_step_decorator(func)
            return wrap
        
        return self._first_step_decorator(cls)
    
    def _end_step_decorator(self, cls: Callable[[Client, Update], Any]) -> Callable[[Client, Update], Any]:
        """
        _end_step_decorator works like middleware for handlers, call unregister_steps before call handler.

        Parameters:
            cls (``Callable[[Client, Update], Any]``):
                handler.
        """
        @functools.wraps(cls)
        async def wrapper(_c: Client, _u: Update, *args, **kwargs):

            if hasattr(_u, "from_user") and hasattr(_u.from_user, "id"):
                await self.unregister_steps(_u.from_user.id)
            
            return await cls(_c, _u, *args, **kwargs)

        return wrapper

    def end_step(self, cls: Callable = None) -> Callable[[Client, Update], Any]:
        """
        end_step works like middleware for handlers, call unregister_steps before call handler.

        Parameters:
            cls (``Callable[[Client, Update], Any]``):
                handler.

        Example:
            >>> @end_step() # or @end_step
            >>> async def end_handler(client, msg):
            ...     # code ...
        """
        if cls == None:
            def wrap(func): return self._end_step_decorator(func)
            return wrap
        
        return self._end_step_decorator(cls)

    async def register_next_step(self, _id: int, _next: Callable[[Client, Update], Any]) -> None:
        """
        register_next_step sets next step for user.

        Parameters:
            _id (``int``):
                user numeric id.
            
            _next (``Callable[[Client, Update], Any]``):
                next step handler.
        
        Example:
            >>> async def handler1(client, msg):
            ...     # code ...
            ...     register_next_step(msg.from_user.id, handler2)
        """
        self.handlers[_id] = _next

    async def ask(self, _msg: Message, _next: Callable[[Client, Update], Any], *args, **kwargs) -> None:
        """ 
        it is shorthand for _msg.reply_text(*args, **kwargs); register_next_step(chat_id, _next)
        """
        await _msg.reply_text(*args, **kwargs)
        self.handlers[_msg.from_user.id] = _next

    async def unregister_steps(self, _id: int) -> None:
        """
        unregister_steps removes all user step's.

        Parameters:
            _id (``int``):
                user numeric id.
        """
        try:
            del self.handlers[_id]
        except KeyError:
            pass

    async def clear(self) -> None:
        """
        clear clears all user's step's.
        """
        self.handlers.clear()

_main_handler = StepHandler()

def set_step_listener(app: Client, filters=None, group: int = 0, on_update: str = "on_message") -> None:
    """
    set_step_listener sets a listener decorator to get better result, and dont need to use first_step
    decorator.

    #### Recommended use after all decorators

    Parameters:
        app (``pyrogram.Client``):
            which client you want to listen.
        
        filters (``pyrogram.filters``):
            filters for listener.
        
        group (``int``):
            which group number you want to set listener.
        
        on_update (``str``):
            set listener on which decorator. default on_message.
    
    Example:
        >>> set_step_listener(app)
    """
    _main_handler.set_step_listener(app, filters, group, on_update)

def first_step(cls: Callable = None) -> Callable[[Client, Update], Any]:
    """
    first_step sets middleware for your handler to check listens.

    Parameters:
        cls (``Callable[[Client, Update], Any]``):
            handler.

    Example:
        >>> @app.on_message(...)
        >>> @pyrostep.first_step() # or @pyrostep.first_step
        >>> async def handler(client, msg):
        ...     # code ...
        ...     pyrostep.register_next_step(msg.from_user.id, handler2)
        ...
        >>> async def handler2(client, msg):
        ...     # code ...
        ...     # pyrostep.register_next_step(msg.from_user.id, handler3)
        ...     # or
        ...     # pyrostep.unregister_steps(msg.from_user.id)
    """
    return _main_handler.first_step(cls)

def end_step(cls: Callable = None) -> Callable[[Client, Update], Any]:
    """
    end_step works like middleware for handlers, call unregister_steps before call handler.

    Parameters:
        cls (``Callable[[Client, Update], Any]``):
            handler.

    Example:
        >>> @pyrostep.end_step() # or @pyrostep.end_step
        >>> async def end_handler(client, msg):
        ...     # code ...
    """
    return _main_handler.end_step(cls)

async def register_next_step(_id: int, _next: Callable[[Client, Update], Any]) -> None:
    """
    register_next_step sets next step for user.

    Parameters:
        _id (``int``):
            user numeric id.
        
        _next (``Callable[[Client, Update], Any]``):
            next step handler.
    
    Example:
        >>> async def handler1(client, msg):
        ...     # code ...
        ...     register_next_step(msg.from_user.id, handler2)
    """
    await _main_handler.register_next_step(_id, _next)

async def ask(_msg: Message, _next: Callable[[Client, Update], Any], *args, **kwargs) -> None:
    """ 
    it is shorthand for _msg.reply_text(*args, **kwargs); register_next_step(chat_id, _next)
    """
    await _main_handler.ask(_msg, _next, *args, **kwargs)

async def unregister_steps(_id: int) -> None:
    """
    unregister_steps removes all user step's.

    Parameters:
        _id (``int``):
            user numeric id.
    """
    await _main_handler.unregister_steps(_id)

async def clear() -> None:
    """
    clear clears all user's step's.
    """
    await _main_handler.clear()
