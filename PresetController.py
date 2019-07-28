"""
Manages matrix presets - saved input-output mapping configurations.
"""

from abc import ABC, abstractmethod

class PresetController(ABC):
    """
    Manages matrix presets - saved input-output mapping configurations.
    """
    def __init__(self):
        pass

    @abstractmethod
    def delete_all_presets(self):
        """
        Delete all preset in the preset controller.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_preset(self, preset_id):
        """
        Delete the given preset id.
        """
        raise NotImplementedError

    @abstractmethod
    def get_preset(self, preset_id):
        """
        Return the patchlist for the given preset id.
        If the preset doesn't exist, return None.
        [patchlist] is a list of inputs to be assigned to outputs in order.
        e.g. [1, 3, 4] implies in 1 -> out 1, in 3 -> out 2, in 4 -> out 3.
        """
        raise NotImplementedError

    @abstractmethod
    def get_all_presets(self):
        """
        For each stored preset, return (preset_id, patchlist).
        [patchlist] is a list of inputs to be assigned to outputs in order.
        e.g. [1, 3, 4] implies in 1 -> out 1, in 3 -> out 2, in 4 -> out 3.
        """
        raise NotImplementedError

    @abstractmethod
    def list_presets(self):
        """
        List all preset ids currently in use.
        """
        raise NotImplementedError

    @abstractmethod
    def move_preset(self, preset1, preset2):
        """
        Rename preset 1 as preset 2, overwriting preset 2, if present.
        """
        raise NotImplementedError

    @abstractmethod
    def preset_id_in_use(self, preset_id):
        """
        Return True if preset exists, else False.
        """
        raise NotImplementedError

    @abstractmethod
    def save_preset(self, patchlist):
        """
        Save the given patchlist in any free preset id.
        Return the id chosen, or None if failed (e.g. run out of ids).
        [patchlist] is a list of inputs to be assigned to outputs in order.
        e.g. [1, 3, 4] implies in 1 -> out 1, in 3 -> out 2, in 4 -> out 3.
        """
        raise NotImplementedError

    @abstractmethod
    def set_preset(self, preset_id, patchlist):
        """
        Save the given patchlist as the given preset id.
        [patchlist] is a list of inputs to be assigned to outputs in order.
        e.g. [1, 3, 4] implies in 1 -> out 1, in 3 -> out 2, in 4 -> out 3.
        """
        raise NotImplementedError

    def set_presets(self, saves):
        """
        Save the given list of preset ids and patchlists.
        saves is a list of (preset_id, patchlist) tuples.
        [patchlist] is a list of inputs to be assigned to outputs in order.
        e.g. [1, 3, 4] implies in 1 -> out 1, in 3 -> out 2, in 4 -> out 3.
        """
        for (preset_id, patchlist) in saves:
            self.set_preset(preset_id, patchlist)
