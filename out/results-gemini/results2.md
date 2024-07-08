```json
[
  {
    "name": "Entity Subclass",
    "description": "A class that inherits from another entity class, representing a specialized type of entity within the database model.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Single Entity Table",
    "description": "A database table that stores data for instances of a single entity class, even if it has subclasses. Used in single table inheritance strategies.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Instance Variable",
    "description": "A variable or attribute associated with an instance of an entity class, representing a specific data point for that entity.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Entity Superclass",
    "description": "A general entity class from which other entity classes (subclasses) inherit properties and relationships.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Entity Table",
    "description": "A database table designed to store data for instances of a particular entity class.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Foreign Key Column",
    "description": "A column in a database table that references the primary key of another table, establishing a link between the two tables.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "One To Many Relationship Mapping",
    "description": "The process of mapping a one-to-many relationship between two entity classes to database tables, usually involving foreign keys.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Column",
    "description": "A fundamental unit of structure within a database table, representing a specific attribute or data field for the entities stored in the table.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Mapped Primary Key",
    "description": "The primary key of an entity class that is mapped to a specific column in a database table.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Nullability",
    "description": "A property of a column in a database table that determines whether the column can contain null values, affecting data integrity.",
    "inferred_stereotype": "quality" 
  },
  {
    "name": "Many to Many Relationship Mapping",
    "description": "The process of mapping a many-to-many relationship between entity classes to database tables, typically using an association table.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Table per Class Inheritance Mapping",
    "description": "An inheritance mapping strategy where each class in the hierarchy, including abstract classes, has its own database table.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Relationship Mapping",
    "description": "The overall process of representing relationships between entity classes within the structure of database tables.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Relationship Association Table",
    "description": "A dedicated database table used to represent a many-to-many relationship between two or more entity tables.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Variable Mapping",
    "description": "The process of mapping variables or attributes of an entity class to specific columns in a database table.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Entity Class",
    "description": "A class that represents a type of entity or data structure within a database model, defining its properties and relationships.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Spuerclass",
    "description": "Likely a typo and should be 'Superclass'. Assuming this refers to a superclass in an inheritance hierarchy.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Mapped Variable",
    "description": "An instance variable or attribute of an entity class that is directly mapped to a column in a database table.",
    "inferred_stereotype": "role"
  },
  {
    "name": "Multiple Entities Table",
    "description": "A database table designed to store data for instances of multiple entity classes.", 
    "inferred_stereotype": "role"
  },
  {
    "name": "Inheritance",
    "description": "A fundamental concept in object-oriented programming where a subclass inherits properties and behaviors from its superclass.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Primary Key Column",
    "description": "A designated column in a database table that uniquely identifies each row or record within that table.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Extendable Class",
    "description": "A class designed in a way that allows other classes (subclasses) to inherit from it and extend its functionality.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Class",
    "description": "A fundamental concept in object-oriented programming, representing a blueprint or template for creating objects.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Inheritance Mapping",
    "description": "The process of defining how an inheritance hierarchy of classes is translated into a relational database schema.",
    "inferred_stereotype": "relator"
  },
  {
    "name": "Class Mapping",
    "description": "The process of mapping a class, its attributes, and relationships to a database schema, including tables and columns.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Subclass",
    "description": "A class that inherits properties and behaviors from its superclass, representing a more specialized type of object.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Single Table Inheritance Mapping",
    "description": "A strategy for mapping an inheritance hierarchy to a database where all subclasses share a single table with a discriminator column.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Foreign Key Mapping",
    "description": "The process of mapping a foreign key relationship between classes or entities to columns in database tables.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Mapped Foreign Key",
    "description": "A foreign key in an entity class that has a corresponding column mapping in a database table.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Primary Key Mapping",
    "description": "The mapping of the primary key attribute of an entity class to a specific column in a database table.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Many To One Relationship Mapping",
    "description": "The process of mapping a many-to-one relationship, where multiple instances of one entity can be associated with a single instance of another.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "One To One Relationship Mapping",
    "description": "Mapping a relationship where a single instance of one entity is associated with a single instance of another entity.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Table per Concrete Class Inheritance Mapping",
    "description": "An inheritance mapping strategy where each concrete class in the hierarchy has its own database table, but abstract classes do not.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Table",
    "description": "A fundamental component of a relational database, organized into rows and columns to store and organize data.",
    "inferred_stereotype": "kind" 
  }
]
```
