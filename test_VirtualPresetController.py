"""Test VirtualPresetController"""

from VirtualPresetController import VirtualPresetController

# Protected members of VirtualPresetController will be accessed for testing
# pylint: disable=W0212

def test_delete_all_presets():
    """Ensure all presets are deleted"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    p2 = [2, 2, 2]
    vpc._presets = {'p1': p1, 'p2': p2}
    vpc.delete_all_presets()
    assert vpc._presets == {}

def test_delete_preset():
    """Delete a singe preset and verify others remain"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    p2 = [2, 2, 2]
    vpc._presets = {'p1': p1, 'p2': p2}
    vpc.delete_preset('p1')
    assert vpc._presets == {'p2': p2}

def test_get_preset_exist():
    """Test getting a preset that exists"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    p2 = [2, 2, 2]
    p3 = [2, 3, 1]
    vpc._presets = {'p1': p1, 'p2': p2, 'p3': p3}
    assert vpc.get_preset('p2') == p2

def test_get_preset_not_exist():
    """Test getting a preset that exists"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    p2 = [2, 2, 2]
    p3 = [2, 3, 1]
    vpc._presets = {'p1': p1, 'p2': p2, 'p3': p3}
    assert vpc.get_preset('p4') is None

def test_get_all_presets():
    """Test getting all presets"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    p2 = [2, 2, 2]
    p3 = [2, 3, 1]
    vpc._presets = {'p1': p1, 'p2': p2, 'p3': p3}
    response = vpc.get_all_presets()
    assert ('p1', p1) in response
    assert ('p2', p2) in response
    assert ('p3', p3) in response

def test_list_presets():
    """Test listing all presets"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    p2 = [2, 2, 2]
    p3 = [2, 3, 1]
    vpc._presets = {'p1': p1, 'p2': p2, 'p3': p3}
    response = vpc.list_presets()
    assert 'p1' in response
    assert 'p2' in response
    assert 'p3' in response

def test_move_preset():
    """Test renaming a preset"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    p2 = [2, 2, 2]
    p3 = [2, 3, 1]
    vpc._presets = {'p1': p1, 'p2': p2, 'p3': p3}
    vpc.move_preset('p1', 'p3')
    assert 'p1' not in vpc._presets
    assert 'p2' in vpc._presets
    assert 'p3' in vpc._presets
    assert vpc._presets['p3'] == p1

def test_preset_id_in_use_exists():
    """Test checking if a preset id is in use with an id in use"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    vpc._presets = {'p1': p1}
    assert vpc.preset_id_in_use('p1')

def test_preset_id_in_use_not_exists():
    """Test checking if a preset id is in use with an id not in use"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    vpc._presets = {'p1': p1}
    assert not vpc.preset_id_in_use('p2')

def test_random_string():
    """Test that a string of the specified length is generated"""
    str_ = VirtualPresetController.random_string(length=10)
    assert len(str_) == 10
    assert isinstance(str_, str)

def test_save_preset():
    """Test that the preset is saved and the assigned id returned"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    p2 = [2, 2, 2]
    vpc._presets = {'p1': p1}
    p2_id = vpc.save_preset(p2)
    assert 'p1' in vpc._presets
    assert p2_id in vpc._presets
    assert vpc._presets[p2_id] == p2

def test_set_preset():
    """Test that the preset is set, including the correct id"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    p2 = [2, 2, 2]
    vpc._presets = {'p1': p1}
    vpc.set_preset('p2', p2)
    assert 'p1' in vpc._presets
    assert 'p2' in vpc._presets
    assert vpc._presets['p2'] == p2

def test_set_presets():
    """Test that the presets are set, including the correct ids"""
    vpc = VirtualPresetController()
    p1 = [1, 4, 4]
    p2 = [2, 2, 2]
    p3 = [2, 3, 1]
    vpc._presets = {'p1': p1}
    vpc.set_presets([('p2', p2), ('p3', p3)])
    assert 'p1' in vpc._presets
    assert 'p2' in vpc._presets
    assert 'p3' in vpc._presets
    assert vpc._presets['p2'] == p2
    assert vpc._presets['p3'] == p3
