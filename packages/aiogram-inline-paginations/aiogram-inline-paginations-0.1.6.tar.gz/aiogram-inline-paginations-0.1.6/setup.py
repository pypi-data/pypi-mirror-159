# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiogram_inline_paginations']

package_data = \
{'': ['*']}

install_requires = \
['aiogram>=2.21,<3.0',
 'pip>=22.1.2,<23.0.0',
 'setuptools>=63.2.0,<64.0.0',
 'wheel>=0.37.1,<0.38.0']

setup_kwargs = {
    'name': 'aiogram-inline-paginations',
    'version': '0.1.6',
    'description': 'A simple library for aiogram that allows you to easily do pagination for any Inline keyboards.',
    'long_description': "# aiogram-inline-paginations\n\n## Description\n\nA simple library for aiogram that allows you to easily do pagination for any Inline keyboards.\n\nInstall for pip:\n\n```shell\npip install aiogram-inline-paginations\n```\n\nInstall for poetry:\n\n```shell\npoetry add aiogram-inline-paginations\n```\n\n## Create paginations object\n\n```python\nfrom aiogram_inline_paginations.paginator import Paginator\nfrom aiogram import types\n\nkb = types.InlineKeyboardMarkup()\npaginator = Paginator(data=kb, size=5)\n```\n\n### Params\n\n**data**: Any ready-to-use keyboard InlineKeyboardMarkup or any iterable object with InlineKeyboardButton.\n\n**size**: The number of rows of buttons on one page, excluding the navigation bar.\n\n### Return\n\nA paginator object that, when called, returns a ready-made keyboard with pagination.\n\n## Get data for registrations handler paginator\n\n```python\nfrom aiogram_inline_paginations.paginator import Paginator\nfrom aiogram import types\n\nkb = types.InlineKeyboardMarkup()\npaginator = Paginator(data=kb, size=5)\n\n\n@dp.message_handler()\nasync def some_func(message: types.Message):\n    await message.answer(\n        text='Some menu',\n        reply_markup=paginator()\n    )\n\n    args, kwargs = paginator.paginator_handler()\n    dp.register_callback_query_handler(*args, **kwargs)\n\n```\n\n### Return paginator_handler()\n\nData for registrations paginator.\n\n## Example\n\n```python\nimport random\n\nfrom aiogram import Bot, Dispatcher, types\nfrom aiogram.contrib.fsm_storage.memory import MemoryStorage\nfrom aiogram.dispatcher.filters import CommandStart\nfrom aiogram.utils.executor import Executor\n\nfrom aiogram_inline_paginations.paginator import Paginator\n\ntoken = 'your token'\n\nstorage = MemoryStorage()\nbot = Bot(token=token)\ndp = Dispatcher(bot, storage=storage)\n\n\n@dp.message_handler(CommandStart(), state='*')\nasync def start(message: types.Message):\n    await message.answer('Hello text')\n\n    kb = types.InlineKeyboardMarkup()  # some keyboard\n\n    '''To demonstrate, I will add more than 50 buttons to the keyboard and divide them into 5 lines per page'''\n    kb.add(\n        *[\n            types.InlineKeyboardButton(\n                text=str(random.randint(1000000, 10000000)),\n                callback_data='pass'\n            ) for i in range(2)\n        ]\n    )\n\n    kb.add(\n        *[\n            types.InlineKeyboardButton(\n                text=str(random.randint(1000000, 10000000)),\n                callback_data='pass'\n            ) for i in range(3)\n        ]\n    )\n\n    kb.add(\n        types.InlineKeyboardButton(\n            text=str(random.randint(1000000, 10000000)),\n            callback_data='pass'\n        )\n    )\n\n    kb.add(\n        *[\n            types.InlineKeyboardButton(\n                text=str(random.randint(1000000, 10000000)),\n                callback_data='pass'\n            ) for i in range(2)\n        ]\n    )\n\n    kb.add(\n        *[\n            types.InlineKeyboardButton(\n                text=str(random.randint(1000000, 10000000)),\n                callback_data='pass'\n            ) for i in range(50)\n        ]\n    )\n\n    paginator = Paginator(data=kb, size=5)\n\n    await message.answer(\n        text='Some menu',\n        reply_markup=paginator()\n    )\n\n    args, kwargs = paginator.paginator_handler()\n    dp.register_callback_query_handler(*args, **kwargs)\n\n\nif __name__ == '__main__':\n    Executor(dp).start_polling()\n\n```\n\n## Screenshots\n\nFirst page:\n\n![img_1.png](https://github.com/daniilshamraev/aiogram-inline-paginations/blob/master/img/img_1.png?raw=true)\n\nSecond page:\n\n![img_2.png](https://github.com/daniilshamraev/aiogram-inline-paginations/blob/master/img/img_2.png?raw=true)\n\nLast page:\n\n![img_3.png](https://github.com/daniilshamraev/aiogram-inline-paginations/blob/master/img/img_3.png?raw=true)\n\n*The order of entries is not lost.*\n\n## License MIT",
    'author': 'Daniil Shamraev',
    'author_email': 'shamraev.2002@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/daniilshamraev/aiogram-inline-paginations',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
