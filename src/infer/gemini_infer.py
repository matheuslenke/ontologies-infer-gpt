import os
from rdflib import RDF, Graph, URIRef
import glob

import rdflib
from src.client.gemini_client import GeminiClient
from src.utils.save_to_file import save_to_file
from src.infer.openai_infer import get_all_classes, get_classes_names, parse_classes_and_types

class ClassElement:
    def __init__(self, name: rdflib.term.Literal, kind: rdflib.term.URIRef):
        self.name = name
        self.kind = kind

def read_owl_ontology(file_path):
    g = Graph()
    try:
        g.parse(file_path, format="turtle")
        return g
    except Exception as e:
        print(f"Error reading OWL ontology: {e}")
        return None


def read_all_ontologies() -> list[Graph]:
    all_graphs = []
    ttl_files = glob.glob("docs/ontologies/*.ttl")
    for file_path in ttl_files:
        g = read_owl_ontology(file_path)
        if g is not None:
            all_graphs.append(g)
    return all_graphs

def get_all_classes(graph: list[Graph]) -> list[URIRef]:
    classes = []
    for s, p, o in graph.triples((None, None, None)):
        if p == RDF.type and o == URIRef("https://w3id.org/ontouml#Class"):
            classes.append(s)
    return classes

def get_classes_names(graph: list[Graph]) -> dict[URIRef, str]:
    classes_names = {}
    for class_uri in get_all_classes(graph):
        name_triples = graph.triples((class_uri, URIRef("https://w3id.org/ontouml#name"), None))
        for _, _, name in name_triples:
            classes_names[class_uri] = name
    return classes_names

def process_graph(client: GeminiClient, prompt, results_file, graph: Graph):
    responses = client.get_completion(prompt)
    for response in responses:
        save_to_file(results_file, response.text)
        print(response.text)

def save_to_csv(index: int, graph: Graph, classes: list[ClassElement]):
    csv_file = "classes.csv"
    with open(csv_file, "a") as f:
        for class_element in classes:
            f.write(f"{index};{class_element.name};{class_element.kind}\n")
    print(f"Classes saved to {csv_file}")

def infer_stereotypes_gemini():
    '''
    This function is responsible for inferring stereotypes using the Gemini API.
    It will read each .ttl file, make a graph, and then extract only the name of each
    ontouml:Class in the graph. Then, it will use the Gemini API to infer the stereotypes
    based on the name and the context of this ontology.
    '''
    all_graphs = read_all_ontologies()
    gemini_client = GeminiClient()
    max_retry = 3

    index = 0
    for graph in all_graphs:
        classes = get_classes_names(graph)
        names =  classes.values()

        prompt = "###"
        for name in names:
            prompt += name + "\n"
        prompt += "###"

        results_file = os.path.join("out", "results-gemini", f"results{index}.md")
        index += 1
        try:
            process_graph(gemini_client, prompt, results_file, graph)
        except:
            print(f"Error processing ontology {index}")
            save_to_file(results_file, f"Error processing ontology {index}")
            continue