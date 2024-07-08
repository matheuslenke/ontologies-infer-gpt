```json
[
{
"name": "TestCase",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type that represents a test case, providing principles of individuation, identity, and persistence to its instances. Examples: Specific test cases like 'Login Functionality Test', 'Data Retrieval Test'."
},
{
"name": "Precondition",
"inferred_stereotype": "role",
"explanation": "An anti-rigid specialization of a kind, representing a state or condition that must be true before a test case can be executed. It depends on the relationship with the test case. Example: 'User account must be created' for a 'Login Functionality Test'."
},
{
"name": "RequirementTestCase",
"inferred_stereotype": "relator",
"explanation": "Represents the relationship between a Requirement and a TestCase, indicating which test cases verify a specific requirement. It acts as the truth-maker for the connection between these two entities. Example: The 'Login Functionality Test' is linked to the requirement 'System shall allow registered users to log in'."
},
{
"name": "FunctionalRequirement",
"inferred_stereotype": "subkind",
"explanation": "A rigid specialization of the kind 'Requirement', representing requirements related to the system's functionality.  Example: 'The system shall allow users to search for products'."
},
{
"name": "UseCase",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type representing a use case, which describes how a user interacts with the system to achieve a specific goal. Examples: 'User Login', 'Search for Products', 'Make a Purchase'."
},
{
"name": "BasicFlow",
"inferred_stereotype": "role",
"explanation": "An anti-rigid specialization of the kind 'Flow', representing the typical or normal sequence of actions within a use case. It depends on the relationship with the use case. Example: The normal steps for 'User Login' would be 'Enter credentials', 'System verifies credentials', 'User is granted access'."
},
{
"name": "Requirement",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type representing a condition or capability needed by a stakeholder. Examples: 'The system shall be secure', 'The system shall be user-friendly'."
},
{
"name": "Artifact",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type representing a piece of information produced during the software development process. Examples: Design documents, code files, test scripts, meeting minutes."
},
{
"name": "Project",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type representing a temporary endeavor undertaken to create a unique product, service, or result. Examples: 'E-commerce Website Development', 'Mobile App Design'."
},
{
"name": "UseTestCase",
"inferred_stereotype": "relator",
"explanation": "Represents the relationship between a UseCase and a TestCase, indicating which test cases are designed to test a specific use case. Example: The 'User Login' use case is linked to the test case 'Successful Login Attempt'."
},
{
"name": "Module",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type representing a distinct and independent unit of source code, often with a specific function or responsibility. Examples: 'User Authentication Module', 'Payment Processing Module'."
},
{
"name": "NonFunctionalRequirement",
"inferred_stereotype": "subkind",
"explanation": "A rigid specialization of the kind 'Requirement', representing constraints on the system's qualities or attributes. Examples: 'The system shall respond to user requests within 2 seconds', 'The system shall be available 99.9% of the time'."
},
{
"name": "AlternativeFlow",
"inferred_stereotype": "role",
"explanation": "An anti-rigid specialization of the kind 'Flow', representing a deviation from the normal course of actions within a use case. Example: In the 'User Login' use case, an alternative flow could be 'Forgotten password', where the user can request a password reset."
},
{
"name": "Postcondition",
"inferred_stereotype": "role",
"explanation": "An anti-rigid specialization of a kind, representing a state or condition that must be true after a test case is executed successfully. Example: After a successful 'Create User Account' test, a postcondition would be 'User account exists in the database'."
},
{
"name": "EntityType",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type representing a significant category of information that the system stores and manages. Examples: 'Customer', 'Product', 'Order'."
},
{
"name": "BusinessRule",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type representing a specific, practicable, and testable directive that guides business operations and reflects business policies or practices. Examples: 'A customer must be 18 years old to make a purchase', 'All orders must have a valid shipping address'."
},
{
"name": "Class",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type representing a blueprint or template for creating objects within the software system. It defines the attributes and behaviors that objects of that class will possess. Examples: 'User', 'Product', 'ShoppingCart'."
},
{
"name": "ClassTestCase",
"inferred_stereotype": "relator",
"explanation": "Represents the relationship between a Class and a TestCase, indicating which test cases are designed to test the functionality of a specific class. It connects the test case to the code it's meant to validate."
},
{
"name": "EventFlow",
"inferred_stereotype": "subkind",
"explanation": "A rigid specialization of the kind 'Flow', representing a sequence of actions or events within the system, often triggered by external stimuli or user interactions. It describes the flow of events in the system's behavior. Example: 'Order Processing Flow' that starts with a customer placing an order and ends with the order being shipped."
},
{
"name": "Condition",
"inferred_stereotype": "kind",
"explanation": "A fundamental sort of endurant type representing a factor or situation that affects an action, decision, or outcome.  Examples: 'Inventory Level', 'Payment Authorization Status'."
}
]
```