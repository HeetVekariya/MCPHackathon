from mcp.server.fastmcp import FastMCP


def register_destination_connectors(mcp: FastMCP):
    """Register all destination connector tools with the MCP server."""
    from connectors.destination.mongo import (
        create_mongodb_destination,
        delete_mongodb_destination,
        update_mongodb_destination,
    )

    from .neo4j import (
        create_neo4j_destination,
        delete_neo4j_destination,
        update_neo4j_destination,
    )

    # Register Neo4j destination connector tools
    mcp.tool()(create_neo4j_destination)
    mcp.tool()(update_neo4j_destination)
    mcp.tool()(delete_neo4j_destination)

    # Register MongoDB destination connector tools
    mcp.tool()(create_mongodb_destination)
    mcp.tool()(update_mongodb_destination)
    mcp.tool()(delete_mongodb_destination)
