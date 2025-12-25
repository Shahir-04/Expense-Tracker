from fastmcp import FastMCP

from test import app
mcp=FastMCP.from_fastapi(
    app=app,
    name='Expense-tracker'
)

if __name__=="__main__":
    mcp.run(transport="https",host="0.0.0.0",port=8000)

