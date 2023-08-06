from typing import List

from ..clv.Address import Address
from ..ns import *
from .AlivePerson import AlivePerson
from .Family import Family


class Resident(AlivePerson):
    __type__ = CPV["Resident"]

    belongsToFamily: List[Family] = None
    hasCurrentResidence: Address = None

    def _addProperties(self, g: Graph):
        if self.belongsToFamily:
            for belongsToFamily in self.belongsToFamily:
                g.add((self.uriRef, CLV["belongsToFamily"], belongsToFamily))

        if self.hasCurrentResidence:
            g.add(self.uriRef, CPV["hasCurrentResidence"],
                  self.hasCurrentResidence.uriRef)
