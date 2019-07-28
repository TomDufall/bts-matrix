"""
Gefen8x8DVIMatrix is a DVI video matrix that can be controlled over serial.
It does not have audio capabilities.
"""
# Gefen 8x8 DVI Matrix controller over serial

from serial import Serial

# Implements the Matrix interface
from Matrix import Matrix

class Gefen8x8DVIMatrix(Matrix):
    """
    Implement the Matrix interface over serial
    The correct serial port should be identified before instantiating this
    class - it cannot automatically detect compatible matrixes
    """

    def __init__(self, serial_port):
        super().__init__(input_count=8, output_count=8)
        # Set up serial port
        self.serial = Serial()
        self.serial.port = serial_port
        # Hard coded serial settings from the matrix manual
        self.serial.baudrate = 19200
        self.serial.bytesize = 8
        self.serial.parity = 'N'
        self.serial.stopbits = 1
        self.serial.timeout = 2 # May need to tweak during testing

    _TO_LETTER_MAPPING = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    @classmethod
    def to_letter(cls, index):
        """
        Convert a number to its corresponding letter in the alphabet (1-indexed)
        i.e. 1->A, 2->B, etc.
        Matrix goes up to 8 - error if higher
        """
        return cls._TO_LETTER_MAPPING[index - 1]

    def send(self, msg):
        """Send the given message over the serial connection"""
        with self.serial.open() as serial:
            serial.write(str.encode(msg))

    def send_line(self, msg):
        """
        Send the given message over the serial connection as a send_line
        This matrix uses a carriage return rather than a newline
        """
        self.send(msg + '\r')

    def patch(self, input_, output):
        """Patch the given input to the given output"""
        print(input_, output)
        self.send('{}'.format(self.to_letter(output) + str(input_)))

    def get_patch(self):
        """
        Return the current routing table as an ordered list of inputs
        i.e. [1, 4, 7] implies [(in 1 -> out 1), (in 4 -> out 2), etc]
        """
        # need to implement reading from serial
        # need to test with hardware to find format to parse
        # self.send('M')
        raise NotImplementedError

    def blackout(self, outputs):
        """Black out the given outputs."""
        if not isinstance(outputs, list):
            # Convert to a single-element list
            outputs = [outputs]
        msg = '#MASK'
        for output in outputs:
            msg += ' {}'.format(self.to_letter(output))
        self.send_line(msg)

    def unblackout(self, outputs):
        """Restore the given outputs from blackout."""
        if not isinstance(outputs, list):
            # Convert to a single-element list
            outputs = [outputs]
        msg = '#UNMASK'
        for output in outputs:
            msg += ' {}'.format(self.to_letter(output))
        self.send_line(msg)

    def blackout_all(self):
        """Black out every output."""
        msg = '#MASK'
        for output in range(1, self.OUTPUT_COUNT + 1):
            msg += ' {}'.format(self.to_letter(output))
        self.send_line(msg)

    def unblackout_all(self):
        """Restore every output from blackout."""
        msg = '#MASK'
        for output in range(1, self.OUTPUT_COUNT + 1):
            msg += ' {}'.format(self.to_letter(output))
        self.send_line(msg)
