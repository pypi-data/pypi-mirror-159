from typing import List

from rdflib import Graph

from ..clv.Country import Country
from ..l0.Characteristic import Characteristic
from ..ns import *
from ..Thing import Thing


class Language(Characteristic):
    __type__ = LANG["Language"]

    isLanguageOf: List[Thing] = None
    spokenIn: List[Country] = None

    def _addProperties(self, g: Graph):
        super()._addProperties(g)

        if self.isLanguageOf:
            for isLanguageOf in self.isLanguageOf:
                g.add((self.uriRef, LANG["isLanguageOf"], isLanguageOf.uriRef))

        if self.spokenIn:
            for spokenIn in self.spokenIn:
                g.add((self.uriRef, LANG["spokenIn"], spokenIn.uriRef))