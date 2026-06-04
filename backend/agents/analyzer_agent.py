def analyze_resume(text):

    skills_database = [
        "Python",
        "Java",
        "JavaScript",
        "React",
        "Next.js",
        "FastAPI",
        "Django",
        "SQL",
        "MongoDB",
        "Docker",
        "AWS",
        "Git",
        "HTML",
        "CSS"
    ]

    found_skills = []

    for skill in skills_database:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    missing_skills = [
        skill
        for skill in skills_database
        if skill not in found_skills
    ]

    ats_score = min(
        100,
        int((len(found_skills) / len(skills_database)) * 100)
    )

    suggestions = []

    if ats_score < 50:
        suggestions.append(
            "Add more technical skills relevant to your role"
        )

    if "Git" not in found_skills:
        suggestions.append(
            "Mention Git or version control experience"
        )

    if "Docker" not in found_skills:
        suggestions.append(
            "Add Docker knowledge if applicable"
        )

    if "AWS" not in found_skills:
        suggestions.append(
            "Add cloud skills such as AWS"
        )

    return {
        "ats_score": ats_score,
        "skills_found": found_skills,
        "missing_skills": missing_skills[:10],
        "suggestions": suggestions
    }