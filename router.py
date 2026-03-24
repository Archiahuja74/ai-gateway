def decide_model(prompt):
    length = len(prompt.split())

    if length < 10:
        return "FAST", "short prompt"
    elif "code" in prompt.lower() or "explain" in prompt.lower():
        return "CAPABLE", "needs reasoning"
    else:
        return "FAST", "simple query"