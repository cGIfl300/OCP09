def stars(number_of_stars, max_stars):
    """
    For a given number of stars, will return number of stars.
    :param int number_of_stars: number of stars
    :param int max_stars: max number of stars
    :return: a string
    """

    star_true = "★"
    star_false = "☆"
    return star_true * number_of_stars + star_false * (
        max_stars - number_of_stars
    )


def test_stars():
    assert stars(0, 6) == "☆☆☆☆☆☆"
    assert stars(1, 6) == "★☆☆☆☆☆"
    assert stars(3, 6) == "★★★☆☆☆"
    assert stars(5, 6) == "★★★★★☆"
    assert stars(6, 6) == "★★★★★★"
