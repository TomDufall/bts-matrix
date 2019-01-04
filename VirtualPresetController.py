# Virtual preset controller - does not require Matrix hardware

from PresetController import PresetController

class VirtualPresetController(PresetController):

    def __init__(self):
        self.presets = []

    def save(self, saves):
        "A tuple or list of tuples (presetNo, [patchlist]). Save each preset."
        if isinstance(saves, list) != True:
            # Convert to a single-element list
            saves = [saves]
        for presetNo, patchlist in saves:
            if isinstance(presetNo, int) and (patchlist is not None):
                if self.exists(presetNo):
                    self.presets = list(map(lambda preset: (preset[0], patchlist) if preset[0] == presetNo else preset, self.presets))
                else:
                    self.presets.append((presetNo, patchlist))

    def move(self, moveList):
        "A tuple or list of tuples (preset1, preset2). Renumber preset1 as preset2, overwriting preset2 if present. Identified by number."
        if isinstance(moveList, list) != True:
            # Convert to a single-element list
            moveList = [moveList]
        for preset1, preset2 in moveList:
            preset = self.get(preset1)
            if preset[1] is None:
                continue
            self.delete(preset2)
            self.presets = list(map(lambda preset: (preset2, preset[1]) if preset[0] == preset1 else preset, self.presets))

    def get(self, presetNos):
        "Return the patchlist for the requested preset. If multiple presetNos, return a list of (patchNo, patchList) tuples."
        if isinstance(presetNos, list) != True:
            # Single presetNo
            return next((tup for tup in self.presets if tup[0] == presetNos), (presetNos, None))
        else:
            response = []
            for presetNo in presetNos:
                response.append(next((tup for tup in self.presets if tup[0] == presetNo), (presetNo, None)))
            return response # [(presetNo, patchList)]

    def getAll(self):
        return self.presets

    def delete(self, presetNos):
        "Delete the requested preset(s)."
        if isinstance(presetNos, list) != True:
            # Convert to a single-element list
            presetNos = [presetNos]
        for presetNo in presetNos:
            try:
                self.presets.remove(self.get(presetNo))
            except ValueError:
                # If not in list, ignore
                pass

    def deleteAll(self):
        self.presets = []

    def exists(self, presetNos):
        "If single presetNo, return True/False depending on whether it exists. For a list of presetNos, return a list of tuples(presetNo, True/False)."
        if isinstance(presetNos, list) != True:
            # Single presetNo
            # True if found, False if terminates without finding
            return next((True for tup in self.presets if tup[0] == presetNos), False)
        else:
            response = []
            for presetNo in presetNos:
                response.append((presetNo, self.exists(presetNo)))
            return response # [(presetNo, patchList)]
        
