from flask import Flask, render_template, url_for

app = Flask(__name__)

# Sample product data
eco_friendly_products = [
    {
        "name": "Recycled Paper Notebook",
        "description": "A sustainable, eco-friendly notebook made from 100% recycled paper.",
        "price": "$12.99",
        "image_url": "images/notpad.jpg"
    },
    {
        "name": "Wooden Beads",
        "description": "Natural wooden beads for crafting your own eco-friendly jewelry.",
        "price": "$5.99",
        "image_url": "images/beads.jpg"
    },
    # Add more products as needed
]

@app.route('/')
def home():
    return render_template('index.html', products=eco_friendly_products)

@app.route('/product/<int:product_id>')
def product_page(product_id):
    product = eco_friendly_products[product_id]
    return render_template('product_page.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
