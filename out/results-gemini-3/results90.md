```json
[
  {
    "name": "MedicalProcedure",
    "description": "A standardized set of actions performed to diagnose, treat, or prevent medical conditions.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "PreviousIllness",
    "description": "A medical condition that a patient has experienced in the past.",
    "inferred_stereotype": "roleMixin" 
  },
  {
    "name": "string",
    "description": "A sequence of characters representing text. This likely represents a general data type rather than a domain concept, so it lacks a stereotype.",
    "inferred_stereotype": null
  },
  {
    "name": "Person",
    "description": "A human being.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "SymptomEnum",
    "description": "An enumeration of different symptoms. This likely represents a data structure rather than a concept, so it lacks a stereotype.",
    "inferred_stereotype": null 
  },
  {
    "name": "ReportingPatient",
    "description": "A patient who is reporting symptoms or seeking medical attention.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "Date",
    "description": "A specific point in time.  Represents a data type rather than a domain concept.",
    "inferred_stereotype": null 
  },
  {
    "name": "HoursSpecification",
    "description": "A specification of a duration in hours. This likely represents a data structure, so it lacks a stereotype.",
    "inferred_stereotype": null
  },
  {
    "name": "DiagnosticProcedure",
    "description": "A medical procedure performed to identify the cause of a patient's symptoms or illness.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "MedicalProcedureOutcome",
    "description": "The result or effect of a medical procedure.",
    "inferred_stereotype": "situation" 
  },
  {
    "name": "PrescribedDoseSchedule",
    "description": "A schedule for administering doses of medication as prescribed by a doctor.",
    "inferred_stereotype": "roleMixin"
  },
  {
    "name": "SevereSymptom",
    "description": "A symptom that is intense or indicates a serious medical condition.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Diagnosis",
    "description": "The identification of the nature of an illness or other problem by examination of the symptoms.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "PhysicalExam",
    "description": "A hands-on examination of a patient's body to assess their physical health.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "SpecialistMedicalProcedure",
    "description": "A complex medical procedure that requires specialized training and expertise.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Drug",
    "description": "A substance used in the treatment, cure, prevention, or diagnosis of disease or used to otherwise enhance physical or mental well-being.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "Symptom",
    "description": "A physical or mental feature that is regarded as indicating a condition of disease, particularly such a feature that is apparent to the patient.",
    "inferred_stereotype": "kind"
  },
  {
    "name": "Rating",
    "description": "A measure, quantity, or frequency, typically one measured against some other quantity or measure.",
    "inferred_stereotype": "quality" 
  },
  {
    "name": "RemoteMedicalProcedure",
    "description": "A medical procedure performed remotely using technology, such as telemedicine.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "boolean",
    "description": "A data type with two possible values: true or false. Represents a data type rather than a domain concept.",
    "inferred_stereotype": null 
  },
  {
    "name": "User",
    "description": "A person who uses a system or service.  This is very generic; might be more specific in a medical context.",
    "inferred_stereotype": "role"
  },
  {
    "name": "MildSymptom",
    "description": "A symptom that is not severe and may not indicate a serious medical condition.",
    "inferred_stereotype": "subkind" 
  },
  {
    "name": "Address",
    "description": "The particulars of the place where someone lives or an organization is situated. Represents a data structure rather than a domain concept.",
    "inferred_stereotype": null
  },
  {
    "name": "Doctor",
    "description": "A qualified practitioner of medicine; a physician.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "MedicalCondition",
    "description": "An abnormal state of health that interferes with normal bodily functions.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "NonSevereOutcome",
    "description": "An outcome of a medical procedure that is not severe or life-threatening.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "float",
    "description": "A data type representing a number with a decimal point. This represents a data type rather than a domain concept.",
    "inferred_stereotype": null
  },
  {
    "name": "MedicalProcedureTrigger",
    "description": "An event or condition that initiates the need for a medical procedure.",
    "inferred_stereotype": "situation"
  },
  {
    "name": "Prescription",
    "description": "A written direction by a physician for the preparation and administration of a medicine or treatment.",
    "inferred_stereotype": "kind" 
  },
  {
    "name": "TherapeuticProcedure",
    "description": "A medical procedure performed to treat or alleviate a medical condition.",
    "inferred_stereotype": "subkind"
  },
  {
    "name": "Patient",
    "description": "A person receiving or registered to receive medical treatment.",
    "inferred_stereotype": "role" 
  },
  {
    "name": "DiagnosisMethod",
    "description": "A particular procedure for accomplishing or approaching something, especially a systematic or established one.",
    "inferred_stereotype": "kind"
  }
]