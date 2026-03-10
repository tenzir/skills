# Create an OCSF mapping


This workflow guides you through creating an OCSF mapping for a parser package. It builds on a [parser package](create-parser-package.md), adding OCSF-specific mapping and validation steps.

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

## 1. Create a parser package

Before mapping to OCSF, you need a package that can parse and clean your source data. Complete a parser package workflow first.

**Results**:

* A working parser package
* All parsing tests passing

**Resources**:

* [Create a parser package](create-parser-package.md)

## 2. Identify the OCSF event class

Analyze your source events to determine which OCSF event class best represents them. Consider the event semantics, not just field names.

**Results**:

* The OCSF event class (e.g., `network_activity`, `authentication`)
* Understanding of required vs. optional attributes

**Resources**:

* [OCSF](../ocsf.md)

## 3. Write mapping operators

For each log type, create a user-defined operator that transforms cleaned events into the OCSF schema. Map source fields to OCSF attributes, handling type conversions and nested structures.

**Results**:

* Main dispatching operator: `acme::vendor::product::ocsf::map`
* Test: `acme/tests/product/ocsf/map.{tql,txt}`
* Event-specific operator(s): `acme::vendor::product::ocsf::event::foo`
* Test(s): `acme/tests/product/ocsf/event/log.{tql,txt}`

**Resources**:

* [Map to OCSF](../../guides/normalization/map-to-ocsf.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)

## 4. Add end-to-end examples

Add examples showing the complete pipeline from raw data to OCSF output:

```tql
from_* {
  acme::product::parse
  acme::product::clean
  acme::product::ocsf::map
}
```

**Results**:

* Examples demonstrating the full normalization pipeline

**Resources**:

* [Collecting](../../guides/collecting.md)

## 5. Finalize package

Update the package manifest to include the OCSF mapping operator. Review operators for idiomatic TQL patterns. Verify all tests pass, including OCSF validation.

**Results**:

* TQL code adheres to idiomatic best practices
* All tests pass
* Updated package manifest with OCSF operator documentation