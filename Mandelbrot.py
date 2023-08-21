
from Model import Model as m
from PIL import Image, ImageDraw

class Mandelbrot:

    def draw(self):

        img = Image.new(mode='RGB', size=(m.width, m.height), color=(256, 256, 256))
        draw = ImageDraw.Draw(img)

        for x in range(0, m.width):
            for y in range(0, m.height):

                c = complex(m.re_start + ((float(x) / float(m.width)) * (m.re_end - m.re_start)),
                            m.im_start + ((float(y) / float(m.height)) * (m.im_end - m.im_start)))

                z = 0
                n = 0
                while abs(z) <= 2 and n < m.const_max_iterations:
                    z = z * z + c
                    n += 1

                color = 256 - n
                draw.point([x, y], (color, color, color))

        img.show()