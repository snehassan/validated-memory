from datasets import load_dataset


def load_mbpp():
    """Load the sanitized MBPP test split as a list of task dicts."""
    dataset = load_dataset("google-research-datasets/mbpp", "sanitized", split="test")
    tasks = []
    for row in dataset:
        tasks.append({
            "task_id": row["task_id"],
            "prompt": row["prompt"],
            "code": row["code"],          # reference solution (never shown to the agent)
            "tests": row["test_list"],    # list of assert statements
            "imports": row["test_imports"],  # imports some tests need
        })
    return tasks