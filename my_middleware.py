from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import config


class BlockMainChatMiddlewareMessage(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        state: FSMContext,
    ) -> Any:
        if event.chat.id == config.data_chat['chat_id']:
            return
        return await handler(event, state)
