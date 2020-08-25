import json, datetime

# Add or subtract a given value from the risk score dictionary.
def sumPoint(riskScore, items, value):
    for item in items:
        riskScore[item] += value

# Set ineligible for a set of insurance.
def setIneligible(result, items):
    for item in items:
        result[item] = 'ineligible'

# Map score to the type of risk: economic, regular and responsible.
def lineRisk(score):
    if (score <= 0):
        return 'economic'
    elif (score >= 3):
        return 'responsible'
    else:
        return 'regular'

# Generate the type of risk for each line of insurance.
def totalRisk(scoreDict):
    result = {}
    for item in scoreDict:
        result[item] = lineRisk(scoreDict[item])

    return result

# Apply rules 3 to 8 on risk score.
def computeScore(userData):
    baseScore = sum(userData["risk_questions"])
    riskScore = {
        "auto": baseScore,
        "disability": baseScore,
        "home": baseScore,
        "life": baseScore
    }
    print(riskScore)
    # Rule 3: Under 40 years old, deduct 1 risk point.
    if (userData["age"] < 40):
        sumPoint(riskScore, riskScore.keys(), -1)

    # Rule 3: Under 30 years old, deduct 2 risk points.
    if (userData["age"] < 30):
        sumPoint(riskScore, riskScore.keys(), -1)

    # Rule 4: Income above 200k, deduct 1 risk point.
    if (userData["income"] > 200000):
        sumPoint(riskScore, riskScore.keys(), -1)

    # Rule 5: If the user has a house and it's mortgaged, add 1 risk point to disability and home scores.
    if (userData['house'] != 0) and (userData["house"]["ownership_status"] == 'mortgaged'):
        sumPoint(riskScore, ["disability", "home"], 1)

    # Rule 6: If the user has dependents, add 1 risk point to disability and life scores.
    if (userData["dependents"] > 0):
        sumPoint(riskScore, ["disability", "life"], 1)

    # Rule 7: If the user is marrid, remove 1 risk point from disability and add 1 risk point to life score.
    if (userData["marital_status"] == "married"):
        sumPoint(riskScore, ["disability"], -1)
        sumPoint(riskScore, ["life"], 1)

    # Rule 8: If the user has a car manufactured in the last 5 years, add 1 risk point to auto score.
    if (userData['vehicle'] != 0):
        currentYear = datetime.datetime.now().year
        if (currentYear - userData["vehicle"]["year"] <= 5):
            sumPoint(riskScore, ["auto"], 1)
    print(riskScore)
    return totalRisk(riskScore)

# Apply rules 1 and 2 to check which insurance is ineligible.
def checkIneligible(result, processedUserData):
    # Rule 1: If the user has no income, than he's ineligible for disability insurance.
    if (processedUserData['income'] == 0):
        setIneligible(result, ["disability"])

    # Rule 1: If the user has no vehicle, than he's ineligible for auto insurance.
    if (processedUserData['vehicle'] == 0):
        setIneligible(result, ["auto"])

    # Rule 1: If the user has no house, than he's ineligible for house insurance.
    if (processedUserData['house'] == 0):
        setIneligible(result, ["home"])

    # Rule 2: If the user is over 60 years old, than he's ineligible for disability and life insurances.
    if (processedUserData["age"] > 60):
        setIneligible(result, ["disability", "life"])

# Main function: apply the algorithm and return a dict to the server.
def computeRisk(personalInfo):
    if personalInfo is None:
        return {}

    result = computeScore(personalInfo)
    checkIneligible(result, personalInfo)

    return result