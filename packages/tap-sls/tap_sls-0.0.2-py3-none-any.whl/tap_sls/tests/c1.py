from tap_sls.tests.p1 import P1


class C1(P1):

    def __init__(self):
        P1.__init__(self)

    @property
    def t(self):
        print(self.client)


    def a(self):
        print(self.client)