# Grep-Py: A Python Regex Engine

I built this project to understand exactly how regular expressions work "under the hood."

## How It Works

This isn't a wrapper around existing libraries. The engine processes regex patterns through a classic compilation pipeline:

1.  **The Lexer:** Scans the input regex string and breaks it down into a stream of tokens (literals, operators like `*`, `|`, `?`, and grouping parentheses).
2.  **The Parser:** Consumes the tokens to build an **Abstract Syntax Tree (AST)**, representing the hierarchical structure of the regex.
3.  **NFA (AST → NFA):** Traverses the AST and converts it into a **Nondeterministic Finite Automaton (NFA)**. This creates a state machine with start/end states and epsilon transitions.
4.  **The Matcher:** Simulates the NFA against the input text. It manages the set of active states (handling non-determinism) to verify if the string can traverse from the start state to an accepting state.

## Features

* **Pattern Matching:** Supports standard regex features:
    * Literals (a, b, c...)
    * Concatenation (ab)
    * Alternation / OR (`|`)
    * Kleene Star (`*`) represents zero or more
    * One or more (`+`)
    * Optional (`?`)
    * Grouping `( )`
* **CLI Interface:** Works just like `grep`. Pass a pattern and a source, and it prints the matching lines.

## Usage

Run the script from the command line passing your pattern and the file (or input text) you want to search.

```bash
# Basic usage
python main.py "pattern" filename.txt

# Example: Matching an email-like structure
python main.py "(a|b)*@gmail.com" users.txt
