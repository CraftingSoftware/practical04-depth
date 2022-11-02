# Reflection on Analyzing Module Depth and Identifying Information Leakage

## Add Your Name Here

## What is the behavior of `datastore.py get KEY`? What happens if the `KEY` does not exist?

TODO

## What is the behavior of `datastore.py put KEY VALUE`?

TODO

## Looking only at `datastore.py`, describe the complexity of the interface of the `kv_get` module

TODO

## Looking only at `datastore.py`, describe the complexity of the interface of the `kv_put` module

TODO

## Describe the behaviors of the following functions in `kv_get.py`

`check_file_exists`: TODO

`create_empty_file`: TODO

`open_file`: TODO

`get_json`: TODO

`get`: TODO

## Describe the behavior of the following function in `kv_put.py`

`put`: TODO

## State whether the `kv_get` module is deep or shallow and explain how you determined this

TODO

## State whether the `kv_put` module is deep or shallow and explain how you determined this

TODO

## Explain the relationship between module depth and interface complexity

TODO

## Explain how the design of the overall system, such as the separation of the `kv_get` and `kv_put` modules, may indicate temporal decomposition

TODO

## Identify two sources of information leakage across `datastore.py`, `kv_get.py`, and `kv_put.py`

The first source of information leakage is TODO

The second source of information leakage is TODO

## Propose a way to fix one source of information leakage identified above

TODO
