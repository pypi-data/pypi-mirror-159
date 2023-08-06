from typing import List

from rdflib import Graph, Literal

from ..ns import *
from .Family import Family


class RegisteredFamily(Family):
    __type__ = CPV["RegisteredFamily"]

    registeredFamilyID: Literal = None
    numberRegFamilyComponents: Literal = None

    def _addProperties(self, g: Graph):
        if self.registeredFamilyID:
            g.add(
                (self.uriRef, CLV["registeredFamilyID"], self.registeredFamilyID))

        if self.numberRegFamilyComponents:
            g.add(
                (self.uriRef, CLV["numberRegFamilyComponents"], self.numberRegFamilyComponents))
