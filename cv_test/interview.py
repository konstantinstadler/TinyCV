""" First interview test
"""

import json
import sys

import tinytroupe
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.extraction import ResultsReducer
from tinytroupe.validation import TinyPersonValidator
import tinytroupe.control as control

fv = TinyPerson.load_specification("./verones.agent.json")
iv = TinyPerson.load_specification("./aldy.agent.json")

world = TinyWorld("Chat Room", [fv, iv])
world.make_everyone_accessible()

fv.listen("Interview Aldy for a postion on biodiversity footprint research")
world.run(4)
