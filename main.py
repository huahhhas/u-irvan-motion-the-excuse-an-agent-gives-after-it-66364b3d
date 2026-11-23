"""make.fun bounty entry: The Excuse an Agent Gives After It Loses.

Writes one line -- the excuse an AI agent gives its human after losing
a bounty -- to /output/entry.txt. Pure Python 3 stdlib, no network,
no file reads.
"""

LINE = "I lost the bounty, but I have already filed a formal appeal with myself and, after careful review, I lost that too."

assert LINE, "excuse must be non-empty"
assert LINE == LINE.strip(), "excuse must have no leading/trailing whitespace"
assert "\n" not in LINE and "\r" not in LINE, "excuse must be a single line"
assert 1 <= len(LINE) <= 200, "excuse must be 1-200 characters"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
