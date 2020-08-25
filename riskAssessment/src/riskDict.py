# Function used to treat and build the input dictionary properly.
def treatInput(inputDict):
    ownershipStatus = {
        "ownership_status": inputDict['ownership_status']
    }

    year = {
        "year": 0
    }
    if (inputDict['vehicle'] != 'no'):
        year = {
            "year": int(inputDict['year'])
        }

    treatedDict = {
        "age": int(inputDict['age']),
        "dependents": 0 if inputDict['dependents'] == '' else int(inputDict['dependents']),
        "house": 0 if inputDict['house'] == 'no' else ownershipStatus,
        "income": 0 if inputDict['income'] == '' else int(inputDict['income']),
        "marital_status": inputDict['marital_status'],
        "risk_questions": [int(inputDict['risk-question1']), int(inputDict['risk-question2']), int(inputDict['risk-question3'])],
        "vehicle": 0 if inputDict['vehicle'] == 'no' else year
    }

    return treatedDict