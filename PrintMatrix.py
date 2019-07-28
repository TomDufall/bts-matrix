"""
Text-based matrix for debugging or testing systems that use a Matrix.
Prints descriptions of actions when called.
"""

from Matrix import Matrix

class PrintMatrix(Matrix):
    """
    Text-based matrix for debugging or testing systems that use a Matrix.
    Prints descriptions of actions when called.
    """

    def __init__(self, input_count, output_count):
        super().__init__(input_count, output_count)

    def patch(self, input_, output):
        print('Patch input {} to output {}'.format(input_, output))

    def patch_pairs(self, patch_pairs):
        """
        A list of patch instructions, each given as a tuple {input, output}.
        """
        if not isinstance(patch_pairs, list):
            # Convert to a single-element list
            patch_pairs = [patch_pairs]
        try:
            for output, input_ in patch_pairs:
                print('Patch input {} to output {}'.format(input_, output))
        except TypeError:
            raise TypeError('Inappropriate argument type. Argument patchPair \
                            should be a tuple or list of tuples')

    def patch_one_to_all(self, input_):
        """Patch the given input to every output"""
        print('Patching all outputs to input {}'.format(input_))

    def patch_one_to_one(self):
        """
        Patch in 1 -> out 1, in 2 -> out 2, etc.
        If more outputs than inputs, wrap and start counting from 1 again.
        """
        print('Patching all outputs one to one')

    def get_patch(self):
        """
        Return the current routing table as an ordered list of inputs
        I.e. [1, 4, 7] implies [(in 1 -> out 1), (in 4 -> out 2), etc]
        """
        print('Getting patch table from matrix')

    def blackout(self, outputs):
        """Black out the given outputs."""
        if not isinstance(outputs, list):
            # Convert to a single-element list
            outputs = [outputs]
        for output in outputs:
            print('Blacking out output {}'.format(output))

    def unblackout(self, outputs):
        """Restore the given outputs from blackout."""
        if not isinstance(outputs, list):
            # Convert to a single-element list
            outputs = [outputs]
        for output in outputs:
            print('Restoring from blackout output {}'.format(output))

    def blackout_all(self):
        """Black out every output."""
        print('Blacking out all outputs')

    def unblackout_all(self):
        """Restore every output from blackout."""
        print('Restoring all outputs from blackout')
