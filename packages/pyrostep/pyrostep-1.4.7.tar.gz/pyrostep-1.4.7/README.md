# Pyrostep

[![Downloads](https://static.pepy.tech/personalized-badge/pyrostep?period=total&units=abbreviation&left_color=red&right_color=grey&left_text=Downloads)](https://pepy.tech/project/pyrostep) ![Python](https://img.shields.io/static/v1?label=Language&message=Python&color=blue&style=flat&logo=python) ![Pyrogram](https://img.shields.io/static/v1?label=Framework&message=Pyrogram&color=red&style=flat)

A step handler library for pyrogram framework. \
Helps you to step handling ...

> I tried to provide the best speed ...

1. [Installing](#installing)
2. [Usage](#usage)
    - [set_step_listener method](#set_step_listener-method)
    - [use set_step_listener or first_step](#use-set_step_listener-or-first_step)
    - [why use set_step_listener after all decorators](#why-use-set_step_listener-after-all-decorators)
    - [StepHandler](#stephandler-class)
    - [Keyboards](#keyboards)
    - [Filters](#filters)
3. [Examples](#examples)
4. [TODO](#todo)
5. [Copyright & License](#license)

# Installing
Can use **pip**:
```bash
pip3 install -U pyrostep
```

Or, Can use **git** (not recommended):
```bash
git clone https://github.com/aWolver/pyrostep && cd pyrostep && python3 setup.py install
```

# Usage
Usage is very easy ... Follow me

> **before learn, You should know that this library only works as async.**

First import `pyrostep`:
```python
import pyrostep
```

`pyrostep` has a decorator named `first_step`, use this for handler which is first step, example:
```python
app = Client(...)
# ...

@app.on_message()
@pyrostep.first_step()
async def step1(cli: Client, msg: Message):
    await msg.reply_text("please send your name:")
    await pyrostep.register_next_step(msg.from_user.id, step2)

# create handler to get name:
async def step2(cli: Client, msg: Message):
    await msg.reply_text("Hello %s!" % msg.text)

    # unregister step2 in end step (don't forget it)
    await pyrostep.unregister_steps(msg.from_user.id)

# ...
```

you can use `ask` method instead of `register_next_step`:

```python
...
async def step1(cli: Client, msg: Message):
    pyrostep.ask(msg, step2, "please send your name:")
...
```

End of this code, you see `unregister_steps` method, you can use `end_step` decorator instead of it:
```python
...
@end_step()
async def step2(cli: Client, msg: Message):
    await msg.reply_text("Hello %s!" % msg.text)
...
```

#### set_step_listener method
`first_step` decorator may broken your code, so i recommended use `set_step_listener` instead of `first_step`.

Example:
```python
app = Client(...)
# ...

@app.on_message(filters=filters.command("sayhello"))
async def step1(cli: Client, msg: Message):
    await msg.reply_text("please send your name:")
    await pyrostep.register_next_step(msg.from_user.id, step2)

# create handler to get name:
async def step2(cli: Client, msg: Message):
    await msg.reply_text("Hello %s!" % msg.text)

    # unregister step2 in end step (don't forget it)
    await pyrostep.unregister_steps(msg.from_user.id)

# after all decorators
pyrostep.set_step_listener(app)

# ...
```

**Note: Better you use set_step_listener after all of decorators.**

#### Use set_step_listener or first_step?
to answer this, you should know how does `set_step_listener` and `first_step` works.

`first_step` decorator sets middleware on your handler/decorator. checks if this user in listening users or not, if true, call step functions, and if false, call default handler.

`set_step_listener` too. it sets a step listener handler without default decorator.

#### Why use `set_step_listener` after all decorators?
to check the pyrogram as the last method.

> If you want clear all steps for all users, use `clear` method.

## StepHandler *class*

You can use it to have a different steps handler:

```python
from pyrostep import StepHandler

h = StepHandler()
```

It has all of methods you want.

## Keyboards
import keyboards:
```python
from pyrostep import keyboards
```

Now see methods:

`split_list` splites lst list:
```python
>>> keyboards.split_list([1, 2, 3, 4, 5, 6], 2)
# [[1, 2], [3, 4], [5, 6]]
>>> keyboards.split_list([1, 2, 3], 2)
# [[1, 2], [3]]
```

`keyboard` creates ReplyKeyboardMarkup from your list:
```python
buttons = [
    [
        ["Top Left"], ["Top Right"]
    ],
    [
        ["Bottom | Request Contact", True, "request_contact"]
    ]
]
kb = keyboards.keyboard(buttons)
```

`inlinekeyboard` creates InlineKeyboardMarkup from your list:
```python
buttons = [
    [
        ["Top Left", "data_1"], ["Top Right", "data_2"]
    ],
    [
        ["Bottom", "Your URL", "url"]
    ]
]
ikb = inlinekeyboard(buttons)
```

## Filters
import filters:
```python
from pyrostep import filters
```

Now see filters:

`ttl_message`: Filter ttl messages ( ttl photo message or ttl video message ).

`video_sticker`: Filter video sticker messages.

`entities`: Filter messages include entities.

`photo_size`: Filter photo messages with width and height.

# Examples
See Examples [here](https://github.com/aWolver/pyrostep/tree/main/examples)

# TODO
- [x] Add examples
- [x] Add helper methods
- [ ] Do Other Tests

# License
Licensed under the terms of the **GNU Lesser General Public License v2**
