from datasets import load_dataset


def load_mbpp():
    """Load the sanitized MBPP test split as a list of task dicts."""
    dataset = load_dataset("google-research-datasets/mbpp", "sanitized", split="test")
    tasks = []
    for row in dataset:
        tests = row["test_list"]
        if len(tests) < 2:
            continue  # need at least one held-out test to score fairly
        tasks.append({
            "task_id": row["task_id"],
            "prompt": row["prompt"],
            "code": row["code"],            # reference solution (never shown to the agent)
            "visible_test": tests[0],       # shown to the agent
            "heldout_tests": tests[1:],     # only used for scoring
            "imports": row["test_imports"], # imports some tests need
        })
    return tasks