```json
[
  {
    "name": "Primary Key Column",
    "description": "A column in a database table that uniquely identifies each row in the table.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Spuerclass",
    "description": "Assumed to be a misspelling of 'Superclass'.  A superclass in an inheritance hierarchy.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Column",
    "description": "A vertical division of a table that holds data of a specific type.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Single Entity Table",
    "description": "A table in a database that holds data for a single entity type.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Class Mapping",
    "description": "The process of mapping a class in the application code to a table in the database.",
    "inferred_stereotype": "relator"
  },
  {
    "name": "Table",
    "description": "A collection of related data held in a structured format within a database.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Relationship Mapping",
    "description": "The process of mapping relationships between entities in the application code to tables or constraints in the database.",
    "inferred_stereotype": "relator"
  },
  {
    "name": "Mapped Variable",
    "description": "A variable in a class that is mapped to a specific column in a database table.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Class",
    "description": "A blueprint or template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Many to Many Relationship Mapping",
    "description": "The process of mapping a many-to-many relationship between entities to a database schema, usually involving an intermediate association table.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Variable Mapping",
    "description": "The process of mapping a variable in a class to a corresponding element in another structure, such as a database table.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Primary Key Mapping",
    "description": "The process of mapping the primary key of an entity in the application code to the corresponding primary key column in a database table.",
    "inferred_stereotype": "relator"
  },
  {
    "name": "Subclass",
    "description": "A class that is derived from another class (its superclass), inheriting its properties and behaviors and potentially adding its own.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Single Table Inheritance Mapping",
    "description": "A strategy for mapping an inheritance hierarchy to a relational database where all classes in the hierarchy are mapped to a single table.",
    "inferred_stereotype": "relator"
  },
  {
    "name": "Mapped Primary Key",
    "description": "A primary key in the application code that is mapped to a corresponding primary key column in a database table.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Nullability",
    "description": "A property of a column in a database table that defines whether or not it can contain null values.",
    "inferred_stereotype": "quality" 
  },
  {
    "name": "Extendable Class",
    "description": "A class designed and implemented in a way that allows other classes to inherit from it (i.e., to be its subclasses).",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "One To Many Relationship Mapping",
    "description": "The process of mapping a one-to-many relationship between entities in the application code to a database schema, typically using a foreign key in the 'many' side's table.",
    "inferred_stereotype": "relator"
  },
  {
    "name": "Table per Concrete Class Inheritance Mapping",
    "description": "A strategy for mapping an inheritance hierarchy to a relational database where each concrete class (i.e., a class that can be instantiated) has its own table.",
    "inferred_stereotype": "relator"
  },
  {
    "name": "Entity Subclass",
    "description": "A subclass in an inheritance hierarchy that represents a specific type of entity in the system.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Mapped Foreign Key",
    "description": "A foreign key in the application code that is mapped to a corresponding foreign key column in a database table.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Inheritance",
    "description": "A mechanism in object-oriented programming where a class (subclass) can inherit properties and behaviors from another class (superclass).",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Inheritance Mapping",
    "description": "The process of mapping an inheritance hierarchy from an object-oriented model to a relational database schema.",
    "inferred_stereotype": "relator"
  },
  {
    "name": "Table per Class Inheritance Mapping",
    "description": "A strategy for mapping an inheritance hierarchy to a relational database where each class in the hierarchy, including abstract classes, has its own table.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Multiple Entities Table",
    "description": "A table in a database that holds data for multiple entity types, typically used in specific inheritance mapping scenarios.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Many To One Relationship Mapping",
    "description": "The process of mapping a many-to-one relationship between entities in the application code to a database schema, typically using a foreign key in the 'many' side's table.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Relationship Association Table",
    "description": "An intermediary table in a database used to represent a many-to-many relationship between two other tables.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Entity Table",
    "description": "A table in a database that represents a specific type of entity and holds data for instances of that entity.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Foreign Key Mapping",
    "description": "The process of mapping a foreign key constraint in the application code to the corresponding foreign key column(s) in a database table.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "One To One Relationship Mapping",
    "description": "The process of mapping a one-to-one relationship between entities in the application code to a database schema, often using a shared primary key or a unique foreign key constraint.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Foreign Key Column",
    "description": "A column in a database table that establishes a link to the primary key of another table, representing a relationship between the two tables.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Entity Superclass",
    "description": "A superclass in an inheritance hierarchy that represents a general type of entity in the system.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Instance Variable",
    "description": "A variable associated with individual instances of a class. Each instance of the class has its own copy of the instance variable.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Entity Class",
    "description": "A class in an object-oriented model that represents a data entity in the system, often mapped to a table in a relational database.",
    "inferred_stereotype": "role" 
  }
]
```