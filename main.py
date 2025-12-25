from fastmcp import FastMCP
import os
from test import app
mcp=FastMCP.from_fastapi(
    app=app,
    name='Expense-tracker'
)
CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), "categories.json")
@mcp.resource("expense:///categories", mime_type="application/json")  # Changed: expense:// → expense:///
def categories():
    try:
        # Provide default categories if file doesn't exist
        default_categories = {
            "categories": [
                "Food & Dining",
                "Transportation",
                "Shopping",
                "Entertainment",
                "Bills & Utilities",
                "Healthcare",
                "Travel",
                "Education",
                "Business",
                "Other"
            ]
        }
        
        try:
            with open(CATEGORIES_PATH, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            import json
            return json.dumps(default_categories, indent=2)
    except Exception as e:
        return f'{{"error": "Could not load categories: {str(e)}"}}'
if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)

