Prompt items: 
SampleSequence, ToConductCEI, RVContraction, STSegment, PWave, Lungs, Non-ElementaryForm, LAContraction, ConductingSystemOfAtria, CSVMyocytesPolarized, PurkinjeElectircalImpulse, TWave, CSAMyocytes, SAElecticalImpulse, RVBloodStoring, AVElectricalImpulse, ToRestoreEPs, CSAAsCEIConductor, RightAtriumAsBloodContainer, SANodeAsCEIConductor, Normal, ECMOfSANode, QWave, HisPurkinjeElectricalImpulse, LeftAtrium, NonPacemakerCells, RightVentricleAsBloodContainer, Wave, LeftAtriumAsBloodContainer, BodySurface, DateDomain, SANodeMyocytesDepolarized, Physician, BloodinRightAtrium, ElementaryForm, LVBloodStoring, WaveForm, Period(ms), Geometric Form, Person, Segment, CSVAsEPsAccumulator, PeripheralsBloodStoring, p.d.(mV), LeftVentricle, CSVAsCEIConductor, RightVentricleAsPump, LeftAtriumAsPump, Lead, Patient, ECMOfCSV, QRSComplex, BodySurfaceRegionAsObjectOfMeasure, ECGForm, CSVMyocytes, SANodeCells, TimeDomain, SANode, p.d.Seq({mV}), HeartAsBloodContainer, BodySurfaceRegion, RightAtriumAsPump, ECGRecord, BloodInPeripherals, RABloodStoring, Treatment, TPSegment, RightAtrium, CorrelatedObservationSeries, sampleRate(Hz), HeartCells, LeftVentricleAsPump, Sample, RightVentricle, PacemakerCells, CSVMyocytesDepolarized, EPsAccumulator, HumanBody, DepolarizationOfCSAMyocytes, ObservationSeries, SANodeMyocytes, BloodInLungs, ConductingSystemOfVentricles, AVNodeCells, Observation, Cycle, FilteringTecnique, RepolarizationOfCSVMyocytes, BandpassFilter, CSAMyocytesDepolarized, Chamber, LeftVentricleAsBloodContainer, BloodinRightVentricle, BloodInLeftVentricle, Electrode, HisElectricalImpulse, CardiacElectricalImpulse, PRSegment, ElectrodeAsAMeasurer, LVContraction, TransitionalSANodeMyocytes, SANodeAsCEIGenerator, SWave, HumanHeart, BloodInLeftAtrium, LowpassFilter, Muscle, Annotation, CSAMyocytesPolarized, Placement, Peripherals, HeartAsPump, RAContraction, ECGRecordingDevice, EPR, PacemakerSANodeMyocytes, SANodeMyocytesPolarized, RWave, BloodInHumanBody, LungAsBloodContainer, ECGRecordingSession, DepolarizationOfCSVMyocytes, LungBloodStoring, Baseline, ECMOfCSA, CEIGenerator, ElectricalPotential(mV), LABloodStoring, Abnormal, CEIConductor, PeripheralsAsBloodContainer, ToGenerateCEI, DepolarizationOfPacemakerSANodeMyocytes, 
amout of items: 133
 I have read the provided user query and will perform the following actions:
1 - I understand each element as a concept or object within a biological context related to the human heart (Electrode, SANodeMyocytes, LeftVentricle, etc.)
2 - Without asking any questions, I will infer possible OntoUML stereotypes for each element with a missing stereotype based on their properties and roles.
3 - The stereotypes I infer are:
   - Electrode: Device or situation
   - SANodeMyocytes: Cell
   - LeftVentricle: Situation or event (it accumulates temporal parts)
4 - Output a csv with the following columns: name (the name of the element), inferred_stereotype (the stereotype that I inferred).

Sample output in CSV format:
name, inferred_stereotype
Electrode, Device or situation
SANodeMyocytes, Cell
LeftVentricle, Situation or event
