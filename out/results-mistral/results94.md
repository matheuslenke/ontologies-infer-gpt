Prompt items: 
Design Evaluation, Performed Activity, Software Product, Interface High-level Design, Architectural Component, Architectural Connector, Requirements Document, Artifact, Detailed Design, Model, Software Item, Performed Process, Architectural Element, Data Model, Architecture Development, Performed Composite Activity, Software Architect, Component Design, Designer, Composite Artifact, Software Architecture, Simple Artifact, Stakeholder, Design Evaluation Document, Performed General Process, User Interface Specification, Data Definitions, Information Item, Component Interface Design, Data High-level Design, Interface Specification, Document, Design Documentation, Architectural Design, User Inteface Design, Data Design, Performed Simple Activity, Design Process, Performed Specific Process, Design Document, 
amout of items: 40
 Understood: I have a list of element names. For each element with no stereotype defined, I will infer one possible OntoUML stereotype from the provided list and output a CSV with two columns: name (the name of the element) and inferred_stereotype (the stereotype that I inferred).

Inferred_stereotypes:
- Design Evaluation: None
- Performed Activity: Event
- Software Product: None
- Interface High-level Design: None
- Architectural Component: Kind
- Architectural Connector: Relator
- Requirements Document: Category
- Artifact: None
- Detailed Design: None
- Model: None
- Software Item: None
- Performed Process: Process
- Architectural Element: Kind
- Data Model: Kind
- Architecture Development: Process
- Performed Composite Activity: CompositeActivity
- Software Architect: Role
- Component Design: RoleMixin
- Designer: Role
- Composite Artifact: CompositeArtifact
- Software Architecture: Category
- Simple Artifact: Type
- Stakeholder: None
- Design Evaluation Document: Document
- Performed General Process: GeneralProcess
- User Interface Specification: None
- Data Definitions: Mixin
- Information Item: Quality
- Component Interface Design: RoleMixin
- Data High-level Design: None
- Interface Specification: Type
- Document: Document
- Design Documentation: Category
- Architectural Design: Process
- User Inteface Design: Phase
- Data Design: Phase
- Performed Simple Activity: SimpleActivity
- Design Process: Process
- Performed Specific Process: None (since no more specific stereotype is given for this element)

Output CSV:
name,inferred_stereotype
Design Evaluation,,
Performed Activity,Event
Software Product,,
Interface High-level Design,,
Architectural Component,Kind
Architectural Connector,Relator
Requirements Document,Category
Artifact,,
Detailed Design,,
Model,,
Software Item,,
Performed Process,Process
Architectural Element,Kind
Data Model,Kind
Architecture Development,Process
Performed Composite Activity,CompositeActivity
Software Architect,Role
Component Design,RoleMixin
Designer,Role
Composite Artifact,CompositeArtifact
Software Architecture,Category
Simple Artifact,Type
Stakeholder,,
Design Evaluation Document,Document
Performed General Process,GeneralProcess
User Interface Specification,,
Data Definitions,Mixin
Information Item,Quality
Component Interface Design,RoleMixin
Data High-level Design,,
Interface Specification,Type
Document,Document
Design Documentation,Category
Architectural Design,Process
User Inteface Design,Phase
Data Design,Phase
Performed Simple Activity,SimpleActivity
Design Process,Process
Performed Specific Process,,
