import re

from agent.llm import call_llm
from eval.runner import run_tests

MODEL = "Qwen/Qwen2.5-Coder-7B-Instruct"
SYSTEM = "You are an expert Python programmer. Reply with only one Python code block."


def extract_code(text):
    """Pull code out of a ```python ... ``` block; fall back to the raw text."""
    match = re.search(r"```(?:python)?\n(.*?)```", text, re.DOTALL)
    return match.group(1) if match else text


def solve(task, max_attempts=3):
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": f"{task['prompt']}\nYour code should pass