from PIL import Image, ImageDraw
from math import log, log2, pi, e


class Julia:

    def draw(self, m):

        img = Image.new(mode='RGB', size=(m.width, m.height), color=(256, 256, 256))
        draw = ImageDraw.Draw(img)

        c = complex(m.c_real, m.c_imag)

        for x in range(0, m.width):
            for y in range(0, m.height):

                z0 = complex(m.re_start + ((float(x) / float(m.width)) * (m.re_end - m.re_start)),
                             m.im_start + ((float(y) / float(m.height)) * (m.im_end - m.im_start)))

                z = z0
                n = 0

                while abs(z) <= 2 and n < m.const_max_iterations:
                    z = z * z + c
                    n += 1

                if n != m.const_max_iterations:
                    zn = n + 1 - log(log(log2(abs(z)))) * pi * e
                else:
                    zn = n

                color = 256 - int(zn)
                draw.point([x, y], (color, color, color))

        img.show()
