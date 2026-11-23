"""Simple symptom checker.

Matches the symptoms a user types in against a small disease database and
shows a match percentage for each disease. This is a learning project, not
a medical tool.
"""

DISEASES = {
    "Malaria": "fever,headache,chills,sweating,body aches",
    "Influenza": "fever,cough,headache,body aches,fatigue",
    "Common Cold": "cough,runny nose,sneezing,sore throat",
    "Typhoid Fever": "fever,headache,stomach pain,weakness,diarrhea",
    "Migraine": "headache,nausea,sensitivity to light",
    "Gastroenteritis": "diarrhea,vomiting,stomach pain,nausea",
}


DISEASE_SYMPTOMS = {
    name: {s.strip().lower() for s in symptoms.split(",")}
    for name, symptoms in DISEASES.items()
}


def get_user_symptoms():
    raw = input("Enter your symptoms, separated by commas: ")
    return {s.strip().lower() for s in raw.split(",") if s.strip()}


def score_diseases(user_symptoms):
    """Return a list of (disease, percent, matched_symptoms), best match first.

    Percentage = share of the disease's known symptoms that the user reported.
    """
    results = []
    for disease, known in DISEASE_SYMPTOMS.items():
        matched = user_symptoms & known
        if matched:
            percent = len(matched) / len(known) * 100
            results.append((disease, percent, matched))
    results.sort(key=lambda r: r[1], reverse=True)
    return results


def main():
    print("Diseases in database:", ", ".join(DISEASES))
    user_symptoms = get_user_symptoms()

    if not user_symptoms:
        print("No symptoms entered.")
        return

    print("\nYou entered:", ", ".join(sorted(user_symptoms)).upper())

    results = score_diseases(user_symptoms)
    if not results:
        print("\nNo matching diseases found in the database.")
        return

    print("\nPossible matches:")
    for disease, percent, matched in results:
        print(f"  {disease}: {percent:.0f}%  (matched: {', '.join(sorted(matched))})")

    unknown = user_symptoms - set().union(*DISEASE_SYMPTOMS.values())
    if unknown:
        print("\nNot recognised:", ", ".join(sorted(unknown)))

    print("\nNote: this is only a rough guide, not a diagnosis. "
          "Please see a doctor or health worker for proper testing and advice.")


if __name__ == "__main__":
    main()
