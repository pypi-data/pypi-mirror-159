from spaceremover import remove_extra_spaces

def test_spaceremover_with_simple_text():
    text_with_extra_spaces = " Hey  this is    an exemple "
    assert "Hey this is an exemple" == remove_extra_spaces(text_with_extra_spaces)