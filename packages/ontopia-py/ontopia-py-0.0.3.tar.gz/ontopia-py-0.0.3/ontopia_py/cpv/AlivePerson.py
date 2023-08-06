from rdflib import Graph, Literal

from ..ns import *
from .EducationLevel import EducationLevel
from .Person import Person


class AlivePerson(Person):
    __type__ = CPV["AlivePerson"]

    hasLevelOfEducation: EducationLevel = None
    age: Literal = None

    def _addProperties(self, g: Graph):
        if self.hasLevelOfEducation:
            g.add(self.uriRef, CPV["hasLevelOfEducation"],
                  self.hasLevelOfEducation.uriRef)

        if self.age:
            g.add(self.uriRef, CPV["age"], self.age)
