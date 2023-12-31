# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module libranet_quantum.__init__."""
import packaging.version


def test_version() -> None:
    from libranet_quantum import __version__

    assert isinstance(__version__, str)
    assert packaging.version.parse(__version__) >= packaging.version.parse("0.0")


# def test_copyright() -> None:
#     from libranet_quantum import __copyright__

#     assert isinstance(__copyright__, str)
#     assert "Copyright" in __copyright__


def test_license() -> None:
    import libranet_quantum
    # from libranet_quantum import __license__

    assert isinstance(libranet_quantum.__license__, str)
    assert "MIT" in libranet_quantum.__license__
