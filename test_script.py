from getGeoCoords import getGeoCoords


# testing an ident known ident from the csv file
def test_knownIdent1():
    assert getGeoCoords("2NK4") == ("41.27730178833008", "-73.94039916992188")


# testing anothet known ident from the csv file
def test_knownIdent2():
    assert getGeoCoords("KJFK") == ("40.63980103", "-73.77890015")


# testing if the ident is empty
def test_emptyIdent():
    assert getGeoCoords("") == ("", "")


# testing if the ident does not exist
def test_invalidIdent():
    assert getGeoCoords("YONK") == ("", "")
