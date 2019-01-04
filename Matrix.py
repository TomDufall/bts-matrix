# This is an abstract Matrix. An implementation should use this class to communicate with the matrix, for example, over serial protocol
# Some functions are included to reduce more complex instructions to common simple ones - if the more complex instructions are supported, use them!

# enable abstract classes
from abc import ABC, abstractmethod
from VirtualPresetController import VirtualPresetController

class Matrix(ABC):

    def __init__(self, input_count, output_count, presetController=None):
        self.INPUT_COUNT = input_count
        self.OUTPUT_COUNT = output_count
        if presetController is None:
            self.presetController = VirtualPresetController()
        else:
            self.presetController = presetController

    def getInputCount(self):
        "Return the number of inputs on the matrix."
        return self.IN_COUNT

    def getOutputCount(self):
        "Return the number of inputs on the matrix."
        return self.OUT_COUNT

    @abstractmethod
    def patch(self, patchPair):
        "A list of patch instructions, each given as a tuple {output, input}. Patch the input to the output."
        if isinstance(patchPair, list) != True:
            # Convert to a single-element list
            patchPair = [patchPair]
        for output, input in patchPair:
            pass

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
        "Patch 1->1, 2->2, etc. If more outputs than inputs, wrap and start counting from 1 again."
        for output in range(0, self.OUTPUT_COUNT):
            self.patch(output, (output % self.INPUT_COUNT) + 1)

    @abstractmethod
    def getPatch(self):
        "Return the current routing table as a list of {output, input} tuples."

    @abstractmethod
    def blackout(self, outputs):
        "Blackout the given outputs."
        if isinstance(outputs, list) != True:
            # Convert to a single-element list
            outputs = [outputs]
        for output in outputs:
            pass

    @abstractmethod
    def unblackout(self, outputs):
        "Restore the given outputs from blackout."
        if isinstance(outputs, list) != True:
            # Convert to a single-element list
            outputs = [outputs]
        for output in outputs:
            pass

    def blackoutAll(self):
        "Black out every output."
        for output in range(1, self.OUTPUT_COUNT + 1):
            self.blackout(output)

    def unblackoutAll(self):
        "Restore every output from blackout."
        for output in range(1, self.OUTPUT_COUNT + 1):
            self.unblackout(output)

    def applyPreset(self, presetNo):
        self.patchList(self.presetController.get(presetNo)[1])
