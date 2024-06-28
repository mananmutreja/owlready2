from owlready2 import *

# Function to check consistency of ontology
def check_consistency(ontology):
    return not ontology.is_inconsistent()
