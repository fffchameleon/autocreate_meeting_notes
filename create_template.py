def create_template(meeting_time, presentation_people, followup_people):
    template_content = f"# {meeting_time} meeting\n\n"
    template_content += "## Follow up\n"
    for person in followup_people:
        template_content += f"### {person}\n\n"

    template_content += "\n## Presentation\n"
    for person in presentation_people:
        template_content += f"### {person}\n\n"

    print("Generated Template:")
    print(template_content)
    return template_content