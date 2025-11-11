def response(hey_bob: str) -> str:
    message: str = hey_bob.strip()
    if not message:
        return "Fine. Be that way!"
    if message.upper() == hey_bob and not message.lower() == hey_bob:
        if message[-1] == "?":
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if message[-1] == "?":
        return "Sure."
    return "Whatever."
