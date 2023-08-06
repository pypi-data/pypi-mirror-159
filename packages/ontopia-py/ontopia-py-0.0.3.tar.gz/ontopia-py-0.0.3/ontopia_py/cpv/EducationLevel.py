from typing import List

from rdflib import Graph, Literal

from ..ns import *
from ..l0.Characteristic import Characteristic


class EducationLevel(Characteristic):
    __type__ = CPV["EducationLevel"]

    educationLevelDesc: List[Literal] = None
    educationLevelID: Literal = None

    def _addProperties(self, g: Graph):
        if self.educationLevelDesc:
            for educationLevelDesc in self.educationLevelDesc:
                g.add(
                    (self.uriRef, CLV["educationLevelDesc"], educationLevelDesc))

        if self.educationLevelID:
            g.add(self.uriRef, CPV["educationLevelID"], self.educationLevelID)
