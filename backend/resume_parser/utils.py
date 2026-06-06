import re


def clean_json_response(response_text: str) -> str:

    response_text = response_text.strip()

    response_text = re.sub(
        r"^```json",
        "",
        response_text
    )

    response_text = re.sub(
        r"```$",
        "",
        response_text
    )

    return response_text.strip()