import openai

from settings import *


class API:
    system_prompt: str

    def __init__(self, system_prompt: str) -> None:
        self.system_prompt = system_prompt
        openai.api_key = OPENAI_API_KEY

    def get_response(self, text: str) -> str | None:
        try:
            response = openai.chat.completions.create(
                model="chatgpt-4o-latest",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": text},
                ],
                temperature=0.2,
                top_p=0.1,
            )
            response_text: str = response.choices[0].message.content
        except Exception as e:
            print(e)
            return None

        return self.parse_response(response_text)

    def parse_response(self, response: str) -> str:
        if response.startswith("```html"):
            response = response.removeprefix("```html")
        if response.endswith("```"):
            response = response.removesuffix("```")
        return response.strip()
