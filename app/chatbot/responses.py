from typing import Dict, List


RESPONSES: Dict[str, Dict] = {
    "greeting": {
        "response": "Hello! I can help you find safety equipment or recommend products.",
        "products": []
    },

    "product_search": {
        "response": "Here are some safety equipment products available.",
        "products": []
    },

    "construction_safety": {
        "response": "Recommended equipment for construction work:",
        "products": [
            "Firefighter Helmet",
            "Cut Resistant Hand Gloves",
            "Industrial Safety Shoe / Gum Boot",
            "High Visibility Safety Vest"
        ]
    },

    "fire_safety": {
        "response": "Fire safety equipment available:",
        "products": [
            "Industrial Fire Extinguisher 5kg",
            "Fire Cylinder 10kg ABC Type",
            "Firefighter Helmet"
        ]
    },

    "ppe_info": {
        "response": "Personal Protective Equipment (PPE) protects workers from workplace hazards.",
        "products": [
            "Personal Protection Equipment Kit"
        ]
    }
}