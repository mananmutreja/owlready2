import json
from owlready2 import *
from ontology_handling import University, Course, Professor, offersCourse, hasProfessor

# Populate ontology from JSON file
def populate_ontology_from_json(ontology, json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    with ontology:
        for entry in data['universities']:
            university = University(entry['name'].replace(" ", "_"))
            for course in entry['courses']:
                course_obj = Course(course['name'].replace(" ", "_"))
                offersCourse[university].append(course_obj)
                for professor in course['professors']:
                    professor_obj = Professor(professor['name'].replace(" ", "_"))
                    hasProfessor[course_obj].append(professor_obj)

    return ontology
