def route_claim(extracted_fields: dict, missing_fields: list) -> tuple:
    """
    Decide claim route and reasoning.
    Returns (route, reasoning)
    """

    description = extracted_fields.get("description", "") or ""
    claim_type = extracted_fields.get("claimType", "") or ""
    estimated_damage = extracted_fields.get("estimatedDamage")

    # Rule 1: Missing mandatory fields
    if missing_fields:
        return (
            "Manual Review",
            "One or more mandatory fields are missing."
        )

    # Rule 2: Fraud indicators
    fraud_keywords = ["fraud", "inconsistent", "staged"]
    if any(word in description.lower() for word in fraud_keywords):
        return (
            "Investigation Flag",
            "Description contains potential fraud indicators."
        )

    # Rule 3: Injury claims
    if claim_type.lower() == "injury":
        return (
            "Specialist Queue",
            "Claim type is injury and requires specialist handling."
        )

    # Rule 4: Fast-track eligibility
    if estimated_damage is not None and estimated_damage < 25000:
        return (
            "Fast-track",
            "Estimated damage is below 25,000 and no issues detected."
        )

    # Default
    return (
        "Manual Review",
        "Claim does not meet fast-track criteria."
    )
