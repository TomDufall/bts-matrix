"""
Generic video matrix interface.

Some functions are included to reduce complex instructions to common simple
ones - if the complex instructions are supported in hardware, implement them!
"""

from abc import ABC, abstractmethod
from VirtualPresetController import VirtualPresetController

class Matrix(ABC):
    """
    Generic video matrix interface.

    Some functions are included to reduce complex instructions to common simple
    ones - if the complex instructions are supported in hardware, implement them!
    """
    def __init__(self, input_count, output_count, preset_controller=None):
        self.INPUT_COUNT = input_count
        self.OUTPUT_COUNT = output_count
        if preset_controller is None:
            self.PRESET_CONTROLLER = VirtualPresetController()
        else:
            self.PRESET_CONTROLLER = preset_controller

    def get_input_count(self):
        """Return the number of inputs on the matrix."""
        return self.INPUT_COUNT

    def get_output_count(self):
        """Return the number of inputs on the matrix."""
        return self.OUTPUT_COUNT

    @abstractmethod
    def patch(self, input_, output):
        """Patch the given input to the given output"""
        raise NotImplementedError

    def patch_pairs(self, patch_pairs):
        """
        A list of patch instructions, each given as a tuple {input, output}.
        """
        if not isinstance(patch_pairs, list):
            # Convert to a single-element list
            patch_pairs = [patch_pairs]
        for input_, output in patch_pairs:
            self.patch(input_, output)

    def patch_list(self, patch):
        """
        An ordered list of inputs, to be applied to outputs in order.
        I.e. [1, 1, 2, 3] implies in 1 -> out 1, in 1 -> out 2, etc
        """
        output = 1
        for input_ in patch:
            self.patch(input_, output)
            output += 1

    def patch_one_to_all(self, input_):
        """Patch the given input to every output"""
        for output in range(1, self.OUTPUT_COUNT + 1):
            self.patch(input_, output)

    def patch_one_to_one(self):
        """
        Patch in 1 -> out 1, in 2 -> out 2, etc.
        If more outputs than inputs, wrap and start counting from 1 again.
        """
        for i in range(0, self.OUTPUT_COUNT):
            self.patch((i % self.INPUT_COUNT) + 1, i + 1)

    @abstractmethod
    def get_patch(self):
        """
        Return the current routing table as an ordered list of inputs
        I.e. [1, 4, 7] implies [(in 1 -> out 1), (in 4 -> out 2), etc]
        """
        raise NotImplementedError

    @abstractmethod
    def blackout(self, outputs):
        """Black out the given outputs."""
        if not isinstance(outputs, list):
            # Convert to a single-element list
            outputs = [outputs]
        for output in outputs:
            raise NotImplementedError

    @abstractmethod
    def unblackout(self, outputs):
        """Restore the given outputs from blackout."""
        if not isinstance(outputs, list):
            # Convert to a single-element list
            outputs = [outputs]
        for output in outputs:
            raise NotImplementedError

    def blackout_all(self):
        """Black out every output."""
        for output in range(1, self.OUTPUT_COUNT + 1):
            self.blackout(output)

    def unblackout_all(self):
        """Restore every output from blackout."""
        for output in range(1, self.OUTPUT_COUNT + 1):
            self.unblackout(output)

    def apply_preset(self, preset_no):
        """Apply a numbered preset patch from the preset controller"""
        self.patch_list(self.PRESET_CONTROLLER.get(preset_no)[1])
