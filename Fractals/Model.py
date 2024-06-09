class Model:
    """Class with variables used in generating fractals. Contains methods to set and get the variables."""
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
        """Method to set the value of image width."""
        self.width = width

    def get_width(self):
        """Method to get the value of image width."""
        return self.width

    def set_height(self, height):
        """Method to set the value of image height."""
        self.height = height

    def get_height(self):
        """Method to get the value of image height."""
        return self.height

    def set_re_start(self, re_start):
        """Method to set the starting value of real part of fractal, later converted to coordinates."""
        self.re_start = re_start

    def get_re_start(self):
        """Method to get the starting value of real part of fractal, later converted to coordinates."""
        return self.re_start

    def set_re_end(self, re_end):
        """Method to set the ending value of real part of fractal, later converted to coordinates."""
        self.re_end = re_end

    def get_re_end(self):
        """Method to get the ending value of real part of fractal, later converted to coordinates."""
        return self.re_end

    def set_im_start(self, im_start):
        """Method to set the starting value of imaginary part of fractal, later converted to coordinates."""
        self.im_start = im_start

    def get_im_start(self):
        """Method to get the starting value of imaginary part of fractal, later converted to coordinates."""
        return self.im_start

    def set_im_end(self, im_end):
        """Method to set the ending value of imaginary part of fractal, later converted to coordinates."""
        self.im_end = im_end

    def get_im_end(self):
        """Method to get the ending value of imaginary part of fractal, later converted to coordinates."""
        return self.im_end

    def set_c_real(self, c_real):
        """Method to set the real part of constant used in algorithm to calculate the Julia set."""
        self.c_real = c_real

    def get_c_real(self):
        """Method to get the real part of constant used in algorithm to calculate the Julia set."""
        return self.c_real

    def set_c_imag(self, c_imag):
        """Method to set the imaginary part of constant used in algorithm to calculate the Julia set."""
        self.c_imag = c_imag

    def get_c_imag(self):
        """Method to get the imaginary part of constant used in algorithm to calculate the Julia set."""
        return self.c_imag
    