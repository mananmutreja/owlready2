from owlready2 import *

# Function to load SWRL rules
def load_swrl_rules(ontology, swrl_path):
    with open(swrl_path, 'r') as f:
        rules = f.read()

    try:
        with ontology:
            sync_reasoner_pellet(infer_property_values=True, debug=9)
            return rules
    except Exception as e:
        print(f"Error applying SWRL rules: {e}")

# Function to apply reasoning using Pellet reasoner
def apply_reasoning(ontology):
    with ontology:
        sync_reasoner_pellet(infer_property_values=True, debug=9)
    return ontology

# Function to generate new facts and incorporate them into the reasoned ontology
def generate_new_facts(ontology):
    with ontology:
        # Generate new facts based on reasoning results
        # Example: Creating new courses based on inferred relationships
        new_course = Course("New Course")
        university = University("Example University")
        university.offersCourse.append(new_course)
    return ontology
