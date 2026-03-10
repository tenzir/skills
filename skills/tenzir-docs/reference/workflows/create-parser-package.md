# Create a parser package


This workflow guides you through creating a package to parse and clean log events. To this end, you scaffold a Tenzir package and build user-defined operators.

* Human

  Complete each numbered step in order. Each step includes:

  * **Results**: What you should have when done
  * **Resources**: Guides and references to help you

* AI Agent

  Execute this workflow systematically:

  1. Enter plan mode to outline all steps
  2. Create a tasklist when leaving plan mode
  3. Execute each step in a subagent, verifying **Results** before proceeding
  4. Use **Resources** links for implementation details

## 1. Understand your data

Start with a deep understanding of the sample data given.

**Results**:

* Context around the given samples
* Name of the vendor and product for the package

**Resources**:

* Internet: search for extra samples to better understand product and vendor.

## 2. Create the package scaffold

Set up the directory structure and manifest file for your package.

**Results**:

* A package for vendor `acme`
* A package manifest: `acme/package.yaml`
* Event samples in `acme/tests/inputs`

**Resources**:

* [Create a package](../../guides/packages/create-a-package.md)

## 3. Add operators

Create user-defined operators for parsing and cleaning. Use the testing framework to validate each step of work.

**Resources**:

* [Add operators](../../guides/packages/add-operators.md)
* [Test packages](../../guides/packages/test-packages.md)

### 3.1 Parsing operator

The parsing operator translates unstructured into structured data. This is only needed when the data is not yet parsed, i.e., a raw string, or when it contains fields that are not yet parsed, e.g., a JSON with `payload` field.

**Results**:

* Operator: `acme::product::parse`
* Test(s): `acme/tests/product/parse.{tql,txt}`

**Resources**:

* [Parse delimited text](../../guides/parsing/parse-delimited-text.md)
* [Parse string fields](../../guides/parsing/parse-string-fields.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)

### 3.2 Cleaning operator

The cleaning operator ensures semantically rich types, replaces sentinel values, and ensures a proper schema if feasible.

**Results**:

* Operator: `acme::product::clean`
* Test(s): `acme/tests/product/clean.{tql,txt}`

**Resources**:

* [Clean up values](../../guides/normalization/clean-up-values.md)
* [Work with time](../../guides/transformation/work-with-time.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)

## 4. Add examples

Add end-to-end examples that showcase how to use the operators. These examples should reflect the collection method that is typical for the given vendor-product combination, e.g.,

```tql
from_* {
  acme::product::parse
  acme::product::clean
}
```

**Results**:

* A few examples that show how to use the operators in the package

**Resources**:

* [Collecting](../../guides/collecting.md)

## 5. Finalize package

Update the package manifest with accurate descriptions reflecting the final implementation. Review operators for idiomatic TQL patterns. Verify all tests pass.

**Results**:

* TQL code adheres to idiomatic best practices
* All tests pass
* Updated and descriptive package manifest

## Contents

- [Create-ocsf-mapping](create-ocsf-mapping.md)