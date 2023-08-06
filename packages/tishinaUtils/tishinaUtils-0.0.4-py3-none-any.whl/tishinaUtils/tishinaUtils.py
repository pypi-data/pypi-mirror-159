from itertools import chain, repeat


def isValidInput(promptText: str, failText: str, validInputs: list):
    """Checks if the user input a valid choice."""

    def inputInOptions(reply: str):
        """Checks if input is within valid inputs, returns bool."""
        reply = reply.lower()
        return reply in validInputs

    for value in validInputs:
        if not value.isdigit():
            validInputs[validInputs.index(value)] = value.lower()
    if not failText:
        failText = promptText

    prompts = chain([promptText], repeat(failText))
    replies = map(input, prompts)
    validResponse = next(filter(inputInOptions, replies)).lower()

    return validResponse


def isValidInt(promptText: str, failText: str, validInputs: list):
    """Checks if int input is valid. If validInputs is empty, just checks if an int has been input."""

    def inputInOptions(reply: str):
        """Checks if input is within valid inputs, returns bool."""
        return reply in validInputs and reply.isdigit() if validInputs else reply.isdigit()

    if not failText:
        failText = promptText
    # Chain uses prompt text as initial pop up, once exhausted, moves onto fail text.
    # Repeat when not given a loop amount will loop endlessly, works when prompting fail text.
    prompts = chain([promptText], repeat(failText))
    replies = map(input, prompts)
    validResponse = next(filter(inputInOptions, replies))

    return int(validResponse)