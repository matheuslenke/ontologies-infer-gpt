```json
[
  {
    "name": "Base Table",
    "description": "A fundamental table in a relational database schema. It holds data that is persistent and from which other tables (views or materialized views) can be derived.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Software Item",
    "description": "A distinct piece of software, representing a broader category encompassing various software types.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Loaded Software System Copy",
    "description": "A specific instance of a Software System that has been installed and is operational on a Computer System.",
    "inferred_stereotype": "phase" 
  },
  {
    "name": "DBMS Account",
    "description": "Credentials and permissions granted to a user or application to interact with a DBMS.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "External Data Type",
    "description": "How data is represented to users of a database system, focusing on the user's perspective.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "RDBMS",
    "description": "A type of database system that organizes data into tables with rows and columns, adhering to relational principles.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Artifact",
    "description": "A general term used for any product of software development (documents, code, executables, database schemas, etc.)",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Database System",
    "description": "An organized collection of data, generally stored and accessed electronically. This is a general term, encompassing various types like RDBMS, NoSQL, etc.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Check Constraint",
    "description": "A rule that limits the values allowed in a column or across multiple columns in a database table, ensuring data integrity by enforcing specific conditions.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Data Type Constraint",
    "description": "A constraint that enforces the permissible data types for a given attribute or column in a database, contributing to data consistency and validity.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Software System",
    "description": "A collection of interacting software components (programs, libraries, data, etc.) organized for a specific purpose.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Data File",
    "description": "A computer file for storing data, potentially used by a DBMS.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Data Schema",
    "description": "A formal description of the structure of data within a database system, defining tables, columns, relationships, and constraints.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Column Constraint",
    "description": "A rule or limitation specifically applied to a single column in a database table to maintain data integrity.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Line",
    "description": "Potentially refers to a row within a table in a database. More context is needed to be certain. Could also be a line of code in software.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Primary Key Column",
    "description": "A column or set of columns that uniquely identify a row in a database table. Primary keys are essential for relationships and data integrity.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Schema",
    "description": "A general term for a structured framework or plan. In the context of databases, it typically refers to the database schema.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Language",
    "description": "A structured system of communication. In this context, it might refer to programming languages used with the DBMS or a Data Definition Language.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Dictionary",
    "description": "Could refer to the data dictionary within a DBMS, which stores metadata about the database.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Relational Database",
    "description": "A database organized based on the relational model using tables with rows and columns. ",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Line Type",
    "description": "Unclear without further context. Requires more information to determine its specific meaning and applicable stereotype.",
    "inferred_stereotype": ""
  },
  {
    "name": "Relational Database System",
    "description": "A software system for creating and managing relational databases. Synonymous with RDBMS.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Column",
    "description": "A vertical structure in a table that represents a specific attribute of the data being stored.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Data Type",
    "description": "A classification that defines the kind of values a variable can hold (e.g., integer, string, date). Essential for data integrity and operations.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Internal Data Type",
    "description": "How data is physically stored and managed within a DBMS. This is an implementation detail hidden from users.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "DBMS",
    "description": "Database Management System: A software application for creating, managing, and accessing a database.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Computer System",
    "description": "A system that includes hardware and software components working together. The DBMS is typically installed and runs on a computer system.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "DBMS Item",
    "description": "A very broad term. More context is needed. Could be any element managed by a DBMS.",
    "inferred_stereotype": ""
  },
  {
    "name": "Information Schema",
    "description": "A set of tables in a relational database system that provides metadata about the database's structure and organization.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Constraint",
    "description": "A rule that restricts the data that can be entered into a database, ensuring data integrity.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Column Type Constraint",
    "description": "A type of constraint that specifically limits the data type allowed in a table column.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Derived Table",
    "description": "A table created from one or more existing tables through queries. Its data is derived from the base tables and not persistently stored.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Loaded RDBMS Copy",
    "description": "A specific installation and running instance of a Relational Database Management System.",
    "inferred_stereotype": "phase"
  },
  {
    "name": "Relational Schema",
    "description": "A schema specifically designed for a relational database.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Relational Data Language",
    "description": "A language used to interact with relational databases, commonly SQL.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "RDBMS Item",
    "description": "Similar to 'DBMS Item,' this is very general. Without context, it's too broad to assign a specific stereotype.",
    "inferred_stereotype": ""
  },
  {
    "name": "Foreign Key Column",
    "description": "A column in a relational database table that establishes a link to a primary key column in another table, representing relationships between entities.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Primary Key Constraint",
    "description": "A constraint that enforces the uniqueness and non-null properties of a primary key in a database table.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Foreign Key Constraint",
    "description": "A constraint that enforces referential integrity between tables by ensuring that values in the foreign key column correspond to existing primary key values in the related table.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Database",
    "description": "An organized collection of data, managed by a DBMS.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Data Language",
    "description": "A language used for defining, manipulating, and controlling data in a database.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Table",
    "description": "A collection of data organized in rows and columns, a fundamental structure in relational databases.",
    "inferred_stereotype": "subkind"
  }
]
```