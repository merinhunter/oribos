from oribos import oribos
from oribos._version import __version__


def test_version():
    assert __version__ == '0.2.1'

def test_leader():
    assert oribos.leader() == "The Arbiter"

def test_races():
    assert oribos.races() == ["Attendant", "Broker"]
