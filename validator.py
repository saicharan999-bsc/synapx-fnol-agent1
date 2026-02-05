def validate_fields(extracted_fields: dict) -> list:
    """
    Check for missing mandatory fields.
    Returns a list of missing field names.
    """

    mandatory_fields = [
        "claimType",
        "attachments",
        "initialEstimate"
    ]

    missing_fields = []

    for field in mandatory_fields:
        value = extracted_fields.get(field)
        if value is None or value == "":
            missing_fields.append(field)

    return missing_fields
