import os

import rdflib
from src.client.llm_client import OpenAIClient
from src.client.openai_client import make_completion
from rdflib import RDF, Graph, URIRef
import glob
from src.utils.save_to_file import save_to_file

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

def parse_classes_and_types(graph: list[Graph]) -> list[ClassElement]:
    classes: list[ClassElement] = []
    for class_uri in get_all_classes(graph):
        name: rdflib.term.Literal = None
        stereotype: rdflib.term.URIRef = None
        
        name_triples = graph.triples((class_uri, URIRef("https://w3id.org/ontouml#name"), None))
        for _, _, nameElement in name_triples:
            name = nameElement
        stereotype_triples = graph.triples((class_uri, URIRef("https://w3id.org/ontouml#stereotype"), None))
        for _, _, stereotypeElement in stereotype_triples:
            stereotype = stereotypeElement
        if name and stereotype:
            classes.append(ClassElement(name, stereotype))
    return classes


def save_to_csv(index: int, graph: Graph, classes: list[ClassElement]):
    csv_file = "classes.csv"
    with open(csv_file, "a") as f:
        for class_element in classes:
            f.write(f"{index};{class_element.name};{class_element.kind}\n")
    print(f"Classes saved to {csv_file}")

def process_graph(client: OpenAIClient, prompt, results_file, graph: Graph):
    responses = client.get_completion(prompt)
    with open(results_file, "a") as result_file:
        for chunk in responses:
            if chunk.choices[0].delta.content:
                result_file.write(chunk.choices[0].delta.content)
                print(chunk.choices[0].delta.content, end="", flush=True)
        result_file.write("\n")

def infer_stereotype_openai(model: str):
    all_graphs = read_all_ontologies()
    client = OpenAIClient(model=model)
    index = 0
    csv_file = "classes.csv"
    with open(csv_file, "w") as f:
        f.write("Graph Number;Class Name;Class Stereotype\n")
    for graph in all_graphs:
        classes = get_classes_names(graph)
        names =  classes.values()
        classElements = parse_classes_and_types(graph)
        save_to_csv(index, graph, classElements)
        index = index + 1

        # prompt = ""
        # for name in names:
        #     prompt += name + ", "

        # folder = os.path.join("out", f"results-{model}")
        # results_file = os.path.join(folder, f"results{index}.md")

        # with open(results_file, "w") as f:
        #     f.write("Prompt items: \n")
        #     f.write(prompt + "\n")
        #     f.write("amout of items: " + str(len(names)) + "\n")

        # try:
        #     process_graph(client, prompt, results_file, graph)
        # except:
        #     print(f"Error processing ontology {index}")
        #     save_to_file(results_file, f"Error processing ontology {index}")
        #     continue
        # finally:
        #     index += 1

