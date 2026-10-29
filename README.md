# ECM1408 Assignment 2 - Fall 2014

Python solutions to the second continuous assessment for the University of Exeter module ECM1408 Programming for Science (autumn 2014).

## Overview

The assessment (see `Specification.pdf`) was an individual exercise in writing and testing slightly larger programs. This repository holds solutions written in December 2020, revisiting the 2014 coursework. Questions 1 to 4 live in `q1.py` to `q4.py`. The turtle-drawing parts of question 4 are in `follow.py`, `dragon.py` and `sierpinski.py`.

## What's implemented

| File | Question | What it does |
| --- | --- | --- |
| `q1.py` | 1. Word lengths | `histogram`, `histogram_lengths` and `draw_histogram`. Run as a script, it prints a text histogram of word-length percentages for a given file, with each `*` representing 0.25%. |
| `q2.py` | 2. Shuffling | `shuffle(L)` (Durstenfeld / Fisher-Yates, in place), `check_shuffle`, `quality` and `average_quality`. It prints shuffled lists of integers and Greek letter names, and the average quality over 1000 shuffles of `range(100)`. |
| `q3.py` | 3. Patience | Simulates a variant of patience in which pairs summing to 11, or a visible Jack, Queen and King, are covered by new cards. The game is lost when a tenth pile is needed. `many_plays(N)` plays N games and prints a histogram of the cards left in the deck, reusing `shuffle` from `q2.py` and `histogram` from `q1.py`. |
| `q4.py` | 4. String rewriting (algae) | `algae(S)` applies Lindenmayer's algae rules (A → AB, B → A) and prints the string length for n = 0 to 30. |
| `follow.py` | 4. String rewriting | `follow(turtle, S, step=10, angle=90)` interprets `F`/`E` as forward, and `L`/`R` as left and right turns. |
| `dragon.py` | 4. Heighway dragon | Rewrites the axiom `FA` 12 times (A → ARBF, B → FALB) and draws the result with `follow`. |
| `sierpinski.py` | 4. Sierpinski curve | Rewrites the axiom `E` 8 times (E → FLELF, F → ERFRE) and draws the result with step 2 and angle 60°. |

## Tech stack

Python 3, standard library only (`re`, `sys`, `random` and `turtle`). The specification refers to the course's `exturtle` module; the drawing scripts import the standard `turtle` module under that name.

## Getting started

You need Python 3, and Tk support for the turtle drawings.

Run from the repository root:

```
python q1.py dracula.txt   # word-length histogram
python q2.py               # shuffling demo and quality checks
python q3.py               # 100,000 games of patience, then a histogram
python q4.py               # algae string lengths for n = 0..30
python dragon.py           # draws the Heighway dragon
python sierpinski.py       # draws the Sierpinski curve
```

`q3.py` imports from `q1.py` and `q2.py`, and `dragon.py` and `sierpinski.py` import from `follow.py`, so run them from the root.

## Project structure

```
Specification.pdf   Assessment brief
dracula.txt         Text of the first 10 chapters of Bram Stoker's Dracula, the input for question 1
q1.py ... q4.py     Solutions to questions 1-4
follow.py           Turtle interpreter for rewriting-system strings
dragon.py           Heighway dragon
sierpinski.py       Sierpinski curve
__pycache__/        Committed Python bytecode caches (not needed to run)
```

## Status

The repository is complete and archived. `q3.py` has a `verbose` option on `play` that prints each game step by step, but the script's entry point only runs `many_plays`. `q4.py` prints string lengths rather than the first ten rewritten strings.

## Acknowledgements

The assessment brief is from ECM1408 Programming for Science at the University of Exeter.
