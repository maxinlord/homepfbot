import asyncio
import logging
import sys

from dispatcher import dp, bot
from handlers import (
    start,
    main,
    any_mess,
)



async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
