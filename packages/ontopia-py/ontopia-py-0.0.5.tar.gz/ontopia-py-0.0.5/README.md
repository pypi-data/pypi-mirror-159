# ontopia-py

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/luca-martinelli-09/ontopia-py/graphs/commit-activity)
[![PyPI version](https://img.shields.io/pypi/v/ontopia-py.svg)](https://pypi.python.org/pypi/ontopia-py/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ontopia-py.svg)](https://pypi.python.org/pypi/ontopia-py/)
[![PyPI status](https://img.shields.io/pypi/status/ontopia-py.svg)](https://pypi.python.org/pypi/ontopia-py/)

This python package helps in create and implements an [OntoPiA](https://github.com/italia/daf-ontologie-vocabolari-controllati) RDF.

# How it works

For example, to create a street toponym in the ANNCSU dataset:

```python
from rdflib import XSD, Graph, Literal, Namespace

from ontopia_py import ConceptScheme, createGraph
from ontopia_py.clv import StreetToponym

# Set namespace for data
ANNCSU: Namespace = Namespace("https://w3id.org/sona/data/ANNCSU/")

# Create the graph and bind the namespace
g = createGraph()
g.bind("anncsu", ANNCSU)

# Create the concept scheme
ANNCSU_DATA: ConceptScheme = ConceptScheme(ANNCSU)
ANNCSU_DATA.label = [
    Literal("Anagrafe nazionale numeri civici e strade urbane", lang="it"),
    Literal("Civic Addressing and Street Naming", lang="en")
]

# Add to graph
ANNCSU_DATA.addToGraph(g)

# Create the street toponym
streetToponym: StreetToponym = StreetToponym(
  id="street-1",
  baseUri=ANNCSU,
  dataset=ANNCSU_DATA,
  titles=[Literal("Via Roma", datatype=XSD.string)]
)
streetToponym.toponymQualifier = "Via"
streetToponym.officialStreetName = "Roma"

# Add to graph
streetToponym.addToGraph(g)
```

# Ontologies implemented

- [ ] https://w3id.org/italia/onto/ACCO
- [x] https://w3id.org/italia/onto/AccessCondition
- [ ] https://w3id.org/italia/onto/AtlasOfPaths
- [x] https://w3id.org/italia/onto/CLV
- [x] https://w3id.org/italia/onto/COV
- [ ] https://w3id.org/italia/onto/CPEV
- [ ] https://w3id.org/italia/onto/CPSV
- [x] https://w3id.org/italia/onto/CPV
- [ ] https://w3id.org/italia/onto/CulturalHeritage
- [ ] https://w3id.org/italia/onto/HER
- [ ] https://w3id.org/italia/onto/Indicator
- [ ] https://w3id.org/italia/onto/IoT
- [x] https://w3id.org/italia/onto/Language
- [x] https://w3id.org/italia/onto/MU
- [ ] https://w3id.org/italia/onto/PARK
- [ ] https://w3id.org/italia/onto/POI
- [ ] https://w3id.org/italia/onto/POT
- [ ] https://w3id.org/italia/onto/Project
- [ ] https://w3id.org/italia/onto/PublicContract
- [x] https://w3id.org/italia/onto/RO
- [ ] https://w3id.org/italia/onto/Route
- [x] https://w3id.org/italia/onto/SM
- [x] https://w3id.org/italia/onto/TI
- [ ] https://w3id.org/italia/onto/Transparency
- [x] https://w3id.org/italia/onto/l0
