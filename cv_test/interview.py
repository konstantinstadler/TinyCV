""" First interview test
"""


# import tinytroupe
from tinytroupe.agent import TinyPerson
from tinytroupe.extraction import ResultsExtractor
# import tinytroupe.control as control

import pprint

verones = TinyPerson.load_specification("./verones.agent.json")
goldenberg = TinyPerson.load_specification("./goldenberg.agent.json")
goyal = TinyPerson.load_specification("./goyal.agent.json")
gustinara = TinyPerson.load_specification("./gustinara.agent.json")


world = TinyWorld("Group Interview", [verones, goldenberg, goyal, gustinara])
world.make_everyone_accessible()

world.broadcast("""
Verones has a group interview with Goldenberg, Goyal and Gustinara.

Verones interviews everyone in turn, and the answers are accessable to every participant.
The interviews persona can respond to previous answers, and compete for the position in a respectful discussion.
At the end of the 

The position is for a one-year Researcher position in the field of global supply chain
sustainability and biodiversity conservation. The research investigates the biodiversity impacts of food and
non-food commodities along global supply chains. 

As we enter the final phase of these projects, we seek an experienced researcher to help us
analyse the results regarding biodiversity footprints and to synthesize our findings and communicate them effectively to both academic and
public audiences. Your immediate leader is Prof. Dr. Francesca Verones.

Duties of the position
- Investigate biodiversity footprints from food and non-food commodities across a range of impact categories
- Test and contribute to the further development of novel impact categories within life cycle impact assessment regarding biodiversity
impacts
- Lead the writing of scientific articles based on the project's findings
- Manage the publication process, including submission and revision stages
- Produce summaries and articles suitable for public science outlets to disseminate our research to a broader audience
- Develop policy briefs to inform decision-makers and stakeholders about our findings and their implications
- Contribute to writing chapters for a report on the update of the LC-IMPACT methodology

Required selection criteria
- A doctoral degree in a relevant subject area
- Experience with data analytics and visualization
- Proven track record of writing and publishing scientific papers
- Experience or strong interest in sustainability and environmental issues
- Excellent communication skills in English
- Ability to translate complex scientific findings into accessible language for non- specialist audiences


"""
)

verones.listen("Find good questions to find the best candidate for the announced position")
world.run(10)

extractor = ResultsExtractor()


report = extractor.extract_results_from_world(world,
                        extraction_objective="""
                        Recommend the best person for the announced position.
                        Recommend next steps to verify the outcome and to obtain missing information not provided by the interview.
                        """,
                        verbose=True)

pprint.pprint(report)
