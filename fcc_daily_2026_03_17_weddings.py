def get_milestone(years):
    materials = {
        1: "Paper",
        5: "Wood",
        10: "Tin",
        25: "Silver",
        40: "Ruby",
        50: "Gold",
        60: "Diamond",
        70: "Platinum"
    }
    return switch_on_material(years)

def switch_on_material(code):
    if   code >= 70:
        return "Platinum"
    elif code >= 60:
        return "Diamond"
    elif code >= 50:
        return "Gold"
    elif code >= 40:
        return "Ruby"
    elif code >= 25:
        return "Silver"
    elif code >= 10:
        return "Tin"
    elif code >= 5:
        return "Wood"
    elif code >= 1:
        return "Paper"
    else:
        return "Newlyweds"