from experimental import *


def test_MenuSection_menu_token_return_values_01():
    '''Menu entry return values equal menu entry menu_tokens when menu entry menu_tokens are strings.
    Always true, including for all four combinations of the two settings tested here.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_tokens = ['apple', 'banana', 'cherry']
    menu_section = menu.make_section(is_numbered=True, menu_tokens=menu_tokens)
    menu_section.title = 'section'
    assert menu_section.is_numbered
    assert menu_section.menu_token_return_values == ['apple', 'banana', 'cherry']
    assert menu_section.menu_token_return_values == menu_section.menu_token_bodies

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_tokens = ['apple', 'banana', 'cherry']
    menu_section = menu.make_section(menu_tokens=menu_tokens)
    menu_section.title = 'section'
    assert not menu_section.is_numbered
    assert menu_section.menu_token_return_values == ['apple', 'banana', 'cherry']
    assert menu_section.menu_token_return_values == menu_section.menu_token_bodies

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_tokens = ['apple', 'banana', 'cherry']
    menu_section = menu.make_section(is_numbered=True, menu_tokens=menu_tokens, return_value_attribute='body')
    menu_section.title = 'section'
    assert menu_section.is_numbered
    assert menu_section.menu_token_return_values == ['apple', 'banana', 'cherry']
    assert menu_section.menu_token_return_values == menu_section.menu_token_bodies

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_tokens = ['apple', 'banana', 'cherry']
    menu_section = menu.make_section(menu_tokens=menu_tokens, return_value_attribute='body')
    menu_section.title = 'section'
    assert not menu_section.is_numbered
    assert menu_section.menu_token_return_values == ['apple', 'banana', 'cherry']
    assert menu_section.menu_token_return_values == menu_section.menu_token_bodies


def test_MenuSection_menu_token_return_values_02():
    '''Menu entry return values vary when menu entry menu_tokens are tuples.
    You can explicitly demand a return value equal either to the menu entry key or body.
    Note that menu_section numbering plays no role in this.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_tokens = [
        ('add', 'add something'),
        ('rm', 'delete something'),
        ('mod', 'modify something'),
        ]
    menu_section = menu.make_section(is_numbered=True, menu_tokens=menu_tokens,
        return_value_attribute='key')
    menu_section.title = 'section'
    assert menu_section.is_numbered
    assert menu_section.menu_token_return_values == ['add', 'rm', 'mod']
    assert menu_section.menu_token_return_values == menu_section.menu_token_keys

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_tokens = [
        ('add', 'add something'),
        ('rm', 'delete something'),
        ('mod', 'modify something'),
        ]
    menu_section = menu.make_section(menu_tokens=menu_tokens, return_value_attribute='key')
    menu_section.title = 'section'
    assert not menu_section.is_numbered
    assert menu_section.menu_token_return_values == ['add', 'rm', 'mod']
    assert menu_section.menu_token_return_values == menu_section.menu_token_keys

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_tokens = [
        ('add', 'add something'),
        ('rm', 'delete something'),
        ('mod', 'modify something'),
        ]
    menu_section = menu.make_section(is_numbered=True, menu_tokens=menu_tokens, return_value_attribute='body')
    menu_section.title = 'section'
    assert menu_section.is_numbered
    assert menu_section.menu_token_return_values == ['add something', 'delete something', 'modify something']
    assert menu_section.menu_token_return_values == menu_section.menu_token_bodies

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_tokens = [
        ('add', 'add something'),
        ('rm', 'delete something'),
        ('mod', 'modify something'),
        ]
    menu_section = menu.make_section(menu_tokens=menu_tokens, return_value_attribute='body')
    menu_section.title = 'section'
    assert not menu_section.is_numbered
    assert menu_section.menu_token_return_values == ['add something', 'delete something', 'modify something']
    assert menu_section.menu_token_return_values == menu_section.menu_token_bodies


def test_MenuSection_menu_token_return_values_03():
    '''Length-4 tuples include prepopulated return values.
    You must still set return_value_attribute to 'prepopulated'.
    '''

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    menu_tokens = [
        ('add', 'add something', None, 'return value A'),
        ('rm', 'delete something', None, 'return value B'),
        ('mod', 'modify something', None, 'return value C'),
        ]
    menu_section = menu.make_section(menu_tokens=menu_tokens, return_value_attribute='prepopulated')
    menu_section.title = 'section'
    assert not menu_section.is_numbered
    assert menu_section.menu_token_return_values == ['return value A', 'return value B', 'return value C']
