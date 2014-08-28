"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basic": [
        {
            "input": [0, 0, 'conjunction'],
            "answer": 0,
        },
        {
            "input": [0, 1, 'conjunction'],
            "answer": 0,
        },
        {
            "input": [1, 0, 'conjunction'],
            "answer": 0,
        },
        {
            "input": [1, 1, 'conjunction'],
            "answer": 1,
        },
        {
            "input": [0, 0, 'disjunction'],
            "answer": 0,
        },
        {
            "input": [0, 1, 'disjunction'],
            "answer": 1,
        },
        {
            "input": [1, 0, 'disjunction'],
            "answer": 1,
        },
        {
            "input": [1, 1, 'disjunction'],
            "answer": 1,
        },
    ],
    "Extra": [

        {
            "input": [0, 0, 'implication'],
            "answer": 1,
        },
        {
            "input": [0, 1, 'implication'],
            "answer": 1,
        },
        {
            "input": [1, 0, 'implication'],
            "answer": 0,
        },
        {
            "input": [1, 1, 'implication'],
            "answer": 1,
        },
        {
            "input": [0, 0, 'exclusive'],
            "answer": 0,
        },
        {
            "input": [0, 1, 'exclusive'],
            "answer": 1,
        },
        {
            "input": [1, 0, 'exclusive'],
            "answer": 1,
        },
        {
            "input": [1, 1, 'exclusive'],
            "answer": 0,
        },
        {
            "input": [0, 0, 'equivalence'],
            "answer": 1,
        },
        {
            "input": [0, 1, 'equivalence'],
            "answer": 0,
        },
        {
            "input": [1, 0, 'equivalence'],
            "answer": 0,
        },
        {
            "input": [1, 1, 'equivalence'],
            "answer": 1,
        },
    ]
}
