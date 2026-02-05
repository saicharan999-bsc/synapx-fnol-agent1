import pdfplumber
import os
import re


def extract_text(file_path: str) -> str:
    """
    Extract raw text from PDF or TXT file
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    if file_path.lower().endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    raise ValueError("Unsupported file format. Only PDF and TXT allowed.")


def extract_fields(text: str) -> dict:
    fields = {
        "policyNumber": None,
        "policyholderName": None,
        "effectiveDates": None,
        "incidentDate": None,
        "incidentTime": None,
        "location": None,
        "description": None,
        "assetType": None,
        "assetId": None,
        "estimatedDamage": None,
        "claimType": None,
        "attachments": None,
        "initialEstimate": None
    }

    # POLICY NUMBER
    match = re.search(r"POLICY NUMBER[:\s]*([A-Z0-9\-]+)", text, re.IGNORECASE)
    if match:
        fields["policyNumber"] = match.group(1)

    # POLICYHOLDER NAME
    match = re.search(r"POLICYHOLDER NAME[:\s]*(.+)", text, re.IGNORECASE)
    if match:
        fields["policyholderName"] = match.group(1).strip()

    # POLICY EFFECTIVE DATES
    match = re.search(r"POLICY EFFECTIVE DATES[:\s]*(.+)", text, re.IGNORECASE)
    if match:
        fields["effectiveDates"] = match.group(1).strip()

    # INCIDENT DATE
    match = re.search(r"DATE OF LOSS[:\s]*([0-9/]+)", text, re.IGNORECASE)
    if match:
        fields["incidentDate"] = match.group(1)

    # INCIDENT TIME
    match = re.search(r"TIME OF LOSS[:\s]*([0-9:]+)", text, re.IGNORECASE)
    if match:
        fields["incidentTime"] = match.group(1)

    # LOCATION
    match = re.search(r"LOCATION OF LOSS[:\s]*(.+)", text, re.IGNORECASE)
    if match:
        fields["location"] = match.group(1).strip()

    # DESCRIPTION (ROBUST — DOES NOT DEPEND ON ASSET TYPE)
    match = re.search(
        r"DESCRIPTION OF ACCIDENT[:\s]*([\s\S]*?)(ESTIMATE AMOUNT|CLAIM TYPE|ATTACHMENTS|INITIAL ESTIMATE|$)",
        text,
        re.IGNORECASE
    )
    if match:
        fields["description"] = match.group(1).strip()

    # ESTIMATED DAMAGE
    match = re.search(r"ESTIMATE AMOUNT[:\s₹$]*([0-9,]+)", text, re.IGNORECASE)
    if match:
        fields["estimatedDamage"] = int(match.group(1).replace(",", ""))

    # CLAIM TYPE
    match = re.search(r"CLAIM TYPE[:\s]*(.+)", text, re.IGNORECASE)
    if match:
        fields["claimType"] = match.group(1).strip()

    # ATTACHMENTS
    match = re.search(r"ATTACHMENTS[:\s]*(.+)", text, re.IGNORECASE)
    if match:
        fields["attachments"] = match.group(1).strip()

    # INITIAL ESTIMATE
    match = re.search(r"INITIAL ESTIMATE[:\s₹$]*([0-9,]+)", text, re.IGNORECASE)
    if match:
        fields["initialEstimate"] = int(match.group(1).replace(",", ""))

    return fields


def extract_from_file(file_path: str) -> dict:
    text = extract_text(file_path)
    return extract_fields(text)
