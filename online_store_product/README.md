# Online Store Products (Polymorphism Project)

This project demonstrates **polymorphism** using an abstract base class 
(Product) and three subclasses that each calculate product prices 
differently, showcasing how a single method can behave uniquely across 
various object types.

---

## 💡 Concepts Demonstrated

* Polymorphism (The core focus)
* Abstract Classes (ABC)
* Method Overriding
* Real-world price calculation logic

---

## 📁 Product Types

The system uses an abstract base class and defines three concrete 
subclasses, each with a unique pricing structure:

| Product Type | What It Represents |
| :--- | :--- |
| PhysicalProduct | Physical goods with shipping and weight (requires 
shipping calculation) |
| DigitalProduct | Downloadable software/files (no shipping costs) |
| SubscriptionProduct | Services billed monthly or yearly (often handles 
recurring fees) |

---

## ✨ Features

The core feature is the ability to use a unified interface for diverse 
pricing logic:

* Use a single method (**get_final_price**) for all product types
* Get final price for physical, digital, and subscription products
* Apply shipping costs (only for physical products)
* Apply discounts

---

## ▶️ How to Run

1.  **Clone the project** repository to your local machine.
2.  **Open the file** (store_products.py) in your Python environment.
3.  **Execute the script** from your terminal:

```bash
python store_products.py
