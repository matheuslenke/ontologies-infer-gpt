Prompt items: 
Type Parameter, Artifact, Non-Extendable Class, Software Item, Generic Method, Block, Non-Overridable Method, Element Visibility, Abstract Method, Concrete Method, Physical Module, Extendable Class, Language, Programming Language, Nesting, Class Variable, Member, Name, Local Variable, Instance Method, Object-Oriented Programming Language, Module, Class, Accessor Method, Subclass, Type, Variable, Instance Variable, Concrete Class, Class Method, Method (Member Function), Generic Class, Source Code, Inheritance Visibility, Overridable Method, Destructor Method, Object-Oriented Source Code, Nested Class, Type Parameter, Method Variable, Named Element, Logical Module, Root Class, Primitive Type, Attribute (Member Variable), Inheritance, Parameter Variabe, Return Type, Mutability, Value Type, Program, Superclass, Code, Abstract Class, Constructor Method, Software System, 
amout of items: 56
 1 - Reading the name of every element
Artifact: A tangible entity created or constructed for a specific purpose
Non-Extendable Class: A class that cannot have any subclasses derived from it
Software Item: An item within a software system, such as code files, modules, or classes
Generic Method: A method with multiple instantiations based on the types of arguments passed to it
Block: A section of code enclosed by braces and defining a scope
Non-Overridable Method: A method in a superclass that cannot be overridden in any subclasses
Element Visibility: The level of accessibility of an element within a program
Abstract Method: A method in an abstract class with no implementation, requiring its concrete subclasses to define it
Concrete Method: An implemented method in a regular class or structure
Physical Module: A module that can be physically accessed or manipulated, such as a hardware component
Extendable Class: A class that allows other classes to inherit from it
Language: A formal language used for communication or programming, like Python or Java
Programming Language: A programming language used to create software systems or applications
Nesting: The organization of one structure inside another within the same scope
Class Variable: A variable shared among all instances of a class or structure
Member: An element belonging to an object, such as a method or property
Name: The identifier given to an element in a program
Local Variable: A variable defined within a function or block with local scope
Instance Method: A method that can be called on an instance of a class or object
Object-Oriented Programming Language: A programming language based on the principles of objects and classes, like Java or C++
Module: A self-contained section of a software system, containing related classes, functions, or other code components
Accessor Method: A method used to retrieve or modify an attribute or property of an object
Subclass: A class that inherits properties and behavior from another class
Type: A category of values or entities in a programming context
Variable: A container for storing values within a program
Instance Variable: A variable specific to each instance of a class
Concrete Class: A class with implemented methods and attributes
Class Method: A static method belonging to a class, not requiring an object instance
Method (Member Function): A function that is a member of an object or class in an object-oriented program
Generic Class: A class template with multiple instantiations based on the types of arguments passed to it
Source Code: The human-readable code written for software systems
Inheritance Visibility: The visibility level of inherited members within a subclass hierarchy
Overridable Method: A method in a superclass that can be overridden by a concrete subclass
Destructor Method: A method called when an instance of an object is about to be destroyed or cleaned up
Object-Oriented Source Code: Source code written in an object-oriented programming language
Nested Class: A class defined within another class, creating a nested scope and relationship
Type Parameter: A parameter that specifies the type of an argument passed to a generic method or class
Method Variable: A variable used within a method definition
Named Element: An element identified by a name in a program or design context
Logical Module: A module defined conceptually, not necessarily physically present
Root Class: The most general or fundamental class from which others inherit
Primitive Type: A basic type that cannot be broken down into smaller parts within a programming context
Attribute (Member Variable): A property or characteristic of an object or class instance
Inheritance: The process by which one class acquires the properties and methods of another
Parameter Variabe: A variable that represents an argument passed to a function or method
Return Type: The data type that a function or method returns as its output
Mutability: The ability for a value or variable to be modified within a program
Value Type: A data type representing values, such as integers or strings
Program: A collection of source code files organized into a software system
Superclass: The parent class from which another class inherits properties and methods
Constructor Method: A special method used to create new instances of a class
Software System: An integrated set of computer programs designed to perform specific functions

2 - DO NOT ask any questions. Only do as instructed.

3 - Writing the corresponding Rust structures for each element name
Artifact: Not directly represented in Rust, but could be modeled as a struct or enum with associated fields and methods
NonExtendableClass: A simple struct with no implicit implementation of traits
SoftwareItem: Could be modeled as a trait with associated impl blocks for various programming languages, each containing specific implementations for items within the language (e.g., File, Module, Function)
GenericMethod: Representation through the use of type parameters and associated functions
Block: Not directly represented in Rust, but can be simulated using indentation, braces, and scoping rules
NonOverridableMethod: A method declared with the keyword 'final' to prevent overriding by subclasses or traits
ElementVisibility: Rust does not have explicit visibility levels like other languages (e.g., public, private, protected), but you can use modular organization and access control techniques to mimic this behavior
AbstractMethod: A method defined in an abstract trait or struct using the keyword 'type' for abstract types
ConcreteMethod: Implemented methods for a given trait or struct
PhysicalModule: Not directly represented in Rust, but could be modeled as a path-based module system
ExtendableClass: A simple struct with the trait 'std::iter::Extend' implemented to allow additional elements to be added
Language: Not directly relevant to Rust itself, but you can create libraries or crates for different programming languages and their associated structures (e.g., a C++ crate)
ProgrammingLanguage: See "Language" above
Nesting: Managed through indentation, braces, and scoping rules in Rust
ClassVariable: A static variable shared among all instances of a struct or trait
Member: A field or function defined within a struct, enum, or trait
Name: Not directly relevant to Rust itself, but can be handled using the 'String' type for identifiers
LocalVariable: Defined with the keyword 'let' and has scope limited to its containing block or closure
InstanceMethod: Methods associated with a specific instance of a struct or trait object
ObjectOrientedProgrammingLanguage: See "Language" above
Module: Organized using Rust's path-based module system (e.g., mod prelude)
AccessorMethod: Methods defined to read or modify the fields of a struct or enum
Subclass: Achieved through inheritance using the 'super' keyword and trait composition techniques
Type: Basic types like i32, f64, String, and user-defined enums or structs
Variable: Representation as a mutable or immutable value with a given type in Rust
InstanceVariable: Defined with the keyword 'self' to refer to the current struct instance
ConcreteClass: A struct or trait with implemented methods and attributes
ClassMethod: Static methods are defined with the keyword 'static' and can be called on the type itself without an instance
Method (Member Function): Methods associated with a struct, enum, or trait object
GenericClass: Representation through use of generic types (e.g., <T>, <U>) in conjunction with associated functions
SourceCode: Not directly represented in Rust, but can be saved as .rs files
InheritanceVisibility: The visibility of inherited members is determined by their declaration location and scope rules within the codebase
OverridableMethod: A method that can be overridden by subclasses or traits (no need for 'final' keyword in Rust)
DestructorMethod: Not directly represented in Rust, but you can clean up resources using 'drop' or 'impl Drop' implementation on structs or enums
ObjectOrientedSourceCode: See "SourceCode" above
NestedClass: Defined within another struct or trait with the use of nested modules or associated functions
TypeParameter: Representation through the use of <T>, <U> (and higher-order generic types like fn and impl) in Rust
MethodVariable: Declared using let within function or method blocks, similar to local variables
NamedElement: Not directly relevant to Rust itself, but can be managed by giving unique names to functions, variables, structs, or traits
LogicalModule: See "Module" above
RootClass: The top-level struct or trait defining your program's structure and behavior
PrimitiveType: Basic types like i32, f64, char, String, etc. (including custom enum variants and struct fields)
Attribute (Member Variable): Fields defined within a struct or enum to store associated data
Inheritance: Achieved through inheritance using the 'super' keyword and trait composition techniques
ParameterVariable: Representation as positional or named arguments in function signatures
Function: Implemented using fn definitions, with parameters declared in their signature and the associated body block
