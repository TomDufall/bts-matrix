# Debug/dev virtual matrix - prints text versions of matrix actions to the terminal

from Matrix import Matrix

class PrintMatrix(Matrix):

    def __init__(self, input_count, output_count):
        super().__init__(input_count, output_count)

    def patch(self, output, input):
        "Patch an input [1-n] to an output [1-n]"
        print('Patch input {} to output {}'.format(input, output))

    def patchMulti(self, patch):
        "A list of patch instructions, each given as a tuple {output, input}"
        print('Not yet implemented in text')

    def patchList(self, patch):
        "An ordered list of inputs, to be applied to outputs in order. I.e. 1, 1, 2, 3 implies 1->1, 1->2, 2->2, 3->3"
        print('Not yet implemented in text')

    def patchAll(self, input):
        "Patch the given input to every output"
        print('Patching all outputs to input {}'.format(input))

    def patchOneToOne(self):
        "Patch 1->1, 2->2, etc. If more outputs than inputs, follow default hardware behaviour, or keep using the final input."
        print('Patching all outputs one to one')

    def getRoutingTable(self):
        "Return the current routing table as a list of {output, input} tuples."
        print('Not yet implemented in text')

    def blackout(self, output):
        "Black out the given output."
        print('Blacking out output {}'.format(output))

    def unblackout(self, output):
        "Restore the given output from blackout."
        print('Restoring from blackout output {}'.format(output))

    def blackoutMulti(self, inputs):
        "Blackout the given outputs."
        print('Not yet implemented in text')

    def unblackoutMulti(self, inputs):
        "Restore the given outputs from blackout."
        print('Not yet implemented in text')

    def blackoutAll(self):
        "Black out every output."
        print('Blacking out all outputs')

    def unblackoutAll(self):
        "Restore every output from blackout."
        print('Un-blacking out all outputs')
