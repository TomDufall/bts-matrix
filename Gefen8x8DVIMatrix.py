# Gefen 8x8 DVI Matrix controller over serial

from Matrix import Matrix
# requires pyserial
import serial as pyserial

class Gefen8x8DVIMatrix(Matrix):

    def __init__(self, serial_port):
        super().__init__(input_count = 8, output_count = 8)
        self.serial = pyserial.Serial()
        self.serial.port = serial_port
        # Hard coded serial settings from the matrix manual
        self.serial.baudrate = 19200
        self.serial.bytesize = 8
        self.serial.parity = 'N'
        self.serial.stopbits = 1
        self.serial.timeout = 2 # May need to tweak during testing
        self.serial.open()

    def toLetter(self, number):
        "Convert a number to its corresponding letter in the alphabet (1-indexed). 1->A, 2->B, etc."
        return chr(number + 96).upper()

    def send(self, msg):
        "Send a string over serial"
        self.serial.write(str.encode(msg))

    def sendLine(self, msg):
        "Send a string over serial with a carriage return"
        self.send(msg + '\r')

    def patch(self, output, input):
        "Patch an input [1-n] to an output [1-n]"
        self.send('{}'.format(self.toLetter(output) + str(input)))

    def getRoutingTable(self):
        "Return the current routing table as a list of {output, input} tuples."
        # need to implement reading from serial - need to test with hardware to find format to parse
        self.send('M')

    def blackout(self, output):
        "Black out the given output."
        self.sendLine('#MASK {}'.format(self.toLetter(output)))

    def unblackout(self, output):
        "Restore the given output from blackout."
        self.sendLine('#UNMASK {}'.format(self.toLetter(output)))

    def blackoutMulti(self, outputs):
        "Blackout the given outputs."
        str = '#MASK'
        for output in outputs:
            str += ' {}'.format(self.toLetter(output))
        self.sendLine(str)

    def unblackoutMulti(self, outputs):
        "Restore the given outputs from blackout."
        str = '#UNMASK'
        for output in outputs:
            str += ' {}'.format(self.toLetter(output))
        self.sendLine(str)

    def blackoutAll(self):
        "Black out every output."
        str = '#MASK'
        for output in range(1, self.OUTPUT_COUNT + 1):
            str += ' {}'.format(self.toLetter(output))
        self.sendLine(str)

    def unblackoutAll(self):
        "Restore every output from blackout."
        str = '#MASK'
        for output in range(1, self.OUTPUT_COUNT + 1):
            str += ' {}'.format(self.toLetter(output))
        self.sendLine(str)
