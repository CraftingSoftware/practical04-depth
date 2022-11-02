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

## Running GatorGrader

You can gain an approximation of your progress on this assignment by running [GatorGrader](https://github.com/GatorEducator/gatorgrader) locally. You do need to have `gatorgrade` and Python installed to be able to run this command.

```bash
gatorgrade --config config/gatorgrade.yml
```

## Receiving Assistance

If you are having trouble completing any part of this project, then please talk with either the course instructor or a student technical leader during the practical session. Alternatively, you may ask questions in the Discord channel for this course. Finally, you can schedule a meeting during the course instructor's office hours.

## Practical Assessment

The grade that a student receives on this practical assignment is a checkmark grade (0 or 1) and is based on:

- **GitHub Actions CI Build Status**: Students are encouraged to repeatedly try to complete the assignment until it passes all GitHub Actions jobs. Students will receive a checkmark grade if their last before-the-deadline build passes and a green ✔ appears in their GitHub commit log instead of a red ✗.

Students will receive 1 if their solution passes all GatorGrader checks and receives a green ✔ in their last commit.

All grades for this project will be reported through a student's GitHub gradebook repository.
