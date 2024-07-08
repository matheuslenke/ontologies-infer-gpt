1 - Read the name of every element
2 - Infer ONE possible OntoUML stereotype for each element with a missing stereotype
3 - Provide the explanation for each stereotype inferred
4 - Output a json array, where each object contains the following keys: name, inferred_stereotype, explanation.

```json
[
{
"name": "Proposition",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents a statement or assertion that can be true or false."
},
{
"name": "Disposition",
"inferred_stereotype": "mode",
"explanation": "Represents a property that is a tendency or inclination of an entity to behave in a certain way under certain circumstances."
},
{
"name": "System Component",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents a constituent part of a system, typically with a specific function."
},
{
"name": "System Requirements Specification",
"inferred_stereotype": "artifact",
"explanation": "Represents a document or collection of documents that specify the requirements of a system."
},
{
"name": "Agent",
"inferred_stereotype": "role",
"explanation": "An anti-rigid specialization of a kind that represents an entity that can act autonomously and purposefully."
},
{
"name": "Machine",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents a physical device or system that performs a specific function."
},
{
"name": "Event",
"inferred_stereotype": "event",
"explanation": "Represents a significant occurrence or happening that occurs at a specific point in time."
},
{
"name": "Loaded Program Copy",
"inferred_stereotype": "situation",
"explanation": "Represents a state of affairs where a program is loaded into memory and ready for execution."
},
{
"name": "Business Requirements Specification",
"inferred_stereotype": "artifact",
"explanation": "Represents a document or collection of documents that specify the requirements of a business."
},
{
"name": "System Requirement",
"inferred_stereotype": "proposition",
"explanation": "A fundamental sort of endurant type that represents a statement about a desired attribute or capability of a system."
},
{
"name": "Program Requirement",
"inferred_stereotype": "proposition",
"explanation": "A fundamental sort of endurant type that represents a statement about a desired attribute or capability of a program."
},
{
"name": "Business Requirement",
"inferred_stereotype": "proposition",
"explanation": "A fundamental sort of endurant type that represents a statement about a desired attribute or capability of a business."
},
{
"name": "Program Copy Execution",
"inferred_stereotype": "process",
"explanation": "Represents the execution of a program, involving a series of actions or operations."
},
{
"name": "Goal",
"inferred_stereotype": "proposition",
"explanation": "A fundamental sort of endurant type that represents a desired state or outcome."
},
{
"name": "World Assumption",
"inferred_stereotype": "proposition",
"explanation": "A fundamental sort of endurant type that represents an assumption about the state of the world or a specific domain."
},
{
"name": "Normative Description",
"inferred_stereotype": "artifact",
"explanation": "Represents a document or specification that outlines rules, guidelines, or standards."
},
{
"name": "System Element",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents a general term for any constituent part of a system."
},
{
"name": "SubSystem",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents a self-contained system within a larger system."
},
{
"name": "Stakeholder",
"inferred_stereotype": "role",
"explanation": "An anti-rigid specialization of a kind that represents an individual or group with an interest in a particular system or project."
},
{
"name": "Business Constraint",
"inferred_stereotype": "proposition",
"explanation": "A fundamental sort of endurant type that represents a limitation or restriction on a business or its operations."
},
{
"name": "Artifact",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents a human-made object, typically a document or a piece of software."
},
{
"name": "Hardware Equipment",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents physical components of a computer system."
},
{
"name": "External Business Regulations",
"inferred_stereotype": "artifact",
"explanation": "Represents documents or regulations imposed by external entities that govern business operations."
},
{
"name": "Stakeholder Requirements Specification",
"inferred_stereotype": "artifact",
"explanation": "Represents a document or collection of documents that specify the requirements of stakeholders."
},
{
"name": "(Internal) Business Rule",
"inferred_stereotype": "proposition",
"explanation": "A fundamental sort of endurant type that represents an internal rule or guideline that governs business operations."
},
{
"name": "Program",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents a set of instructions that a computer can execute."
},
{
"name": "Organization",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents a group of people with a common purpose or goal."
},
{
"name": "Software System",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents a collection of computer programs, procedures, and documentation."
},
{
"name": "Stakeholder Requirement",
"inferred_stereotype": "proposition",
"explanation": "A fundamental sort of endurant type that represents a statement about a desired attribute or capability from a stakeholder's perspective."
},
{
"name": "Machine Assumption",
"inferred_stereotype": "proposition",
"explanation": "A fundamental sort of endurant type that represents an assumption about the capabilities or behavior of a machine."
},
{
"name": "Program Specification",
"inferred_stereotype": "artifact",
"explanation": "Represents a document or collection of documents that specify the design and behavior of a program."
}
]
```