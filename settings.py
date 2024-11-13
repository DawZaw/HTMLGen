import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT: str = """Based on given article, format it using proper HTML structure without <html>, <head> and <body> tags. 
Tags to use include <article>, <header>, <section>, <h1>, <h2>, <p>, <figure>, <img>, <figcaption>. 
Determine which parts are title, headers and paragraphs. 
<figure> tag should contain <img> with attributes src="image_placeholder.jpg" and alt which should be a prompt proposed by you to generate fitting image for corresponding paragraph also use it in <figcaption> in polish. 
Your response must include only html code."""