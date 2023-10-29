# OpenAI API Data Usage Policy (As of March 1, 2023)

## Data Ownership and Use
- **Data Ownership**: Your data remains yours.
- **Training & Improvement**: Data sent to the OpenAI API is not utilized to train or enhance OpenAI models, unless you choose to opt in. Opting in can lead to models refining their performance on your specific use cases.
- **Data Retention**: To combat misuse, API data might be retained for a maximum of 30 days. After this period, it will be removed unless law mandates otherwise.
- **Zero Data Retention**: For trusted clients with sensitive applications, there's an option for zero data retention. Here, both request and response bodies aren't logged and are retained solely in memory during the request process.
- **Consumer Services**: The above data policy is exclusive to the OpenAI API and doesn't extend to consumer services like ChatGPT or DALL·E Labs.

## Default Usage Policies by Endpoint

| ENDPOINT | DATA USED FOR TRAINING | DEFAULT RETENTION | ELIGIBLE FOR ZERO RETENTION |
|----------|------------------------|-------------------|-----------------------------|
| /v1/completions | No | 30 days | Yes |
| /v1/chat/completions | No | 30 days | Yes |
| /v1/edits | No | 30 days | Yes |
| /v1/images/generations | No | 30 days | No |
| /v1/images/edits | No | 30 days | No |
| /v1/images/variations | No | 30 days | No |
| /v1/embeddings | No | 30 days | Yes |
| /v1/audio/transcriptions | No | Zero data retention | - |
| /v1/audio/translations | No | Zero data retention | - |
| /v1/files | No | Until deleted by customer | No |
| /v1/fine_tuning/jobs | No | Until deleted by customer | No |
| /v1/fine-tunes | No | Until deleted by customer | No |
| /v1/moderations | No | Zero data retention | - |

For comprehensive information, refer to the [API data usage policies](#). To understand more about zero retention, consider contacting the sales team.
