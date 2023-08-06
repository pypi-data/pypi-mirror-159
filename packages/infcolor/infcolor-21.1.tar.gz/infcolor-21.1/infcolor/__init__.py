try:
    import discord
    import DiscordUtils
    from discord.ext import *
    from discord.utils import *
    from discord_components import *
    from Cybernator import Paginator
    import asyncio
    import random
    import os, time
except Exception as import_libs_error:
    print(' [Libs] >>>  {0} '.format(import_libs_error))

global module_not_found, color_not_found, indexLab, all_colors_installed, all_rgb_colors, all_cmyk_colors
module_not_found = ' [System Error]: "This Module Has Not Found !" '
color_not_found = ' [System Error]: "This Color Has Not Found !" '
indexLab = int(21000)

other_colors = [
    "rgb() - [Rainbow Colors]", "cmyk() - [Real Colors]"
]

rgb_colors = [
    0xaaafff, 0xfffaaa, 0xe3f2fd, 0xbbdefb, 0x90caf9, 0x64b5f6, 0x42a5f5, 0xcae9ff, 0xe0aaff, 0xc77dff, 0xdcd6f7,
    0x97dffc, 0xeabaf6, 0x858ae3, 0xc1fba4, 0xb7efc5, 0x613dc1, 0xa9d3ed, 0x2176ff, 0xfdca40, 0xffee32, 0xc4c7ff,
    0xff70a6, 0xff9770, 0xe9ff70, 0xefd6ac, 0xe9b44c, 0x90f1ef, 0xc0fdfb, 0xafcbff, 0x2dc653, 0xb0d7ff, 0xc86bfa,
    0xffbc42, 0xe8ddb5, 0xa0c4e2, 0xcdc1ff, 0xfaae7b, 0xcc8b79, 0xb0d7ff, 0x9f6976, 0x3993cd, 0x7bf1a8, 0xa6b1e1,
    0xf7ffe0, 0x9457eb, 0x4166f5, 0x5b92e5, 0xff6fff, 0xf94d00, 0xfd5e53, 0x00ff7f, 0x0fc0fc, 0x6a5acd, 0x76ff7a, 
    0xffd800, 0xff2400, 0xff6700, 0xff0028, 0xe32636, 0x1fcecb, 0xff5a36, 0xd40000, 0x1c39bb, 0xff6961, 0xffb347, 
    0x77dd77, 0x98fb98, 0xeee8aa, 0xabcdef, 0x273be2, 0xff6e4a, 0xff4500, 0x00fa9a, 0x66ddaa, 0xff8243, 0x0bda51, 
    0x6050dc, 0xfbec5d, 0xaaf0d1, 0xe62020, 0xbfff00, 0x87cefa, 0xff9999, 0xffa07a, 0x7cfc00, 0xee82ee, 0x6668ff, 
    0xff6666, 0xf4bbff, 0xb2ffff, 0xfbec5d, 0xf4bbff, 0xfcf75e, 0xb2ec5d, 0x5a4fcf, 0xf8de7e, 0xbdda57, 0xfe2119, 
    0xe03c31, 0xff0800, 0xff2800, 0xff55a3, 0xff0040, 0xef3038, 0x6f00ff, 0x3f00ff, 0xff00ff, 0x00ffff, 0x007fff, 
    0x318ce7, 0x007aa5, 0x2a52be, 0x00bfff, 0x00ffff, 0x66ff00, 0x03c03c, 0x85bb65, 0x00ff00, 0xff8c00, 0xff9933,
    0x5da9e9, 0xf2ff49, 0xffef9f, 0x826aed, 0x3bf4fb, 0xcaff8a, 0xb2f7ef, 0xf7d6e0, 0xfcdfa6, 0xffadad, 0xf3de8a,
    0xfdee00, 0xfff600, 0xffa812, 0xccff00, 0x00fff8, 0x16db65, 0xef2917, 0xc9182c, 0xeee2df, 0x9dcee2, 0xfcb9b2,
    0xfdc5f5, 0x72ddf7, 0xffdc5e, 0xb8d8ba, 0xd9dbbc, 0xef233c, 0xc200fb, 0xfc2f00, 0xffcb69, 0xc6d2ed, 0xf87575,
    0xffd400, 0xf2a65a, 0xf58549, 0x3a7ca5, 0xdde7c7, 0x73d2de, 0xffbf81, 0x00a8e8, 0xffcb69, 0xffdc5e, 0xff69eb,
    0xffe3e0, 0xbbd686, 0xeef1bd, 0xf7a9a8, 0xb9e6ff, 0xb388eb, 0xffba08, 0xd00000, 0xfaa307, 0xe85d04, 0xf48c06,
    0xf25757, 0x33ccaa, 0xff66b3, 0xffb7ff, 0xc879ff, 0x9bf6ff, 0xffc6ff, 0xffd6a5, 0xddc9b4, 0xfbd1a2, 0xf2b5d4,
    0xd9ed92, 0xb5e48c, 0xe1ecf7, 0xcfbaf0, 0xf5cb5c, 0xfb8b24, 0x0aff99, 0x580aff, 0x9ef01a, 0xfde4cf, 0x98c9a3,
    0xccff33, 0xb2dbbf, 0xb9fbc0, 0x98f5e1, 0x90caf9, 0xffc300, 0x147df5, 0xf7a399, 0xff8700, 0xffd000, 0xe56b6f,
    0xef233c, 0x99d98c, 0xe7e6f7, 0xef6351, 0xffcfd2, 0x70e000, 0xeaac8b, 0x70c1b3, 0xffe1a8, 0xffea00, 0xf3ffbd,
    0xf2542d, 0xdeff0a, 0xff8700, 0xff0000, 0xff002b, 0xff99c8, 0xa1ff0a, 0x580aff, 0xccff33, 0x70e000, 0xf94144,
    0xfdfffc, 0x011627, 0x6fffe9, 0x2d00f7, 0x6a00f4, 0x8900f2, 0xa100f2, 0xbc00dd, 0x7371fc, 0xa594f9, 0xcdc1ff,
    0xdbfeb8, 0x99ddc8, 0xff8500, 0x6247aa, 0x33ccaa, 0x6a66a3, 0xfd390b, 0x449dd1, 0x192bc2, 0xc5edac, 0xff0054,
    0x90f1ef, 0xffd6e0, 0x7bf1a8, 0xc1fba4, 0x7bdff2, 0x80ffdb, 0xa0c4ff, 0x4361ee, 0xffddd2, 0xcaffbf, 0x00b2ca,
    0xff0000, 0xff8700, 0xffd300, 0xdeff0a, 0xa1ff0a, 0x0aff99, 0x0aefff, 0x147df5, 0x580aff, 0xbe0aff, 0xffc857
]
rgb_lenColors = len(rgb_colors)

cmyk_colors = [
    0xfffeee
]
cmyk_lenColors = len(cmyk_colors)


all_colors_installed = (rgb_lenColors + cmyk_lenColors)
all_rgb_colors = (rgb_lenColors)
all_cmyk_colors = (cmyk_lenColors)


class InfColor:
    """
    `The MIT License (MIT)`
    `Copyright (c) 2021-present. "adamsonScripts"`
    `Discord: "adamsonScripts#3624"`

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
    """
    def __init__(self):
        self.info = (21)
        self.rgb = (21)
        self.cmyk = (21)
        self.adless = (21)
        self.godness = (21)

    def info(self):
        """
        `The MIT License (MIT)`

        `Copyright (c) 2021-present. "adamsonScripts"`
        `Discord: "adamsonScripts#3624"`

        Permission is hereby granted, free of charge, to any person obtaining a
        copy of this software and associated documentation files (the "Software"),
        to deal in the Software without restriction, including without limitation
        the rights to use, copy, modify, merge, publish, distribute, sublicense,
        and/or sell copies of the Software, and to permit persons to whom the
        Software is furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in
        all copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
        OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
        FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
        DEALINGS IN THE SOFTWARE.
        """
        try:
            print()
            print(' -----|[ONLY FOR DISCORD BOTS]|-----')
            print()
            print(' -----|[INFORMATION OF MENU]|-----')
            print()
            print(' [{0}]: All Colors Installed. '.format(all_colors_installed))
            print()
            print(' [{0}]: "All RGB Colors." '.format(all_rgb_colors))
            print()
            print(' [{0}]: "All CMYK Colors." '.format(all_cmyk_colors))
            print()
            print(' -----|[INFORMATION OF MENU]|-----')
            print()
            print()
            print(' -----|[HELPOP OF OPTIONS]|-----')
            print()
            print(' "color = InfColor.rgb(0)" > For Select RGB_COLORS ')
            print()
            print(' "color = InfColor.cmyk(0)" > For Select CMYK_COLORS ')
            print()
            print(' "color = InfColor.adless(0)" > For Select AD_COLOR ')
            print()
            print(' "color = InfColor.godness(0)" > For Select GOD_COLOR ')
            print()
            print(' -----|[HELPOP OF OPTIONS]|-----')
            print()
            print(' -----|[ONLY FOR DISCORD BOTS]|-----')
        except:
            print(module_not_found)


    def rgb(self):
        try:
            setRGB = (lambda x: random.choice(x))(rgb_colors)
            return setRGB
        except:
            print(module_not_found + ' >>> [RGB] ')

    def cmyk(self):
        try:
            setCMYK = (lambda x: random.choice(x))(cmyk_colors)
            return setCMYK
        except:
            print(module_not_found + ' >>> [CMYK] ')

    def adless(self):
        return (0xaaafff)

    def godness(self):
        return (0xfffaaa)
