from extractor import extract_from_file
from validator import validate_fields
from router import route_claim
import json
import sys

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "input_docs/fnol_sample_1.txt"

    extracted = extract_from_file(file_path)
    missing = validate_fields(extracted)
    route, reasoning = route_claim(extracted, missing)

    output = {
        "extractedFields": extracted,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reasoning
    }

    print(json.dumps(output, indent=2))
