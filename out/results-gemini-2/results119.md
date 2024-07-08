1 - Read the name of every element:
Pessoa Viva, Pessoa Doente, Funcional, Órgão, Captador, Não Funcional, Item Transplantado, Tecido, Coração, Receptor, Homem, Pessoa, Pessoa com ME, Pessoa com PCR, Captação, Sistema Orgânico, Item Captado, Mulher, Transplante, Transplantador, Doador, Sistema Circulatório, Pessoa Saudável, Córnea, Pessoa Morta

2 - Infer ONE possible OntoUML stereotype for each element with a missing stereotype
Pessoa Viva: **phase**
Pessoa Doente: **phase**
Funcional: **phaseMixin**
Órgão: **kind**
Captador: **role**
Não Funcional: **phaseMixin**
Item Transplantado: **subkind**
Tecido: **kind**
Coração: **subkind**
Receptor: **role**
Homem: **subkind**
Pessoa: **kind**
Pessoa com ME: **role**
Pessoa com PCR: **role**
Captação: **event**
Sistema Orgânico: **kind**
Item Captado: **subkind**
Mulher: **subkind**
Transplante: **event**
Transplantador: **roleMixin**
Doador: **role**
Sistema Circulatório: **subkind**
Pessoa Saudável: **phase**
Córnea: **subkind**
Pessoa Morta: **phase**

3 - Provide the explanation for each stereotype inferred:
Pessoa Viva: Represents a phase in the life of a Pessoa, when it is alive.
Pessoa Doente: Represents a phase in the life of a Pessoa, when it is sick.
Funcional: Represents a contingent property that can be applied to instances of different kinds, like Órgão, describing its functionality.
Órgão: Represents a fundamental sort of endurant type, in this case, a type of organ.
Captador: Represents an anti-rigid specialization of a kind, in this case, a person that harvests organs.
Não Funcional: Represents a contingent property that can be applied to instances of different kinds, like Órgão, describing its non-functionality.
Item Transplantado: Represents a rigid specialization of the kind Item, in this case, an item that was transplanted.
Tecido: Represents a fundamental sort of endurant type, in this case, a type of tissue.
Coração: Represents a rigid specialization of the kind Órgão, in this case, a heart.
Receptor: Represents an anti-rigid specialization of a kind, in this case, a person that receives an organ.
Homem: Represents a rigid specialization of the kind Pessoa, in this case, a man.
Pessoa: Represents a fundamental sort of endurant type, in this case, a person.
Pessoa com ME: Represents an anti-rigid specialization of the kind Pessoa, in this case, a person with a medical condition that makes them eligible for organ donation after death.
Pessoa com PCR:  Represents an anti-rigid specialization of the kind Pessoa, in this case, a person with cardiorespiratory arrest.
Captação: Represents a perdurant type, in this case, the event of harvesting an organ.
Sistema Orgânico: Represents a fundamental sort of endurant type, in this case, a system of organs.
Item Captado: Represents a rigid specialization of the kind Item, in this case, an item that was harvested.
Mulher: Represents a rigid specialization of the kind Pessoa, in this case, a woman.
Transplante: Represents a perdurant type, in this case, the event of transplanting an organ.
Transplantador: Represents properties that are essential to some of their instances, but accidental to some other instances, in this case, the quality of being a transplant surgeon.
Doador: Represents an anti-rigid specialization of a kind, in this case, a person that donates an organ.
Sistema Circulatório: Represents a rigid specialization of the kind Sistema Orgânico, in this case, the circulatory system.
Pessoa Saudável: Represents a phase in the life of a Pessoa, when it is healthy.
Córnea: Represents a rigid specialization of the kind Órgão, in this case, a cornea.
Pessoa Morta: Represents a phase in the life of a Pessoa, when it is dead.


4 - Output a json array, where each object contains the following keys: name, inferred_stereotype, explanation. Please, do not truncate the array and always provide every element in the response.
```json
[
    {
        "name": "Pessoa Viva",
        "inferred_stereotype": "phase",
        "explanation": "Represents a phase in the life of a Pessoa, when it is alive."
    },
    {
        "name": "Pessoa Doente",
        "inferred_stereotype": "phase",
        "explanation": "Represents a phase in the life of a Pessoa, when it is sick."
    },
    {
        "name": "Funcional",
        "inferred_stereotype": "phaseMixin",
        "explanation": "Represents a contingent property that can be applied to instances of different kinds, like Órgão, describing its functionality."
    },
    {
        "name": "Órgão",
        "inferred_stereotype": "kind",
        "explanation": "Represents a fundamental sort of endurant type, in this case, a type of organ."
    },
    {
        "name": "Captador",
        "inferred_stereotype": "role",
        "explanation": "Represents an anti-rigid specialization of a kind, in this case, a person that harvests organs."
    },
    {
        "name": "Não Funcional",
        "inferred_stereotype": "phaseMixin",
        "explanation": "Represents a contingent property that can be applied to instances of different kinds, like Órgão, describing its non-functionality."
    },
    {
        "name": "Item Transplantado",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a rigid specialization of the kind Item, in this case, an item that was transplanted."
    },
    {
        "name": "Tecido",
        "inferred_stereotype": "kind",
        "explanation": "Represents a fundamental sort of endurant type, in this case, a type of tissue."
    },
    {
        "name": "Coração",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a rigid specialization of the kind Órgão, in this case, a heart."
    },
    {
        "name": "Receptor",
        "inferred_stereotype": "role",
        "explanation": "Represents an anti-rigid specialization of a kind, in this case, a person that receives an organ."
    },
    {
        "name": "Homem",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a rigid specialization of the kind Pessoa, in this case, a man."
    },
    {
        "name": "Pessoa",
        "inferred_stereotype": "kind",
        "explanation": "Represents a fundamental sort of endurant type, in this case, a person."
    },
    {
        "name": "Pessoa com ME",
        "inferred_stereotype": "role",
        "explanation": "Represents an anti-rigid specialization of the kind Pessoa, in this case, a person with a medical condition that makes them eligible for organ donation after death."
    },
    {
        "name": "Pessoa com PCR",
        "inferred_stereotype": "role",
        "explanation": "Represents an anti-rigid specialization of the kind Pessoa, in this case, a person with cardiorespiratory arrest."
    },
    {
        "name": "Captação",
        "inferred_stereotype": "event",
        "explanation": "Represents a perdurant type, in this case, the event of harvesting an organ."
    },
    {
        "name": "Sistema Orgânico",
        "inferred_stereotype": "kind",
        "explanation": "Represents a fundamental sort of endurant type, in this case, a system of organs."
    },
    {
        "name": "Item Captado",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a rigid specialization of the kind Item, in this case, an item that was harvested."
    },
    {
        "name": "Mulher",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a rigid specialization of the kind Pessoa, in this case, a woman."
    },
    {
        "name": "Transplante",
        "inferred_stereotype": "event",
        "explanation": "Represents a perdurant type, in this case, the event of transplanting an organ."
    },
    {
        "name": "Transplantador",
        "inferred_stereotype": "roleMixin",
        "explanation": "Represents properties that are essential to some of their instances, but accidental to some other instances, in this case, the quality of being a transplant surgeon."
    },
    {
        "name": "Doador",
        "inferred_stereotype": "role",
        "explanation": "Represents an anti-rigid specialization of a kind, in this case, a person that donates an organ."
    },
    {
        "name": "Sistema Circulatório",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a rigid specialization of the kind Sistema Orgânico, in this case, the circulatory system."
    },
    {
        "name": "Pessoa Saudável",
        "inferred_stereotype": "phase",
        "explanation": "Represents a phase in the life of a Pessoa, when it is healthy."
    },
    {
        "name": "Córnea",
        "inferred_stereotype": "subkind",
        "explanation": "Represents a rigid specialization of the kind Órgão, in this case, a cornea."
    },
    {
        "name": "Pessoa Morta",
        "inferred_stereotype": "phase",
        "explanation": "Represents a phase in the life of a Pessoa, when it is dead."
    }
]
```