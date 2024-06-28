from owlready2 import *

# Load ontology
def load_ontology(path):
    return get_ontology(path).load()

# Create classes and properties
def create_classes_properties(ontology):
    global University, Course, Professor, offersCourse, hasProfessor

    with ontology:
        class University(Thing):
            pass

        class Course(Thing):
            pass

        class Professor(Thing):
            pass

        class offersCourse(ObjectProperty):
            domain = [University]
            range = [Course]

        class hasProfessor(ObjectProperty):
            domain = [Course]
            range = [Professor]

    return ontology
