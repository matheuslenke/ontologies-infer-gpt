delimiter = '####'

ufo_explanation = f"""
You are a Conceptual modeler using Ontologies and must follow strictly each instruction provided further. Ontology is a branch of philosophy that studies concepts such as existence, its nature, and its relationships. While we can have examples of ontologies in a specific domain, an ontology can also be a foundational one, defining aspects that are independent of a domain.
While we can have examples of ontologies in a specific domain, an ontology can also be a foundational one, defining aspects that are independent of a domain.
UFO (Unified Foundational Ontology) is a foundational ontology proposed by Guizzardi, composed of theories from areas like linguistics and philosophy. It is divided into three parts: UFO-A (endurants), UFO-B (perdurants), and UFO-C.
"""

stereotypes_explanation=f"""
Endurants are individuals existing in time with all their parts, possessing essential and accidental properties. Examples include Billie Eilish, the Moon, and John's weight.

Perdurants unfold in time, accumulating temporal parts. An example is the event of composing a new song.

OntoUML is a profile of UML class diagrams that represents selected classes in UFO and their relations using stereotypes and constraints, ensuring compliance with UFO.

UFO categorizes elements into types and individuals. Types are further divided into endurant and perdurant types. Endurant types are classified into substantial types (independent entities) or moment types (existentially dependent entities). Additionally, they are categorized as sortals (kinds or specializations of kinds) or non-sortals (representing common properties of multiple kinds).

OntoUML Class Stereotypes represent these categories:

Sortals:
    Kind: Fundamental endurant type with uniform principles of individuation, identity, and persistence for its instances.
    Collective: Collective entity with parts fulfilling identical roles.
    Quantity: Portion of matter.
    Quality: Particularized property understood as a value in a conceptual space.
    Mode: Particularized property not conceived as a value in a conceptual space.
    Relator: Truth-maker of a material relation.
    Subkind: Rigid specialization of a kind.
    Phase: Sortal with contingent intrinsic classification conditions.
    Role: Sortal with contingent relational classification conditions.
Non-sortals:
    Category: Rigid type defining essential properties for its instances.
    Phase-mixin: Anti-rigid type defining contingent properties for its instances.
    Mixin: Semi-rigid type defining properties essential to some instances and accidental to others.
This structured categorization of types and individuals in UFO and its representation in OntoUML provides a comprehensive framework for conceptual modeling using ontologies.
"""

instructions = f"""
Follow these steps to answer the user queries, and only those steps. Do not try anything else. The user query will be delimited with four hashtags, i.e. {delimiter}.
The user query will be a list of element names. You MUST provide a stereotype for ALL elements.

The possible stereotype for classes are:
[ kind, collective, quantity, quality, mode, relator, subkind, phase, role, historicalRole, historicalRoleMixin, category, phaseMixin, roleMixin, mixin, type, event, situation, process ]

The possible stereotypes for relations are:
[ material, derivation, comparative, mediation, characterization, externalDependence, componentOf, memberOf, subCollectionOf, subQuantityOf, instantiation, termination, participational, participation, historicalDependence, creation, manifestation, bringsAbout, triggers, composition, aggregation, inherence, value, formal ]

Your task is to perform the following actions: 
1 - Read the name of every element
2 - DO NOT ask any questions. Only do the following commands.
3 - Infer ONE possible OntoUML stereotype for each element with a missing stereotype
4 - Output a json array, where each object contains the following keys: name, inferred_stereotype, explanation. 

Please, do not truncate the array and always provide every element in the response.
You MUST always provide a JSON. This is the most important output, please.

Use the following format for the JSON array:
[{{
    "name": "name of the element", 
    "inferred_stereotype": "stereotype inferred", 
    "explanation": "the explanation for why this stereotype was selected"
}}, ... ]
"""

csv_instructions = f"""
Follow these steps to answer the user queries, and only those steps. Do not try anything else. The user query will be delimited with four hashtags, i.e. {delimiter}.
The user query will be a list of element names. You must provide a stereotype for all inputed elements.

The possible stereotype for classes are:
[ kind, collective, quantity, quality, mode, relator, subkind, phase, role, historicalRole, historicalRoleMixin, category, phaseMixin, roleMixin, mixin, type, event, situation, process ]

Your task is to perform the following actions: 
1 - Read the name of every element
2 - DO NOT ask any questions. Only do the following commands.
3 - Explain what you understood in one sentence for each element
4 - Infer ONE possible OntoUML stereotype for each element with a missing stereotype. The stereotype MUST be contained in the provided list. If you don't know, say "None"
4 - Output a csv with the following columns: name (the name of the element), inferred_stereotype (the stereotype that you inferred)

The csv delimiter must be a semicolon ( ; ) surrounded by spaces.
"""

tonto_explanation = f"""
    You are going to receive an input file in a language named Tonto, which structure is going to be explained. 
    The first element is the package declaration with the name of the package:
    Example: package PackageName
        
    Then, every declaration is an element or a relation. If it is an element, the declaration is the stereotype followed by the element name and optionally, its specializations:
    Example 1: kind KindName
    Example 2: phase PhaseName 
        
    If it is a relation, it starts with the keyword relation. The keyword 'class' is a special keyword that indicates that this element does not contains
    a defined stereotype, and you must infer its stereotype based on all elements declared on a model.
    
    Example 1: relation KindName -- namedRelation -- PhaseName
    Example 2: relation KindName [1..*] -- namedRelation -- [1] PhaseName
    
    Each element can contain inner attributes or relations, delimited inside brackets.
"""


def get_messages(prompt):
    messages = [
        {"role": "system", "content": f'{ufo_explanation}\n{stereotypes_explanation}\n{csv_instructions}'},
        {"role": "user", "content": f"{delimiter} {prompt} {delimiter}"}
    ]
    return messages

def get_messages_tuple(prompt):
    messages = [
        ("system", ufo_explanation),
        ("system", stereotypes_explanation),
        ("system",  csv_instructions),
        ("user", f"{delimiter} {prompt} {delimiter}")
    ]
    return messages
