from bot.main import process_text


def test_get_root():
    message = """
120 80 93
    131 86;
     131 86  
     130,70,90    
     131 86 95  
131 86;
    """
    assert process_text(message) == [
        ('120', '80', '93'),
        ('131', '86', ''),
        ('131', '86', ''),
        ('130', '70', '90'),
        ('131', '86', '95'),
        ('131', '86', ''),
    ]
    assert process_text('120 80') == [('120', '80', '')]
    assert process_text('120 80 76') == [('120', '80', '76')]
    assert process_text('20 80') == [('20', '80', '')]
    assert process_text('20 80 76') == [('20', '80', '76')]
    assert process_text(' 120 80 76 ') == [('120', '80', '76')]
    assert process_text(';120 80 76;') == [('120', '80', '76')]
    assert process_text('76;') == []
    assert process_text('76;30') == [('76', '30', '')]
