# knowledge_and_data_mining
Knowledge and Data Mining Project: Weighted Model Counting via Knowledge Compilation

## Problem presentation
Write a method that transforms a formula in sd-DNNF form,and use this method for computing the weighted model countof the formula.
Evaluate your approach by comparing the results of yourmethod with the explicit computation of weighted modelcounting via truth table.

To do resolve this problem I proced in the following way:

1. Transform the formula in CNF using SymPy library
2. Transform the formula in d-DNNF:
  - Substitute the negation of the propositional variable with its lower value
  - Separate the input into smaller subformulas
  - Create a dictionary where 'key' is the propositional variable common in the subformulas (or one of the subformula) and 'value' is a tuple made of subformulas
    that share the propositional varibale (or just the subformula)
  - Shannon's Expantion
3. Transform the formula is sd-DNNF:
  - Find the main connective and divide the formula into two subformulas
  - Recursively divide the formula until every disjunction has been found
  - Smooth every disjunction and rebuild the formula
4. Model Counting: just substitues disjunction with a sum and conjunction with a multiplication
5. Truth Table: I modified the code of the following article in order to have also the model counting (https://medium.com/street-science/how-to-implement-a-truth-table-generator-in-python-40185e196a5b)

## How to run code
- Run main1.py to have the result of model counting via truth table
- Run main2.py to have the result of model counting via knowledge compilation
