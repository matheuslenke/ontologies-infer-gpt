import os
from owlready2 import *
import pandas as pd
from typing import Dict, List
from rdflib import Graph, Literal, RDF, URIRef

cols = ["upperBound", "cardinalityValue", "type", "lowerBound", "aggregationKind", "propertyType",
        "cardinality", "isDerived", "isOrdered", "isReadOnly", "generalization", "isComplete",
        "name", "isDisjoint", "order", "isAbstract", "isPowertype", "restrictedTo", "stereotype",
        "isExtensional", "targetEnd", "description", "sourceEnd", "relationEnd", "general", "attribute",
        "specific"]


def load_ontologies():
    curr_path = os.getcwd()
    parent_path = os.path.abspath(os.path.join(curr_path, os.pardir))
    data_path = os.path.join(parent_path, "docs")
    data_onto_path = os.path.join(data_path, "ontologies")
    data_csv_path = os.path.join(data_path, "csv_data")

    for filename in os.listdir(data_onto_path):
        f = os.path.join(data_onto_path, filename)
        g = Graph()
        g.parse(f)

        df = pd.DataFrame(columns=cols)
        row = {}
        for s, p, o in g:
            if "#" in s:
                s_id = s.split("#")[1]
                p_value = p.split("#")[1]
                value = o
                if s_id in row.keys():
                    d = row[s_id]
                    d[p_value] = o
                    row[s_id] = d
                else:
                    row[s_id] = {}
                    d = {p_value: o}
                    row[s_id] = d

        for d in row.keys():
            df.loc[len(df)] = row[d]
        filename = filename.split(".")[0]
        df.to_csv(os.path.join(data_csv_path, filename+"2501.csv"))
