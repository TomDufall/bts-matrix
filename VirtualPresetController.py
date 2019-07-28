"""
VirtualPresetController acts as a preset controller for matrixes without
hardware support for presets.
"""

import random
from PresetController import PresetController

class VirtualPresetController(PresetController):
    """
    VirtualPresetController acts as a preset controller for matrixes without
    hardware support for presets.
    """
    def __init__(self):
        super().__init__()
        self._presets = {}

    def delete_all_presets(self):
        """
        Delete all preset in the preset controller.
        """
        # Clear the presets dict
        self._presets = {}

    def delete_preset(self, preset_id):
        """
        Delete the given preset id.
        """
        try:
            del self._presets[preset_id]
        except KeyError:
            # Preset doesn't exist to be deleted
            pass

    def get_preset(self, preset_id):
        """
        Return the patchlist for the given preset id.
        If the preset doesn't exist, return None.
        [patchlist] is a list of inputs to be assigned to outputs in order.
        e.g. [1, 3, 4] implies in 1 -> out 1, in 3 -> out 2, in 4 -> out 3.
        """
        return self._presets.pop(preset_id, None)

    def get_all_presets(self):
        """
        For each stored preset, return (preset_id, patchlist).
        [patchlist] is a list of inputs to be assigned to outputs in order.
        e.g. [1, 3, 4] implies in 1 -> out 1, in 3 -> out 2, in 4 -> out 3.
        """
        return [(preset_id, self._presets[preset_id])
                for preset_id in self._presets]

    def list_presets(self):
        """
        List all preset ids currently in use.
        """
        return [preset_id for preset_id in self._presets]

    def move_preset(self, preset1, preset2):
        """
        Rename preset 1 as preset 2, overwriting preset 2, if present.
        """
        patchlist = self._presets.pop(preset1, None)
        if patchlist is not None:
            self._presets[preset2] = patchlist
            self.delete_preset(preset1)

    def preset_id_in_use(self, preset_id):
        """
        Return True if preset exists, else False.
        """
        return preset_id in self._presets

    @staticmethod
    def random_string(length=6):
        """
        Generate a random string of a given length.
        Length defaults to 6.
        """
        str_ = ''
        for _ in range(length):
            str_ += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return str_

    def save_preset(self, patchlist):
        """
        Save the given patchlist in any free preset id.
        Return the id chosen, or None if failed (e.g. run out of ids).
        [patchlist] is a list of inputs to be assigned to outputs in order.
        e.g. [1, 3, 4] implies in 1 -> out 1, in 3 -> out 2, in 4 -> out 3.
        """
        # Use random string as id, making name collision unlikely
        for _ in range(3):
            preset_id = self.random_string()
            if not self.preset_id_in_use(preset_id):
                self.set_preset(preset_id, patchlist)
                return preset_id
        # 3 attempts failed - return None for failure
        return None

    def set_preset(self, preset_id, patchlist):
        """
        Save the given patchlist as the given preset id.
        [patchlist] is a list of inputs to be assigned to outputs in order.
        e.g. [1, 3, 4] implies in 1 -> out 1, in 3 -> out 2, in 4 -> out 3.
        """
        self._presets[preset_id] = patchlist
