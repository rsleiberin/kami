# OpenAI API Model Endpoint Compatibility

This document outlines which models are compatible with specific API endpoints.

## Model Compatibility by Endpoint

| ENDPOINT | COMPATIBLE MODELS |
|----------|-------------------|
| /v1/audio/transcriptions | whisper-1 |
| /v1/audio/translations | whisper-1 |
| /v1/chat/completions | gpt-4, gpt-4-0613, gpt-4-32k, gpt-4-32k-0613, gpt-3.5-turbo, gpt-3.5-turbo-0613, gpt-3.5-turbo-16k, gpt-3.5-turbo-16k-0613 |
| /v1/completions (Legacy) | gpt-3.5-turbo-instruct, babbage-002, davinci-002 |
| /v1/embeddings | text-embedding-ada-002 |
| /v1/fine_tuning/jobs | gpt-3.5-turbo, babbage-002, davinci-002 |
| /v1/moderations | text-moderation-stable, text-moderation-latest |

Ensure that you're using the correct model for the intended endpoint to guarantee optimal results.

