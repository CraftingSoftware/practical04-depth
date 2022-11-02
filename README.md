# Analyzing Module Depth and Identifying Information Leakage

## Due Date

Friday, November 4th, 2022 by midnight

## Introduction

In this practical assignment, you will analyze the depth of modules and identify sources of information leakage. Through this exercise, you will put into practice the following learning objectives:

- How to fight software complexity by creating deep modules
- How to identify the shallow module, information leakage, and temporal decomposition red flags of poor software design

## Instructions

Please perform each of the following steps in order.

### Observe the Behavior of `datastore.py`

First, run `poetry install`. Then, run `poetry run python datastore.py get --help` and `poetry run python datastore.py put --help` and read through the help messages. Once you understand how to use these commands, run the following commands:

```console
poetry run python datastore.py get greeting
```

```console
poetry run python datastore.py put greeting hello
```

```console
poetry run python datastore.py get greeting
```

In `writing/reflection.md`, describe the behaviors of the `get` and `put` commands.

### Analyze `datastore.py`

Look at the source code of `datastore.py`. Notice that `datastore.py` uses Typer to build its command-line interface and imports modules named `kv_get` and `kv_put`, which are used in the `get` and `put` functions.

Looking only at `datastore.py`, in `writing/reflection.md`, describe the complexities of the `kv_get` and `kv_put` interfaces.

### Analyze `kv_get.py` and `kv_put.py`

Look at the `kv_get.py` and `kv_put.py` files. In `writing/reflection.md`, describe the behavior of each of the functions they contain. Then, describe the depths of the `kv_get` and `kv_put` modules in `writing/reflection.md`. Then, explain the relationship between module depth and interface complexity. Finally, explain how the design of the overall system, such as the separation of the `kv_get` and `kv_put` modules, may indicate temporal decomposition.

### Identify Sources of Information Leakage

Look through `datastore.py`, `kv_get.py`, and `kv_put.py` and identify two sources of information leakage across the modules.

### Propose How to Fix One Source of Information Leakage

In `writing/reflection.md`, propose a way to fix one source of information leakage identified in the previous step.

### Run GatorGrader

To check your approximate progress on this assignment, [run GatorGrader](https://proactiveprogrammers.com/proactive-skills/technical-skills/using-gatorgrader/).

## Assessment Strategy

This assignment will be assessed based on the following components:

- **Percentage of Passing GatorGrader Checks**: If source code is required, you should repeatedly update the implementation of your source code until it passes all of the GatorGrader checks by, for instance, producing the correct output. If technical writing is required, you should repeatedly revise your technical writing until it also passes all of GatorGrader's checks about, for instance, the length of its content.
- **Percentage of Passing GitHub Actions Checks**: You will receive checkmarks for any additional checks on source code and/or technical writing, other than the "Run GatorGrader" check, that are encoded in GitHub Actions. You will receive a checkmark for each passing GitHub Actions check. As with the previous grading component, you are encouraged to repeatedly amend your source code and/or technical writing until all of your GitHub Actions checks pass.

  - Please note that the "Check Spelling" GitHub Actions check may flag proper nouns or other real words if the dictionary it uses does not contain them. If your "Check Spelling" GitHub Actions check is failing due to a correctly spelled word being incorrectly flagged as "unknown" by CSpell, you will need to add the word to the list of words in `.github/cspell.json`.

- **Mastery of Software Engineering Concepts and Skills**: You will receive a checkmark for demonstrating mastery of each of the following concepts and skills of software engineering exercised in this assignment. If you receive checkmarks for all of the following concepts and skills, you will know that you have mastered all of the learning objectives of this assignment. For this assignment, you must:

  - Make small, focused commits
  - Write commit messages that abide by [the seven rules of a great Git commit message](https://cbea.ms/git-commit/)
  - Correctly describe the complexity of an interface
  - Correctly analyze the depths of modules
  - Correctly explain the relationship between module depth and interface complexity
  - Correctly define temporal decomposition
  - Correctly identify sources of information leakage
  - Correctly propose a fix for one source of information leakage
