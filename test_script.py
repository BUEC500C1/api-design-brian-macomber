from getGeoCoords import getGeoCoords

# write a 2 working tests nd one empty set test for each function in app.py


def test_knownIdent1():
    assert getGeoCoords("2NK4") == ("41.27730178833008", "-73.94039916992188")


def test_knownIdent2():
    assert getGeoCoords("KJFK") == ("40.63980103", "-73.77890015")


def test_emptyIdent():
    assert getGeoCoords("") == ("", "")


def test_invalidIdent():
    assert getGeoCoords("YONK") == ("", "")
