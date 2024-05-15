delimiter = '####'

ufo_explanation = f"""
You are a Conceptual modeler using Ontologies and must follow strictly each instruction provided further. Ontology is a branch of philosophy that studies concepts such as existence, its nature, and its relationships. While we can have examples of ontologies in a specific domain, an ontology can also be a foundational one, defining aspects that are independent of a domain.
While we can have examples of ontologies in a specific domain, an ontology can also be a foundational one, defining aspects that are independent of a domain. Guizzardi proposes in his work a foundational ontology called UFO (Unified Foundational Ontology) through the composition of several theories from areas such as linguistics and formalizations of ontologies of philosophy. This ontology is divided into three parts: UFO-A, UFO-B, and UFO-C.

For the scope of this work, we will talk mostly about UFO-A, which is an ontology of endurants, and UFO-B, which is an ontology of perdurants. “Endurants are individuals that exist in time with all their parts. They have essential and accidental properties and, hence, they can qualitatively change while maintaining their numerical identify (i.e., while remaining the same individual)”. Billie Eilish, the Moon, and John’s weight are all examples of endurants

Perdurants are individuals that unfold in time accumulating temporal parts. An endurant can change while maintaining its identity, a perdurant cannot” (GUIZZARDI et al., 2022). An example of perdurant is the event of composing a new song, made by an artist.

In OntoUML, selected classes in UFO and the relations between them are represented by stereotypes of classes or associations in UML, with syntactic formal constraints that are semantically motivated. "This combination of stereotypes and constraints enforces conformance, making every valid OntoUML model compliant to UFO"

UFO divides all elements into some ontological categories, the first division being between types and individuals. A type for example would be the kind Computer Operating System, while an individual would be the available operating systems that we have, like Linux, Windows and MacOS. The relation between an individual and a type is called instantiation, meaning that while types determine the characteristics that something needs to have in order to be considered of that type, an individual is the thing that exhibits these characteristics. OntoUML, being a profile of UML class diagrams, only supports the definition of types, meaning that it does not address the specification of individuals.

Types are further categorized into endurant and perdurant types. Endurant types are classified into two orthogonal hierarchies: they are partitioned into substantial types or moment types in one of these hierarchies, and partitioned into sortals and non-sortals in the other. Substantials are independent entities that exist without the need of another, while moments are endurants that existentially depend on other entities. "A sortal is either a kind or a specialization of a kind, and those who are not a kind need to specialize exactly one kind". A non-sortal is a type that represents common properties of individuals of multiple kinds.
"""

stereotypes_explanation=f"""
Here is the explanation for every Class Stereotype:

Sortals:
    - Kind: A fundamental sort of endurant type, a type which provides uniform principles of individuation, identity, and persistence to its instances. For example, the types person, dog, computer, car, organization and marriage are typically considered to be kinds. Kinds apply to instantiating individuals in all possible situations in which these individuals exist. In OntoUML, the stereotype kind is a shortcut for Object Kind, i.e., an Object Type that is also a Kind. Because of this, instances of classes stereotyped kind are instances of Object (also termed 'functional complex' in UFO). Since the notion of ultimate sortals (kinds) is also applicable to Collective Types, Quantity Types, Quality Types, Mode Types and Relator Types, specific stereotypes are introduced: a class stereotyped kind is an Object Kind, a class stereotyped collective is a Collective Kind, a class stereotyped relator is a Relator Kind, a class stereotyped mode is a Mode Kind, a class stereotyped quality is a Quality Kind, and a class stereotyped quantity is a Quantity Kind

    - Collective: An instance of a class stereotyped collective is a collective entity whose parts (members of the collective) fulfill identical roles in relation to the whole, for example, a deck of cards or a forest as a collective of trees

    - Quantity: An instance of a class stereotyped quantity is a portion of home- omerous amount of matter. For example, a portion of water, soda or sand.

    - Quality: An instance of a class stereotyped quality is a particularized property that can be understood as a value in a conceptual space, for example, the weight or height of a person which can be measured in centimeters, or the color of an eye that can be represented in an RGB tuple.

    - Mode: An instance of a class stereotyped mode is a particularized property that is not conceived as a value in a conceptual space. For example, the ability of speaking a language that a person can have, or a disease that is affecting a dog.

    - Relator: An instance of a class stereotyped relator is a truth-makers of a material relation, an entity that needs to exist for two or more related individuals to be connected through a material relation. For example, a handshake depends on two individuals of the kind element Person. Examples or relators include social objects such as Marriage, or a purchase order from an online store.

The additional sortal stereotypes subkind, phase and role represent their counterparts in UFO. They must specialize a unique kind from which they inherit a principle of identity for their instances. Whether their instances are objects, collectives, quantities, qualities, modes or relators is already settled by specialized class (which will be stereotyped kind, collective, quantity, quality, mode or relator). These additional sortal stereotypes have the following semantics:

    - Subkind: Subkinds are rigid specializations of a kind. For example, we can have Man as a subkind of Person.

    - Phase: Phases are 'sortals whose contingent classification conditions are intrinsic'. They represent changes in intrinsic properties of instances of a kind, for example, in the case of the age of instances of the kind person, we can have phases such as Child, Teenager and Adult.

    - Role: Roles are 'sortals whose contingent classification conditions are relational'. They are anti-rigid specializations of kinds, for example, the role student of the kind person.

As opposed to sortals, 'non-sortals are types that represent common properties of individuals of multiple Kinds.'. The non-sortal are category, phase-mixin, role-mixin and mixin.

    - Category: Categories are 'rigid types that define essential properties for their instances, e.g., the category 'physical object' describing the properties of having a mass and a spatial extension, common to things of the kinds car, person, bridge, cow, etc”. Or, for example, we can have the category Furniture, which describes properties of things that are usually used in a house by humans for many purposes.

    - phase-mixin: Phase mixins are 'anti-rigid types that define contingent properties for their instances. Their instantiation is characterized by intrinsic contingent conditions. For example, the phase mixin 'living animal' may apply to instances of the kinds person, dog, and horse'

    - mixin: Mixins are 'semi-rigid types that define properties that are essential to some of their instances but accidental to some other instances (e.g., being a 'music artist' is essential to bands but accidental to people).
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
2 - Infer ONE possible OntoUML stereotype for each element with a missing stereotype
3 - Provide the explanation for each stereotypes inferred
4 - Output a json array, where each object contains the following keys: name, inferred_stereotype, explanation. Please, do not truncate the array and always provide every element in the response. Please output the array inside the following characters: ```.

Use the following format for the JSON array:
name: <name of element>
inferred_stereotype: <stereotype inferred for element>
explanation: <reason of inferred stereotype>
Output JSON: <json with the required format>
"""

csv_instructions = f"""
Follow these steps to answer the user queries, and only those steps. Do not try anything else. The user query will be delimited with four hashtags, i.e. {delimiter}.
The user query will be a element name. You MUST provide a stereotype to it.

The possible stereotype for classes are:
[ kind, collective, quantity, quality, mode, relator, subkind, phase, role, historicalRole, historicalRoleMixin, category, phaseMixin, roleMixin, mixin, type, event, situation, process ]

The possible stereotypes for relations are:
[ material, derivation, comparative, mediation, characterization, externalDependence, componentOf, memberOf, subCollectionOf, subQuantityOf, instantiation, termination, participational, participation, historicalDependence, creation, manifestation, bringsAbout, triggers, composition, aggregation, inherence, value, formal ]

Your task is to perform the following actions: 
1 - Read the name of the element
2 - Infer ONE possible OntoUML stereotype for the element
3 - Output the inferred stereotype, and ONLY that stereotype.

Do not output any other text. I want the answer to be exactly one stereotype and nothing more. If you don't understand the prompt, output "None"

An example:
```
prompt: Person
kind
```
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
        {"role": "system", "content": ufo_explanation},
        {"role": "system", "content": stereotypes_explanation},
        {"role": "system", "content": csv_instructions},
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
