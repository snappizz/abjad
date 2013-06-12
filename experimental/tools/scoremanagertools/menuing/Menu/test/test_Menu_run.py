from experimental import *


def test_Menu_run_01():
    '''String menu_token defaults.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(is_modern=True)
    menu_section.append('apple')
    menu_section.append('banana')
    menu_section.append('cherry')
    menu_section.title = 'section'

    result = menu._run(user_input='foo')
    assert menu._session.transcript[-2][1] == \
    ['Location',
      '',
      '     Section',
      '',
      '     apple',
      '     banana',
      '     cherry',
      '']
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='app')
    assert result == 'apple'

    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='app, che-ban')
    assert result is None


def test_Menu_run_02():
    '''Hidden menu section.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(
        is_hidden=True, 
        is_modern=True,
        )
    menu_section.append('apple')
    menu_section.append('banana')
    menu_section.append('cherry')
    menu_section.title = 'section'
    result = menu._run(user_input='foo')

    assert menu._session.transcript[-2][1] == \
    ['Location', '']
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='app')
    assert result == 'apple'

    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='app, che-ban')
    assert result is None


def test_Menu_run_03():
    '''Numbered menu section.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(
        is_numbered=True,
        is_modern=True,
        )
    menu_section.append('apple')
    menu_section.append('banana')
    menu_section.append('cherry')
    menu_section.title = 'section'
    result = menu._run(user_input='foo')

    assert menu._session.transcript[-2][1] == \
    ['Location',
      '',
      '     Section',
      '',
      '     1: apple',
      '     2: banana',
      '     3: cherry',
      '']
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result == 'apple'

    menu._session.reinitialize()
    result = menu._run(user_input='app')
    assert result == 'apple'

    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='app, che-ban')
    assert result is None


def test_Menu_run_04():
    '''Menu section with range selection turned on.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(
        is_ranged=True, 
        is_modern=True,
        )
    menu_section.append('apple')
    menu_section.append('banana')
    menu_section.append('cherry')
    menu_section.title = 'section'
    result = menu._run(user_input='foo')

    assert menu._session.transcript[-2][1] == \
    ['Location',
      '',
      '     Section',
      '',
      '     apple',
      '     banana',
      '     cherry',
      '']
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='app')
    assert result == ['apple']

    menu._session.reinitialize()
    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='app, che-ban')
    assert result == ['apple', 'cherry', 'banana']


def test_Menu_run_05():
    '''Keyed menu section with key returned.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(
        return_value_attribute='key',
        is_keyed=True, 
        is_modern=True,
        )
    menu_section.append(('first command', 'add'))
    menu_section.append(('second command', 'rm'))
    menu_section.append(('third command', 'mod'))
    menu_section.title = 'section'

    result = menu._run(user_input='foo')

    assert menu._session.transcript[-2][1] == \
    ['Location',
      '',
      '     Section',
      '',
      '     first command (add)',
      '     second command (rm)',
      '     third command (mod)',
      '']
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add')
    assert result == 'add'

    menu._session.reinitialize()
    result = menu._run(user_input='fir')
    assert result == 'add'

    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add, mod-rm')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='fir, thi-sec')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='fir, mod-sec')
    assert result is None


def test_Menu_run_06():
    '''Keyed menu section with display string returned.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(
        return_value_attribute='display_string',
        is_keyed=True, 
        is_modern=True,
        )
    menu_section.append(('first command', 'add'))
    menu_section.append(('second command', 'rm'))
    menu_section.append(('third command', 'mod'))
    result = menu._run(user_input='foo')

    menu._session.reinitialize()
    result = menu._run(user_input='foo')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add')
    assert result == 'first command'

    menu._session.reinitialize()
    result = menu._run(user_input='fir')
    assert result == 'first command'

    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add, mod-rm')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='fir, thi-sec')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='fir, mod-sec')
    assert result is None


def test_Menu_run_07():
    '''Hidden keyed menu section with key returned.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(
        return_value_attribute='key',
        is_keyed=True, 
        is_hidden=True, 
        is_modern=True,
        )
    menu_section.append(('first command', 'add'))
    menu_section.append(('second command', 'rm'))
    menu_section.append(('third command', 'mod'))
    menu_section.title = 'section'
    result = menu._run(user_input='foo')

    assert menu._session.transcript[-2][1] == \
    ['Location', '']

    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add')
    assert result == 'add'

    menu._session.reinitialize()
    result = menu._run(user_input='fir')
    assert result == 'add'

    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add, mod-rm')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='fir, thi-sec')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='fir, mod-sec')
    assert result is None


def test_Menu_run_08():
    '''Hidden keyed menu section with display string returned.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(
        is_keyed=True, 
        is_hidden=True, 
        is_modern=True,
        )
    menu_section.append(('first command', 'add'))
    menu_section.append(('second command', 'rm'))
    menu_section.append(('third command', 'mod'))
    menu_section.title = 'section'

    menu._session.reinitialize()
    result = menu._run(user_input='foo')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add')
    assert result == 'first command'

    menu._session.reinitialize()
    result = menu._run(user_input='fir')
    assert result == 'first command'

    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add, mod-rm')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='fir, thi-sec')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='fir, mod-sec')
    assert result is None


def test_Menu_run_09():
    '''Numbered keyed menu section with key returned.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(
        return_value_attribute='key',
        is_numbered=True, 
        is_keyed=True, 
        is_modern=True,
        )
    menu_section.append(('first command', 'add'))
    menu_section.append(('second command', 'rm'))
    menu_section.append(('third command', 'mod'))
    menu_section.title = 'section'
    result = menu._run(user_input='foo')

    assert menu._session.transcript[-2][1] == \
    ['Location',
      '',
      '     Section',
      '',
      '     1: first command (add)',
      '     2: second command (rm)',
      '     3: third command (mod)',
      '']
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result == 'add'

    menu._session.reinitialize()
    result = menu._run(user_input='add')
    assert result == 'add'

    menu._session.reinitialize()
    result = menu._run(user_input='fir')
    assert result == 'add'

    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add, mod-rm')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='fir, thi-sec')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='fir, mod-sec')
    assert result is None


def test_Menu_run_10():
    '''Ranged keyed menu section with with key returned.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(
        return_value_attribute='key',
        is_keyed=True, 
        is_ranged=True,
        is_modern=True,
        )
    menu_section.append(('first command', 'add'))
    menu_section.append(('second command', 'rm'))
    menu_section.append(('third command', 'mod'))
    menu_section.title = 'section'
    result = menu._run(user_input='foo')

    assert menu._session.transcript[-2][1] == \
    ['Location',
      '',
      '     Section',
      '',
      '     first command (add)',
      '     second command (rm)',
      '     third command (mod)',
      '']
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add')
    assert result == ['add']

    menu._session.reinitialize()
    result = menu._run(user_input='fir')
    assert result == ['add']

    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add, mod-rm')
    assert result == ['add', 'mod', 'rm']

    menu._session.reinitialize()
    result = menu._run(user_input='fir, thi-sec')
    assert result == ['add', 'mod', 'rm']

    menu._session.reinitialize()
    result = menu._run(user_input='fir, mod-sec')
    assert result == ['add', 'mod', 'rm']


def test_Menu_run_11():
    '''RK menu section with display string returned.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_section = menu.make_section(
        is_keyed=True, 
        is_ranged=True,
        is_modern=True,
        )
    menu_section.append(('first command', 'add'))
    menu_section.append(('second command', 'rm'))
    menu_section.append(('third command', 'mod'))
    menu_section.title = 'section'

    menu._session.reinitialize()
    result = menu._run(user_input='foo')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='q')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='1')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add')
    assert result == ['first command']

    menu._session.reinitialize()
    result = menu._run(user_input='fir')
    assert result == ['first command']

    menu._session.reinitialize()
    result = menu._run(user_input='1, 3-2')
    assert result is None

    menu._session.reinitialize()
    result = menu._run(user_input='add, mod-rm')
    assert result == ['first command', 'third command', 'second command']

    menu._session.reinitialize()
    result = menu._run(user_input='fir, thi-sec')
    assert result == ['first command', 'third command', 'second command']

    menu._session.reinitialize()
    result = menu._run(user_input='fir, mod-sec')
    assert result == ['first command', 'third command', 'second command']
