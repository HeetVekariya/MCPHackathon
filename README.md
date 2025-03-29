# Unstructured API MCP Server for Research Paper Data Processing

By leveraging the Unstructured API, this server facilitates easy access to a set of powerful tools that extract meaningful information from research papers, which can then be used for fine-tuning a language model (LLM) to reduce the literature review time for researchers.

## Table of Contents:
1. [Setup](https://github.com/HeetVekariya/MCPHackathon?tab=readme-ov-file#setup)
2. [Requirements](https://github.com/HeetVekariya/MCPHackathon?tab=readme-ov-file#requirements)
3. [Project Flow](https://github.com/HeetVekariya/MCPHackathon?tab=readme-ov-file#project-flow)
4. [Available Tools](https://github.com/HeetVekariya/MCPHackathon?tab=readme-ov-file#available-tools)
5. [Follow Along](https://github.com/HeetVekariya/MCPHackathon?tab=readme-ov-file#follow-along)
6. [Claude Desktop Integration](https://github.com/HeetVekariya/MCPHackathon?tab=readme-ov-file#claude-desktop-integration)
7. [Debugging Tools](https://github.com/HeetVekariya/MCPHackathon?tab=readme-ov-file#debugging-tools)
8. [Running locally minimal client with server](https://github.com/HeetVekariya/MCPHackathon?tab=readme-ov-file#running-locally-minimal-client-accessing-local-the-mcp-server-over-http--sse)


## Setup
Install dependencies:
- `uv add "mcp[cli]"`
- `uv pip install --upgrade unstructured-client python-dotenv`

or use `uv sync`.

## Requirements

Before you can begin working with the **UNS_MCP** project, make sure you have the following setup:

1. **UNSTRUCTURED_API_KEY**  
   - Get your API key from the [Unstructured platform](https://unstructured.io/) to access their API for document processing.

2. **GOOGLEDRIVE_SERVICE_ACCOUNT_KEY**  
   - Set up a Google Cloud project and create a service account to enable access to Google Drive for reading PDFs. Check the set up process [here](https://docs.unstructured.io/api-reference/workflow/sources/google-drive).
   - Save the JSON credentials for your service account and use it to set up the **GOOGLEDRIVE_SERVICE_ACCOUNT_KEY**.

3. **MONGO_DB_CONNECTION_STRING**  
   - Set up a MongoDB database (cloud) and get the connection string for connecting to the database. Check out set up process [here](https://docs.unstructured.io/api-reference/workflow/destinations/mongodb).

4. **.env.template**  
   - The `.env.template` file includes all the required environment variables. Copy this file to `.env` and set the necessary values for the keys mentioned above.

   Example `.env` file:
   ```bash
   UNSTRUCTURED_API_KEY="<key-here>"
   MONGO_DB_CONNECTION_STRING="<CONNECTION_STRING>"
   GOOGLEDRIVE_SERVICE_ACCOUNT_KEY="<converted string>"


## Project Flow

1. User Query to MCP Client

2. Claude Interacts with `UNS_MCP` Server
   - Claude forwards the user's query to the custom MCP server named `UNS_MCP`.

3. MCP Tool Executes Unstructured API
   - `UNS_MCP` interacts with the Unstructured API to process the research paper PDF, extract relevant information, and convert it into structured JSON data.

4. Structured Data (JSON) Output is stored in the destination source
   - The result from the Unstructured API is transformed into JSON format, which can then be further utilized to fine-tune LLMs, helping researchers quickly find the relevant information without manually reading the entire paper.

![](https://github.com/HeetVekariya/MCPHackathon/blob/main/img/user-flow.png)

![](https://github.com/HeetVekariya/MCPHackathon/blob/main/img/unstructured-workflow.png)

## Available Tools

| Tool | Description |
|------|-------------|
| `list_sources` | Lists available sources from the Unstructured API. |
| `get_source_info` | Get detailed information about a specific source connector. |
| `create_gdrive_source` | Create a google drive source connector.
| `update_gdrive_source` | Update an existing google source connector by params. |
| `delete_gdrive_source` | Delete a source connector by source id. |
| `list_destinations` | Lists available destinations from the Unstructured API. |
| `get_destination_info` | Get detailed info about a specific destination connector. Currently, we have s3/weaviate/astra/neo4j/mongo DB (more to come!) |
| `create_mongodb_destination` | Create a mongodb destination connector by params. |
| `update_mongodb_destination` | Update an existing mongodb destination connector by destination id. |
| `delete_mongodb_destination` | Delete a mongodb destination connector by destination id. |
| `list_workflows` | Lists workflows from the Unstructured API. |
| `get_workflow_info` | Get detailed information about a specific workflow. |
| `create_workflow` | Create a new workflow with source, destination id, etc. |
| `run_workflow` | Run a specific workflow with workflow id |
| `update_workflow` | Update an existing workflow by params. |
| `delete_workflow` | Delete a specific workflow by id. |
| `list_jobs` | Lists jobs for a specific workflow from the Unstructured API. |
| `get_job_info` | Get detailed information about a specific job by job id. |
| `cancel_job` |Delete a specific job by id. |


## Follow Along

### 1. **Set Up Required Connectors**

#### Google Drive Source Connector:
- **Create a Google Drive Source Connector** to connect your service account with Google Drive and retrieve PDFs.
- **Test the connection** to ensure accessibility.

#### MongoDB Destination Connector:
- **Set up the MongoDB Destination Connector** to store processed data.
- **Test the connection** to ensure accessibility.

---

### 2. **Develop the Workflow**

1. **Define Connectors**: Set up the **Google Drive** source and **MongoDB** destination connectors.
   
2. **Partitioning**: Use **Auto partitioning** for optimal document splitting.

3. **Chunking**: Apply **by-page chunking** for manageable text segments.

4. **Enrichment**: Use **NER** to extract entities and **table enrichment** for any tables.

5. **Embedding**: Convert text into embeddings for querying or analysis.

Note: **Tweak the Flow**: Adjust any step (partitioning, chunking, enrichment, embedding) as needed.

---

### 3. **Set Up Claude Desktop**

1. Install **Claude Desktop** and integrate it with the UNS_MCP server by following steps given [below](https://github.com/HeetVekariya/MCPHackathon?tab=readme-ov-file#claude-desktop-integration).
2. **Restart Claude** to link with the MCP server and ensure workflow functionality.

---

### 4. **Query and Run the Workflow**

- Use **Claude** to interact with the system and execute queries to list, create, edit, delete and run the workflow. You can perform many such tasks, go through `Available Tools` given above.

### 5. **Results**

![](https://github.com/HeetVekariya/MCPHackathon/blob/main/img/list-workflow.png)
![](https://github.com/HeetVekariya/MCPHackathon/blob/main/img/run-workflow.png)
![](https://github.com/HeetVekariya/MCPHackathon/blob/main/img/ui-job-output.png)

## Claude Desktop Integration

To install in Claude Desktop:

1. Go to `claude_desktop_config.json` by running the below command.

```bash
# For macOS or Linux:
code ~/Library/Application\ Support/Claude/claude_desktop_config.json

# For Windows:
code $env:AppData\Claude\claude_desktop_config.json
```

2. In that file add:
```bash
{
    "mcpServers":
    {
        "UNS_MCP":
        {
            "command": "ABSOLUTE/PATH/TO/.local/bin/uv",
            "args":
            [
                "--directory",
                "ABSOLUTE/PATH/TO/YOUR-UNS-MCP-REPO/uns_mcp",
                "run",
                "server.py"
            ],
            "env":
            [
            "UNSTRUCTURED_API_KEY":"<your key>"
            ],
            "disabled": false
        }
    }
}
```
3. Restart Claude Desktop.

4. Example Issues seen from Claude Desktop.
    - You will see `No destinations found` when you query for a list of destination connectors. Check your API key in `.env` or in your config json, it needs to be your personal key in `https://platform.unstructured.io/app/account/api-keys`.

## Debugging tools

Anthropic provides `MCP Inspector` tool to debug/test your MCP server. Run the following command to spin up a debugging UI. From there, you will be able to add environment variables (pointing to your local env) on the left pane. Include your personal API key there as env var. Go to `tools`, you can test out the capabilities you add to the MCP server.
```
mcp dev uns_mcp/server.py
```

If you need to log request call parameters to `UnstructuredClient`, set the environment variable `DEBUG_API_REQUESTS=false`.
The logs are stored in a file with the format `unstructured-client-{date}.log`, which can be examined to debug request call parameters to `UnstructuredClient` functions.

## Running locally minimal client
```
uv run python minimal_client/client.py uns_mcp/server.py
```

or

```
make local-client
```

Env variables to configure behavior of the client:
- `LOG_LEVEL="ERROR"` # If you would like to hide outputs from the LLM and present clear messages for the user
- `CONFIRM_TOOL_USE='false'` If you would like to disable the tool use confirmation before running it (True by default). **BE MINDFUL** about that option, as LLM can decide to purge all data from your account or run some expensive workflows; use only for development purposes.

## Running locally minimal client, accessing local the MCP server over HTTP + SSE

The main difference here is it becomes easier to set breakpoints on the server side during development -- the client and server are decoupled.

```
# in one terminal, run the server:
uv run python uns_mcp/server.py --host 127.0.0.1 --port 8080

or
make sse-server

# in another terminal, run the client:
uv run python minimal_client/client.py "http://127.0.0.1:8080/sse"
or
make sse-client
```

Hint: `ctrl+c` out of the client first, then the server. Otherwise the server appears to hang.

