from mcp.server.fastmcp import FastMCP


def register_source_connectors(mcp: FastMCP):
    """Register all source connector tools with the MCP server."""

    from .gdrive import create_gdrive_source, delete_gdrive_source, update_gdrive_source

    mcp.tool()(create_gdrive_source)
    mcp.tool()(update_gdrive_source)
    mcp.tool()(delete_gdrive_source)
