from ontology_handling import load_ontology, create_classes_properties
from data_handling import populate_ontology_from_json
from reasoning_handling import apply_reasoning, check_consistency

def main():
    ontology_path = "university.owl"
    json_path = "data.json"

    # Load ontology
    ontology = load_ontology(ontology_path)

    # Create classes and properties
    ontology = create_classes_properties(ontology)

    # Populate ontology from JSON data
    ontology = populate_ontology_from_json(ontology, json_path)

    # Apply reasoning using Pellet
    ontology = apply_reasoning(ontology)

    # Check consistency
    is_consistent = check_consistency(ontology)
    print("Ontology is consistent:", is_consistent)

    # Save the populated ontology
    ontology.save(file="populated_university.owl")
    print("Ontology populated and saved successfully.")

if __name__ == "__main__":
    main()
