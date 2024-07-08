```json
[
  {
    "name": "Merged_1",
    "description": "This term seems ambiguous without further context. It could refer to a state resulting from merging other entities or a specific type of merging. Please provide more information.",
    "inferred_stereotype": ""
  },
  {
    "name": "Idea Comment",
    "description": "A comment specifically related to an idea.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Accepted",
    "description": "A state signifying an idea or submission has been positively reviewed and approved.",
    "inferred_stereotype": "phase"
  },
  {
    "name": "Describee",
    "description": "The entity that is being described. This might be too generic without context. Consider if a 'Description' relator wouldn't be more suitable.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Review Category",
    "description": "A category or classification for reviews.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Idea Category",
    "description": "A category or classification for ideas.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Idea Relationship",
    "description": "A relationship between two ideas. This is too broad. Specify the nature of the relationship for a more precise stereotype.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Creation",
    "description": "The act of bringing something new into existence.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "User Group",
    "description": "A group of users.",
    "inferred_stereotype": "collective"
  },
  {
    "name": "Commented Contest",
    "description": "A contest that has received comments. This is likely an unnecessary distinction as most systems allow commenting on contests.",
    "inferred_stereotype": "" 
  },
  {
    "name": "User with Comment",
    "description": "A user who has made a comment. This is redundant; a Participation relator between User and Comment would suffice.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Submitting User",
    "description": "A user who submits something.  Use a Participation relator to indicate the submission action.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Authorization",
    "description": "The act of granting permission or authority.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Idea",
    "description": "A thought or suggestion as to a possible course of action.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Contest with Access Authorization",
    "description": "A contest that has access authorization. Use a relator like 'hasAuthorization' to model this.",
    "inferred_stereotype": ""
  },
  {
    "name": "Submited by Method",
    "description": "Unclear without more context. Likely a relator indicating how something is submitted.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Merged",
    "description": "A state indicating entities have been combined. Consider using a relator to capture the act of merging.",
    "inferred_stereotype": "phase" 
  },
  {
    "name": "Idea Updater User",
    "description": "A user who updates ideas. Use Participation relator to link user to update action.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Category",
    "description": "A class or division of people or things regarded as having particular shared characteristics.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Updated Idea",
    "description": "An idea that has been updated. This is redundant, an Idea can have a state of being 'updated'.",
    "inferred_stereotype": ""
  },
  {
    "name": "Idea with a Comment",
    "description": "Redundant, as with 'User with Comment'.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Edited",
    "description": "A state of having been corrected or modified.",
    "inferred_stereotype": "phase" 
  },
  {
    "name": "Describes Part",
    "description": "Potentially a relator, but unclear without context. Does one entity describe a part of another?",
    "inferred_stereotype": "" 
  },
  {
    "name": "Textual Review",
    "description": "A review in textual form.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "User with Idea Contest Comment",
    "description": "Overly specific. Participation relators can model users commenting on specific contests.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Idea Contest Attachment",
    "description": "An attachment associated with an idea contest.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Similar Idea",
    "description": "Redundant. Model similarity relationships between Ideas with a dedicated relator.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Related Idea",
    "description": "Too vague.  Needs a specific relator to explain the type of relationship.",
    "inferred_stereotype": ""
  },
  {
    "name": "User Editor",
    "description": "A user who edits content. Again, use Participation for the editing action.",
    "inferred_stereotype": ""
  },
  {
    "name": "Partially Implemented",
    "description": "A state indicating partial implementation.",
    "inferred_stereotype": "phase"
  },
  {
    "name": "User with Account",
    "description": "Redundant; Account Ownership relator is more appropriate.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Online Account",
    "description": "An account for accessing online services.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Submission",
    "description": "The act of submitting something, such as an idea or a proposal.",
    "inferred_stereotype": "relator"
  },
  {
    "name": "Submitted Idea",
    "description": "An idea that has been submitted.",
    "inferred_stereotype": "phase" 
  },
  {
    "name": "Idea Attachment",
    "description": "An attachment associated with an idea.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Similaree",
    "description": "Likely a misspelling of 'Similarity', which is best modeled as a relator.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Metric",
    "description": "A system or standard of measurement.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Contest with Idea",
    "description": "Redundant. Contests inherently involve ideas.",
    "inferred_stereotype": ""
  },
  {
    "name": "Updated Contest",
    "description": "A contest that has been updated.",
    "inferred_stereotype": "phase"
  },
  {
    "name": "Revised Idea",
    "description": "An idea that has been revised.",
    "inferred_stereotype": "phase"
  },
  {
    "name": "Relatee",
    "description": "Unclear without more context.  Likely an entity involved in a relationship.",
    "inferred_stereotype": "" 
  },
  {
    "name": "Rejected",
    "description": "A state indicating something has not been accepted.",
    "inferred_stereotype": "phase"
  },
  {
    "name": "Described",
    "description": "A state of having been described. Use a relator to indicate what is describing what.",
    "inferred_stereotype": "phase" 
  },
  {
    "name": "Access Authorized Group",
    "description": "A group that has been granted access authorization.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Merging",
    "description": "The act of combining two or more things into one.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Deployed",
    "description": "A state where something has been made available for use.",
    "inferred_stereotype": "phase"
  },
  {
    "name": "Implemented",
    "description": "A state where something has been put into effect.",
    "inferred_stereotype": "phase" 
  },
  {
    "name": "Rating Review",
    "description": "A review that includes a rating.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "SubCategory",
    "description": "A category that is a subdivision of a larger category.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "User Group in a Group",
    "description": "Redundant; implies hierarchical groups, model with a 'subgroupOf' relator.",
    "inferred_stereotype": ""
  },
  {
    "name": "Similarity",
    "description": "The state or fact of being similar.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Submission Method",
    "description": "A method used for submitting something.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "User",
    "description": "A person who uses a computer or network service.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "MinMax Rating Range",
    "description": "A rating range defined by minimum and maximum values.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Review",
    "description": "A formal assessment or examination of something.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Account Ownership",
    "description": "The state of owning an account.",
    "inferred_stereotype": "relator" 
  },
  {
    "name": "Write Authorization",
    "description": "Permission to write or modify data.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Update Idea",
    "description": "The action of updating an idea. Use 'Update' as a relator connected to Idea.",
    "inferred_stereotype": "" 
  },
  {
    "name": "User in a Group",
    "description": "Redundant; 'memberOf' relator indicates this relationship.",
    "inferred_stereotype": ""
  },
  {
    "name": "Idea Contest",
    "description": "A contest where people submit ideas.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Read Authorization",
    "description": "Permission to read data.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Review Rating",
    "description": "A rating associated with a review.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Rating Range",
    "description": "The range of possible values for a rating.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Draft",
    "description": "A preliminary version of a piece of writing.",
    "inferred_stereotype": "phase" 
  },
  {
    "name": "Up Down Rating Range",
    "description": "Unclear, likely a rating range with up/down voting mechanics.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Reviewer",
    "description": "A person who conducts a review.",
    "inferred_stereotype": "role"
  }
]
``` 
