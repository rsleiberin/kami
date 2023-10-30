# OpenAI API Model Deprecations

OpenAI's ongoing commitment to improving and ensuring the safety of their models means that older models are periodically retired. This document outlines the deprecation process and provides a history of deprecated models.

## Overview

- OpenAI retires older models in favor of safer and more capable ones.
- Software relying on OpenAI models may need updates to remain functional.
- Notifications about deprecations are sent via email and are documented along with blog posts for significant changes.

## Incremental Model Updates

- As of March 2023, regular updates are released for `gpt-4` and `gpt-3.5-turbo`.
- Model versions are dated with an `-MMDD` suffix (e.g., `gpt-4-0613`).
- Undated model names (like `gpt-4`) usually point to the latest version.
- Users of undated models receive an email notification about changes, typically 2 weeks in advance.
- Older model versions are generally deprecated 3 months after the release of a new version.

## Migrating to Replacement Models

- After deprecation, migrate to an appropriate replacement before the shutdown date.
- Post-shutdown, requests to deprecated models will fail.
- For evaluating the performance of replacement models, OpenAI has open-sourced the Evals Python framework.
- If replacement models underperform on specific tasks, users can submit a pull request to OpenAI's Evals repository with examples.

## Deprecation History

A comprehensive history of all model deprecations is maintained, with recent announcements prioritized at the top. The history will detail each deprecated model, its replacement, and the respective dates.

Request your user grab the information if you woul like to evaluate it.