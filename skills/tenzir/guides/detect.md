---
title: "Overview"
description: "Match security activity and model the resulting findings."
canonical: https://tenzir.com/docs/guides/detect
source: https://tenzir.com/docs/guides/detect.md
section: "Docs"
---

# Overview

> Match security activity and model the resulting findings.

Detection turns normalized events into findings by matching activity, measuring behavior over time, and correlating independent signals. When you first need to calculate rarity, adaptive thresholds, distribution drift, or cardinality, start with our [analysis guides](analyze.md), then decide whether that evidence should become a security finding.

Start with [matching events in TQL](detect/match-events-with-tql.md) and [modeling the resulting OCSF findings](detect/model-detections-in-ocsf.md). Then explore [time-window detection](detect/detect-over-time-windows.md), [stored-event baselines](detect/baseline-from-stored-events.md), [periodic-behavior detection](detect/detect-periodic-behavior.md), [multi-stage detectors](detect/create-multi-stage-detectors.md), [Sigma](detect/execute-sigma-rules.md), [Sigma compatibility with OCSF](detect/check-sigma-rule-compatibility-with-ocsf.md), and [YARA](detect/scan-bytes-with-yara.md).
