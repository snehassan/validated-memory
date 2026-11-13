# Validated Agent Memory
Validated Agent Memory is a research prototype that tests whether AI agents improve more reliably when they only remember lessons that have been checked for correctness.

A coding agent (Qwen2.5-Coder 7B) solves MBPP programming tasks in sequence, writing a short lesson after each task. The project compares agents with no memory, with every lesson stored, and with only lessons approved by a panel of models that debate whether each lesson is correct. It also stress-tests memory by injecting deliberately wrong lessons, and compares strategies for pruning memory as it grows.

The intended use is research: measuring whether validated memory helps agents learn on the job, how vulnerable unvalidated memory is to bad lessons, and when memory starts hurting performance. Results are meant to inform the design of self-improving agents.
