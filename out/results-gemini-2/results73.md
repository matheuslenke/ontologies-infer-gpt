1 - Read the name of every element
2 - Infer ONE possible OntoUML stereotype for each element with a missing stereotype
3 - Provide the explanation for each stereoype inferred
4 - Output a json array, where each object contains the following keys: name, inferred_stereotype, explanation.

```json
[
{
"name": "Quality Constraint",
"inferred_stereotype": "type",
"explanation": "Represents a restriction or limitation on a quality."
},
{
"name": "Functional Requirement",
"inferred_stereotype": "type",
"explanation": "Represents a function that a system or component must be able to perform."
},
{
"name": "Intention",
"inferred_stereotype": "type",
"explanation": "Represents a goal, objective, or desired outcome that a stakeholder or system aims to achieve."
},
{
"name": "Gradable Quality Region",
"inferred_stereotype": "type",
"explanation": "Represents a range or interval of values for a quality that can be assessed on a scale or continuum."
},
{
"name": "Quality Structure",
"inferred_stereotype": "type",
"explanation": "Represents the organization or composition of multiple qualities into a hierarchical or interconnected structure."
},
{
"name": "Gradable NFR",
"inferred_stereotype": "type",
"explanation": "Represents a non-functional requirement that can be evaluated or measured on a graded scale."
},
{
"name": "Crisp Quality Region",
"inferred_stereotype": "type",
"explanation": "Represents a precise and clearly defined range or set of acceptable values for a quality."
},
{
"name": "Quality Universal",
"inferred_stereotype": "type",
"explanation": "Represents a high-level or abstract concept of quality that encompasses multiple specific qualities or dimensions."
},
{
"name": "Quality",
"inferred_stereotype": "type",
"explanation": "Represents a characteristic, property, or attribute of a system, product, or process that is relevant to its stakeholders and can be assessed or evaluated."
},
{
"name": "Quality Region",
"inferred_stereotype": "type",
"explanation": "Represents a specific range, interval, or set of values for a quality that is considered acceptable, desirable, or relevant."
},
{
"name": "NFR (Quality Goal)",
"inferred_stereotype": "type",
"explanation": "Represents a non-functional requirement that expresses a desired level or target for a quality attribute."
},
{
"name": "Goal",
"inferred_stereotype": "type",
"explanation": "Represents a desired state, outcome, or objective that a stakeholder or system aims to achieve."
},
{
"name": "Hardgoal",
"inferred_stereotype": "type",
"explanation": "Represents a goal that must be fully satisfied or achieved without any compromise."
},
{
"name": "Function",
"inferred_stereotype": "type",
"explanation": "Represents a specific task, operation, or action that a system or component is designed to perform."
},
{
"name": "Softgoal",
"inferred_stereotype": "type",
"explanation": "Represents a goal that is desirable to achieve but may be subject to trade-offs or partial fulfillment."
},
{
"name": "Quality Value",
"inferred_stereotype": "type",
"explanation": "Represents a specific measurement, assessment, or rating of a quality attribute."
},
{
"name": "Vague NFR",
"inferred_stereotype": "type",
"explanation": "Represents a non-functional requirement that is not precisely defined or may have multiple interpretations."
},
{
"name": "Situation",
"inferred_stereotype": "situation",
"explanation": "Represents a state of affairs or a set of circumstances that exist at a particular point in time or over a period of time."
}
]
```