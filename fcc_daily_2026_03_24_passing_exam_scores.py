def detect_roast(beans):
    bean_points = {
        "'": 1,
        "-": 2,
        ".": 3
    }
    roast = 0
    for bean in beans:
        if bean not in bean_points:
            return "Invalid input"
        roast += bean_points.get(bean)
    avg = roast / len(beans)
    if avg > 2.5:
        return "Dark"
    if avg >= 1.75:
        return "Medium"
    return "Light"