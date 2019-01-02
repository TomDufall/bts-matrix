# This is an abstract preset controller
# A preset controller should store IO patch presets and recall them as required
# It may be hardware-based, software-based, or hybrid. It should support unlimited presets.

from abc import ABC, abstractmethod

class PresetController(ABC):

    def __init__(self):


    @abstractmethod
    def save(self, saves):
        "A tuple or list of tuples (presetNo, [patchlist]). Save each preset."
        if isinstance(saves, list) != True:
            # Convert to a single-element list
            saves = [saves]
        for presetNo, patchlist in saves:
            pass

    @abstractmethod
    def move(self, moveList):
        "A tuple or list of tuples (preset1, preset2). Renumber preset1 as preset2, overwriting preset2 if present."
        if isinstance(moveList, list) != True:
            # Convert to a single-element list
            moveList = [moveList]
        for preset1, preset2 in moveList:
            pass

    @abstractmethod
    def apply(self, presetNo):


    @abstractmethod
    def get(self, presetNos):


    @abstractmethod
    def getAll(self):


    @abstractmethod
    def delete(self, presetNos):

    @abstractmethod
    def deleteAll(self):


    @abstractmethod
    def exists(self, presetNos):
        
