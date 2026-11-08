import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("EcommerceDemo")

# Mock Database: 5 Products
PRODUCTS = [
    {"id": 1, "name": "Wireless Noise-Canceling Headphones", "category": "Audio", "price": 199.99, "stock": 45, "desc": "Over-ear headphones with active noise cancellation and 30-hour battery life."},
    {"id": 2, "name": "Bluetooth Workout Earbuds", "category": "Audio", "price": 59.99, "stock": 120, "desc": "Compact water-resistant earbuds suitable for running and gym."},
    {"id": 3, "name": "Smartwatch Pro", "category": "Wearables", "price": 149.50, "stock": 30, "desc": "Fitness tracking, heart rate monitor, and smartphone notifications."},
    {"id": 4, "name": "Mechanical Gaming Keyboard", "category": "Computers", "price": 89.99, "stock": 60, "desc": "RGB backlit keyboard with tactile mechanical switches."},
    {"id": 7, "name": "Waterproof Hiking Jacket", "category": "Apparel", "price": 79.99, "stock": 85, "desc": "Breathable, lightweight rain jacket for outdoor trails."}
]

@mcp.tool()
def search_products(query: str) -> str:
    """
    Search the e-commerce store for products matching a customer's requirement.
    Returns a brief list of matching products with their IDs.
    """
    query = query.lower()
    results = [p for p in PRODUCTS if query in p["name"].lower() or query in p["category"].lower() or query in p["desc"].lower()]
    
    if not results:
        return f"No products found matching: '{query}'"
    
    return json.dumps([{"id": p["id"], "name": p["name"], "price": p["price"]} for p in results], indent=2)

@mcp.tool()
def get_product_details(product_id: int) -> str:
    """
    Fetch the complete details, full description, and current stock for a specific product ID.
    """
    for p in PRODUCTS:
        if p["id"] == product_id:
            return json.dumps(p, indent=2)
            
    return f"Error: Product with ID {product_id} not found."

if __name__ == "__main__":
    mcp.run(transport='stdio')
