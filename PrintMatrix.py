# Debug/dev virtual matrix - prints text versions of matrix actions to the terminal

from Matrix import Matrix

class PrintMatrix(Matrix):

    def __init__(self, input_count, output_count):
        super().__init__(input_count, output_count)

    def patch(self, patchPair):
        "A list of patch instructions, each given as a tuple {output, input}. Patch the input to the output."
        if isinstance(patchPair, list) != True:
            # Convert to a single-element list
            patchPair = [patchPair]
        try:
            for output, input in patchPair:
                print('Patch input {} to output {}'.format(input, output))
        except TypeError:
            raise TypeError('Inappropriate argument type. Argument patchPair should be a tuple or list of tuples')

    def patchAll(self, input):
        "Patch the given input to every output"
        print('Patching all outputs to input {}'.format(input))

    def patchOneToOne(self):
        "Patch 1->1, 2->2, etc. If more outputs than inputs, wrap and start counting from 1 again."
        print('Patching all outputs one to one')

    def getPatch(self):
        "Return the current routing table as a list of {output, input} tuples."
        print('Getting patch table from matrix')

    def blackout(self, outputs):
        "Blackout the given outputs."
        if isinstance(outputs, list) != True:
            # Convert to a single-element list
            outputs = [outputs]
        for output in outputs:
            print('Blacking out output {}'.format(output))

    def unblackout(self, outputs):
        "Restore the given outputs from blackout."
        if isinstance(outputs, list) != True:
            # Convert to a single-element list
            outputs = [outputs]
        for output in outputs:
            print('Restoring from blackout output {}'.format(output))

    def blackoutAll(self):
        "Black out every output."
        print('Blacking out all outputs')

    def unblackoutAll(self):
        "Restore every output from blackout."
        print('Restoring all outputs from blackout')
