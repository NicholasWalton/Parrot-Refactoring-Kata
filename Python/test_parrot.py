from parrot import African, European, NorwegianBlue


def test_speed_of_european_parrot():
    parrot = European()
    assert parrot.speed() == 12.0


def test_cry_of_european_parrot():
    parrot = European()
    assert parrot.cry() == "Sqoork!"


def test_speed_of_african_parrot_with_one_coconut():
    parrot = African(1)
    assert parrot.speed() == 3.0


def test_cry_of_african_parrot():
    parrot = African(1)
    assert parrot.cry() == "Sqaark!"


def test_speed_of_african_parrot_with_two_coconuts():
    parrot = African(2)
    assert parrot.speed() == 0.0


def test_speed_of_african_parrot_with_no_coconuts():
    parrot = African(0)
    assert parrot.speed() == 12.0


def test_speed_norwegian_blue_parrot_nailed():
    parrot = NorwegianBlue(1.5, True)
    assert parrot.speed() == 0.0


def test_speed_norwegian_blue_parrot_not_nailed():
    parrot = NorwegianBlue(1.5, False)
    assert parrot.speed() == 18.0


def test_speed_norwegian_blue_parrot_not_nailed_high_voltage():
    parrot = NorwegianBlue(4, False)
    assert parrot.speed() == 24.0


def test_cry_norwegian_blue_parrot_high_voltage():
    parrot = NorwegianBlue(4, False)
    assert parrot.cry() == "Bzzzzzz"


def test_cry_norwegian_blue_parrot_no_voltage():
    parrot = NorwegianBlue(0, False)
    assert parrot.cry() == "..."
