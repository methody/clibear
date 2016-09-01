import testtools
from clibear import base


class TestBase(testtools.TestCase):
    def test_base(self):
        base.main()
