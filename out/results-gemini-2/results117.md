1 - Read the name of every element: Educational Organization, Educational History, Language, Course, Faculty, Admission Period, In Presence, Bachelor Graduate, Employment History, University, Local Languages, Hybrid, Student Club, Co-Op Program, City, Vocational school, Study Program, Institute, Full Time, Country, Masters Graduate, Machine Learning, Unemployed, Part Time, Online, Hobbies, Academic Instructor, Language Requirement, Application, High School Graduate, College, Employed, Degree Requirement, Applicant.
2 - Infer ONE possible OntoUML stereotype for each element:
     - Educational Organization: **kind**
     - Educational History: **phaseMixin**
     - Language: **kind**
     - Course: **kind**
     - Faculty: **kind**
     - Admission Period: **role**
     - In Presence: **roleMixin**
     - Bachelor Graduate: **role**
     - Employment History: **phaseMixin**
     - University: **subkind**
     - Local Languages: **role**
     - Hybrid: **roleMixin**
     - Student Club: **collective** 
     - Co-Op Program: **kind**
     - City: **kind**
     - Vocational school: **subkind**
     - Study Program: **kind**
     - Institute: **subkind**
     - Full Time: **roleMixin**
     - Country: **kind**
     - Masters Graduate: **role**
     - Machine Learning: **subkind**
     - Unemployed: **roleMixin**
     - Part Time: **roleMixin**
     - Online: **roleMixin**
     - Hobbies: **mode**
     - Academic Instructor: **role**
     - Language Requirement: **kind**
     - Application: **kind**
     - High School Graduate: **role**
     - College: **subkind**
     - Employed: **roleMixin**
     - Degree Requirement: **kind**
     - Applicant: **role**
3 - Provide the explanation for each stereotype inferred:
    - Educational Organization: It represents a fundamental type of institution that provides education.
    - Educational History: Represents phases in an individual's educational journey, contingent on their experiences.
    - Language: Represents a distinct system of communication.
    - Course: Represents a structured unit of teaching within an educational program.
    - Faculty: Represents a group of educators within an institution.
    - Admission Period: Represents the time when an applicant can apply to an institution.
    - In Presence: Represents a way of attending courses that require physical presence.
    - Bachelor Graduate: Represents a person that has concluded a bachelor's degree.
    - Employment History: Represents the history of jobs, contingent on time and experiences.
    - University: A specific type of educational organization.
    - Local Languages: Represents the languages spoken in a specific location.
    - Hybrid: Represents a mix of methods, in this case, study methods.
    - Student Club: Represents a group of students.
    - Co-Op Program: Represents a structured program that combines work and studies.
    - City: Represents an urban area.
    - Vocational School: Represents a specific type of educational organization.
    - Study Program: Represents a structured sequence of courses.
    - Institute: Represents a specific type of educational organization.
    - Full Time: Represents a dedication of time, in this case, to studies or work.
    - Country: Represents a nation or state.
    - Masters Graduate: Represents a person that has concluded a master's degree.
    - Machine Learning: Represents a specific field of study.
    - Unemployed: Represents a phase in a person's work life.
    - Part Time: Represents a dedication of time, in this case, to studies or work.
    - Online: Represents something on the internet, in this case, a study method.
    - Hobbies: Represents things that a person likes to do.
    - Academic Instructor: Represents a role within the educational field.
    - Language Requirement: Represents a specific requirement, in this case, for language proficiency.
    - Application: Represents a formal request to an institution.
    - High School Graduate: Represents a person that has concluded high school.
    - College: Represents a specific type of educational organization.
    - Employed: Represents the state of having a job.
    - Degree Requirement: Represents a specific requirement for a degree.
    - Applicant: Represents a person that applies to something, in this case, an institution.
4 - Output a json array:
```json
[
    {
        "name": "Educational Organization",
        "inferred_stereotype": "kind",
        "explanation": "It represents a fundamental type of institution that provides education."
    },
    {
        "name": "Educational History",
        "inferred_stereotype": "phaseMixin",
        "explanation": "Represents phases in an individual's educational journey, contingent on their experiences."
    },
    {
        "name": "Language",
        "inferred_stereotype": "kind",
        "explanation": "Represents a distinct system of communication."
    },
    {
        "name": "Course",
        "inferred_stereotype": "kind",
        "explanation": "Represents a structured unit of teaching within an educational program."
    },
    {
        "name": "Faculty",
        "inferred_stereotype": "kind",
        "explanation": "Represents a group of educators within an institution."
    },
    {
        "name": "Admission Period",
        "inferred_stereotype": "role",
        "explanation": "Represents the time when an applicant can apply to an institution."
    },
    {
        "name": "In Presence",
        "inferred_stereotype": "roleMixin",
        "explanation": "Represents a way of attending courses that require physical presence."
    },
    {
        "name": "Bachelor Graduate",
        "inferred_stereotype": "role",
        "explanation": "Represents a person that has concluded a bachelor's agree."
    },
    {
        "name": "Employment History",
        "inferred_stereotype": "phaseMixin",
        "explanation": "Represents the history of jobs, contingent on time and experiences."
    },
    {
        "name": "University",
        "inferred_stereotype": "subkind",
        "explanation": "A specific type of educational organization."
    },
    {
        "name": "Local Languages",
        "inferred_stereotype": "role",
        "explanation": "Represents the languages spoken in a specific location."
    },
    {
        "name": "Hybrid",
        "inferred_stereotype": "roleMixin",
        "explanation": "Represents a mix of methods, in this case, study methods."
    },
    {
        "name": "Student Club",
        "inferred_stereotype": "collective",
        "explanation": "Represents a group of students."
    },
    {
        "name": "Co-Op Program",
        "inferred_stereotype": "kind",
        "explanation": "Represents a structured program that combines work and studies."
    },
    {
        "name": "City",
        "inferred_stereotype": "kind",
        "explanation": "Represents an urban area."
    },
    {
        "name": "Vocational school",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a specific type of educational organization."
    },
    {
        "name": "Study Program",
        "inferred_stereotype": "kind",
        "explanation": "Represents a structured sequence of courses."
    },
    {
        "name": "Institute",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a specific type of educational organization."
    },
    {
        "name": "Full Time",
        "inferred_stereotype": "roleMixin",
        "explanation": "Represents a dedication of time, in this case, to studies or work."
    },
    {
        "name": "Country",
        "inferred_stereotype": "kind",
        "explanation": "Represents a nation or state."
    },
    {
        "name": "Masters Graduate",
        "inferred_stereotype": "role",
        "explanation": "Represents a person that has concluded a master's degree."
    },
    {
        "name": "Machine Learning",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a specific field of study."
    },
    {
        "name": "Unemployed",
        "inferred_stereotype": "roleMixin",
        "explanation": "Represents a phase in a person's work life."
    },
    {
        "name": "Part Time",
        "inferred_stereotype": "roleMixin",
        "explanation": "Represents a dedication of time, in this case, to studies or work."
    },
    {
        "name": "Online",
        "inferred_stereotype": "roleMixin",
        "explanation": "Represents something on the internet, in this case, a study method."
    },
    {
        "name": "Hobbies",
        "inferred_stereotype": "mode",
        "explanation": "Represents things that a person likes to do."
    },
    {
        "name": "Academic Instructor",
        "inferred_stereotype": "role",
        "explanation": "Represents a role within the educational field."
    },
    {
        "name": "Language Requirement",
        "inferred_stereotype": "kind",
        "explanation": "Represents a specific requirement, in this case, for language proficiency."
    },
    {
        "name": "Application",
        "inferred_stereotype": "kind",
        "explanation": "Represents a formal request to an institution."
    },
    {
        "name": "High School Graduate",
        "inferred_stereotype": "role",
        "explanation": "Represents a person that has concluded high school."
    },
    {
        "name": "College",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a specific type of educational organization."
    },
    {
        "name": "Employed",
        "inferred_stereotype": "roleMixin",
        "explanation": "Represents the state of having a job."
    },
    {
        "name": "Degree Requirement",
        "inferred_stereotype": "kind",
        "explanation": "Represents a specific requirement for a degree."
    },
    {
        "name": "Applicant",
        "inferred_stereotype": "role",
        "explanation": "Represents a person that applies to something, in this case, an institution."
    }
]
```