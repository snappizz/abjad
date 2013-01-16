from abjad.tools import *
from experimental import *


def test_SettingInventory___init___01():
    '''Init from other setting inventory.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures([(4, 8), (3, 8)])

    setting_inventory_1 = score_specification['red'].single_context_settings
    setting_inventory_2 = settingtools.SettingInventory(setting_inventory_1)

    assert isinstance(setting_inventory_1, settingtools.SettingInventory)
    assert isinstance(setting_inventory_2, settingtools.SettingInventory)
    assert not setting_inventory_1 is setting_inventory_2
    assert setting_inventory_1 == setting_inventory_2
