# Test virtual preset controller

from VirtualPresetController import VirtualPresetController

def test_save_single():
    # Test saving a single preset when no presets and when other presets exist
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    vpc.save(preset1)
    assert preset1 in vpc.presets
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    vpc.save(preset2)
    assert preset2 in vpc.presets

def test_save_single_overwrite():
    # Test saving a single preset to a presetNo that is already in use
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    vpc.save(preset1)
    assert preset1 in vpc.presets
    preset2 = ((1, [2, 2, 4, 2, 1, 1, 4, 7]))
    vpc.save(preset2)
    # Should have overwritten the existing preset
    assert preset2 in vpc.presets
    assert preset1 not in vpc.presets

def test_save_single_patchList_None():
    # Test saving a patchList that is None
    # Should fail silently
    vpc = VirtualPresetController()
    preset1 = ((1, None))
    vpc.save(preset1)
    assert vpc.presets == []

def test_save_single_patchNo_not_int():
    # Test saving non-int preset numbers
    # Should fail silently
    vpc = VirtualPresetController()
    pl = [1, 1, 2, 2, 3, 3, 4, 5]
    vpc.save((1.0, pl))
    vpc.save((None, pl))
    vpc.save(("Eric", pl))
    assert vpc.presets == []

def test_save_multi():
    # Test saving multiple patches in one function
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset3 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.save([preset1, preset2, preset3])
    assert preset1 in vpc.presets
    assert preset2 in vpc.presets
    assert preset3 in vpc.presets
    
def test_move_single_no_conflict():
    # Test moving a preset to an unused number
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    vpc.move((1, 3))
    assert preset1 not in vpc.presets
    assert (3, preset1[1]) in vpc.presets
    assert preset2 in vpc.presets
    assert preset4 in vpc.presets

def test_move_single_yes_conflict():
    # Test moving a preset to a conflicting number
    # Should overwrite
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    vpc.move((1, 4))
    assert preset1 not in vpc.presets
    assert preset4 not in vpc.presets
    assert (4, preset1[1]) in vpc.presets
    assert preset2 in vpc.presets
    
def test_get_single():
    # Test retrieving a single preset
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    assert preset1 is vpc.get(1)
    assert preset2 is vpc.get(2)
    assert preset4 is vpc.get(4)
    assert preset1 in vpc.presets # make sure it's still there

def test_get_not_there():
    # Test retrieving a single preset that doesn't exist
    vpc = VirtualPresetController()
    assert vpc.get(1) == (1, None)
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    assert vpc.get(3) == (3, None)

def test_get_multi_all_there():
    # Test retrieving multiple presets
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    result = vpc.get([1, 4])
    assert preset1 in result
    assert preset2 not in result
    assert preset4 in result
    assert preset1 in vpc.presets # make sure it's still there

def test_get_multi_inc_not_there():
    # Test retrieving multiple presets including one that doesn't exist
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    result = vpc.get([1, 3, 4])
    assert preset1 in result
    assert preset2 not in result
    assert (3, None) in result
    assert preset4 in result
    assert preset1 in vpc.presets # make sure it's still there

def test_getAll():
    # Test retrieving all presets
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    result = vpc.getAll()
    assert preset1 in result
    assert preset2 in result
    assert preset4 in result
    assert preset1 in vpc.presets # make sure it's still there

def test_delete_single_exists():
    # Test deleting a single preset that exists
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    vpc.delete(2)
    assert preset1 in vpc.presets
    assert preset2 not in vpc.presets
    assert preset4 in vpc.presets

def test_delete_single_not_exists():
    # Test deleting a single preset that doesn't exist
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    vpc.delete(3)
    assert preset1 in vpc.presets
    assert preset2 in vpc.presets
    assert preset4 in vpc.presets

def test_delete_multiple_exists():
    # Test deleting multiple presets that exist
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    vpc.delete([1, 4])
    assert preset1 not in vpc.presets
    assert preset2 in vpc.presets
    assert preset4 not in vpc.presets

def test_delete_multiple_inc_not_exists():
    # Test deleting multiple presets including one that doesn't exist
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    vpc.delete([1, 3, 4])
    assert preset1 not in vpc.presets
    assert preset2 in vpc.presets
    assert preset4 not in vpc.presets

def test_deleteAll():
    # Test deleting all presets
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    vpc.deleteAll()
    assert vpc.presets == []

def test_exists_single_does_exist():
    # Test if a single preset that does exist exists
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    assert vpc.exists(2) is True
    assert preset2 in vpc.presets

def test_exists_single_does_not_exist():
    # Test if a single preset that doesn't exist exists
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    assert vpc.exists(3) is False

def test_exists_multiple():
    # Test if multiple presets exist, including one that doesn't
    vpc = VirtualPresetController()
    preset1 = ((1, [1, 1, 2, 2, 3, 3, 4, 5]))
    preset2 = ((2, [2, 2, 4, 2, 1, 1, 4, 7]))
    preset4 = ((4, [1, 1, 4, 5, 6, 7, 1 ,1]))
    vpc.presets = [preset1, preset2, preset4]
    result = vpc.exists([5, 4, 3, 2, 1])
    truths = list(map(lambda x: x[1], result))
    assert truths == [False, True, False, True, True]
