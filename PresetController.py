# This is an abstract preset controller
# A preset controller should store IO patch presets and recall them as required
# It may be hardware-based, software-based, or hybrid. It should support unlimited presets.

from abc import ABC, abstractmethod

class PresetController(ABC):

    def __init__(self):


    @abstractmethod
    def save(self, presetNo, patchList):


    @abstractmethod
    def saveMulti(self, saves):


    @abstractmethod
    def move(self, presetNo1, presetNo2):


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
        
