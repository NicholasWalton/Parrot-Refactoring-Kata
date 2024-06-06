from parrot import African, European, Nailed, NorwegianBlue


def test_speed_of_european_parrot():
    assert European().speed() == 12.0


def test_cry_of_european_parrot():
    assert European().cry() == "Sqoork!"


def test_speed_of_african_parrot_with_one_coconut():
    assert African(1).speed() == 3.0


def test_cry_of_african_parrot():
    assert African(1).cry() == "Sqaark!"


def test_speed_of_african_parrot_with_two_coconuts():
    assert African(2).speed() == 0.0


def test_speed_of_african_parrot_with_no_coconuts():
    assert African(0).speed() == 12.0


def test_speed_norwegian_blue_parrot_nailed():
    assert Nailed(1.5).speed() == 0.0


def test_speed_norwegian_blue_parrot_not_nailed():
    assert NorwegianBlue(1.5).speed() == 18.0


def test_speed_norwegian_blue_parrot_not_nailed_high_voltage():
    assert NorwegianBlue(4).speed() == 24.0


def test_cry_norwegian_blue_parrot_high_voltage():
    assert NorwegianBlue(4).cry() == "Bzzzzzz"


def test_cry_norwegian_blue_parrot_no_voltage():
    assert NorwegianBlue(0).cry() == "..."
