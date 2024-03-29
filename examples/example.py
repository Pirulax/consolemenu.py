#  SPDX-FileCopyrightText: 2024 Pirulax <patrikjankovics7@gmail.com>
#  SPDX-License-Identifier: MIT

import asyncio
import consolemenu_py as cm

async def main():
    # Create the main menu. The name should usually be the name of your program
    mm = cm.MainMenu("Example Program")

    # This will enter an empty sub-menu
    mm.add_item(cm.Menu("A sub-menu!"))

    # This will print "Hello World!" to the console
    mm.add_item(cm.FunctionMenuItem("A function menu item", lambda _: print("Hello World!")))

    # This will only return if the user exists the main menu
    await mm.run()

if __name__ == "__main__":
    asyncio.run(main())
