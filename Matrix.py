# This is an abstract Matrix. An implementation should use this class to communicate with the matrix, for example, over serial protocol
# Some functions are included to reduce more complex instructions to common simple ones - if the more complex instructions are supported, use them!

# enable abstract classes
from abc import ABC, abstractmethod

class Matrix(ABC):

    def __init__(self, input_count, output_count):
        self.INPUT_COUNT = input_count
        self.OUTPUT_COUNT = output_count

    def getInputCount(self):
        "Return the number of inputs on the matrix."
        return self.IN_COUNT

    def getOutputCount(self):
        "Return the number of inputs on the matrix."
        return self.OUT_COUNT

    @abstractmethod
    def patch(self, output, input):
        "Patch an input [1-n] to an output [1-n]"

    def patchMulti(self, patch):
        "A list of patch instructions, each given as a tuple {output, input}"
        for output, input in patch:
            self.patch(output, input)

    def patchList(self, patch):
        "An ordered list of inputs, to be applied to outputs in order. I.e. 1, 1, 2, 3 implies 1->1, 1->2, 2->2, 3->3"
        output = 1
        for input in patch:
            self.patch(output, input)
            output += 1

    def patchAll(self, input):
        "Patch the given input to every output"
        for output in range(1, self.OUTPUT_COUNT + 1):
            self.patch(output, input)

    def patchOneToOne(self):
        "Patch 1->1, 2->2, etc. If more outputs than inputs, follow default hardware behaviour, or keep using the final input."
        for i in range(1, self.OUTPUT_COUNT + 1):
            self.patch(i, min(i, INPUT_COUNT))

    @abstractmethod
    def getRoutingTable(self):
        "Return the current routing table as a list of {output, input} tuples."

    @abstractmethod
    def blackout(self, output):
        "Black out the given output."

    @abstractmethod
    def unblackout(self, output):
        "Restore the given output from blackout."

    def blackoutMulti(self, outputs):
        "Blackout the given outputs."
        for output in outputs:
            self.blackout(output)

    def unblackoutMulti(self, outputs):
        "Restore the given outputs from blackout."
        for output in outputs:
            self.unblackout(output)

    def blackoutAll(self):
        "Black out every output."
        for output in range(1, self.OUTPUT_COUNT + 1):
            self.blackout(output)

    def unblackoutAll(self):
        "Restore every output from blackout."
        for output in range(1, self.OUTPUT_COUNT + 1):
            self.unblackout(output)
