class Model:
    width = 800
    height = 600

    re_start = -2
    re_end = 1
    im_start = -1
    im_end = 1

    c_real = 0.285
    c_imag = 0.01

    const_max_iterations = 256

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_re_start(self, re_start):
        self.re_start = re_start

    def get_re_start(self):
        return self.re_start

    def set_re_end(self, re_end):
        self.re_end = re_end

    def get_re_end(self):
        return self.re_end

    def set_im_start(self, im_start):
        self.im_start = im_start

    def get_im_start(self):
        return self.im_start

    def set_im_end(self, im_end):
        self.im_end = im_end

    def get_im_end(self):
        return self.im_end

    def set_c_real(self, c_real):
        self.c_real = c_real

    def get_c_real(self):
        return self.c_real

    def set_c_imag(self, c_imag):
        self.c_imag = c_imag

    def get_c_imag(self):
        return self.c_imag
    