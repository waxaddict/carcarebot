
def load_common_searches():
    return [
        "How to remove tar from paint",
        "Best way to clean alloy barrels",
        "How to fix water spots",
        "Best snow foam for waxed cars",
        "Iron fallout remover tips"
    ]

def get_placeholder_response(query):
    return {
        "issue": "Iron fallout on white paint.",
        "fix": "Use an iron remover, let it dwell, then rinse thoroughly.",
        "tip": "Work panel by panel to avoid streaking on hot days.",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "products": [
            {
                "name": "Gtechniq W6 Iron Remover",
                "price": "12.95",
                "image": "https://example.com/w6.jpg",
                "buy_url": "https://your-retailer.com/w6"
            },
            {
                "name": "Bilt Hamber Korrosol",
                "price": "14.99",
                "image": "https://example.com/korrosol.jpg",
                "buy_url": "https://your-retailer.com/korrosol"
            }
        ]
    }
