anekos
================

   An asynchronous wrapper for nekos.life API

Features
========

-  You can download the images! (using
   `aiofile <https://pypi.org/project/aiofile>`__)
-  Easy to use with an object-oriented design.

Install
=======

.. code:: sh

   # Linux/macOS
   python3 -m pip install -U anekos

   # Windows
   py -3 -m pip install -U anekos

To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/Nekos-life/Async-nekos.life-wrapper.git
    $ cd Async-nekos.life-wrapper
    $ python3 -m pip install -U .

Optional Packages
-----------------

-  `aiodns <https://pypi.org/project/aiodns>`__,
   `brotlipy <https://pypi.org/project/brotlipy>`__,
   `cchardet <https://pypi.org/project/cchardet>`__ (for aiohttp
   speedup)
-  `orjson <https://pypi.org/project/orjson>`__ (for json speedup)

Quick Example
=============

.. code:: py

   from anekos import NekosLifeClient, SFWImageTags
   from asyncio import get_event_loop

   client = NekosLifeClient()


   async def main():
       result = await client.image(SFWImageTags.WALLPAPER)
       print(result.url)


   loop = get_event_loop()
   loop.run_until_complete(main())

Links
=====
-  `Issues <https://github.com/Async-nekos.life-wrapper/issues>`__
