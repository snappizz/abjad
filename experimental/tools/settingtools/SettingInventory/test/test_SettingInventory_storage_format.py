from abjad.tools import *
from experimental import *
from experimental.tools.settingtools import SettingInventory


def test_SettingInventory_storage_format_01():
    '''Storage format exists and is evaluable.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures([(4, 8), (3, 8)])
    score_specification.interpret()

    setting_inventory_1 = score_specification['red'].single_context_settings
    storage_format = setting_inventory_1.storage_format
    setting_inventory_2 = eval(storage_format)

    assert isinstance(setting_inventory_1, SettingInventory)
    assert isinstance(setting_inventory_2, SettingInventory)
    assert not setting_inventory_1 is setting_inventory_2
    assert setting_inventory_1 == setting_inventory_2
