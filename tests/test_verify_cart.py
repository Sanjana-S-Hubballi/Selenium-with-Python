from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage

def test_full_cart_flow(driver):
    home = HomePage(driver)
    products = ProductsPage(driver)
    product_details = ProductDetailsPage(driver)
    cart = CartPage(driver)

    # 1️⃣ Open Home page
    home.goto()

    # 2️⃣ Verify Home Page is visible
    assert home.is_home_page_visible()

    # 3️⃣ Click Products link
    home.goto_products()

    # 4️⃣ Verify All Products Page is visible
    assert products.is_all_products_visible()

    # 5️⃣ Verify products list is visible
    assert products.is_products_list_visible()

    # 6️⃣ Click View Product
    products.view_first_product()

    # 7️⃣ Verify Product Details Page is visible
    assert product_details.is_product_details_visible()

    # 8️⃣ Add to Cart
    product_details.add_to_cart()

    # 9️⃣ Click View Cart
    product_details.view_cart()

    # 🔟 Verify product is in cart
    assert cart.is_product_in_cart("Blue Top")

    # ✅ Verify price, quantity, total
    price = cart.get_product_price()
    quantity = cart.get_product_quantity()
    total = cart.get_product_total()

    print(f"Price: {price}, Quantity: {quantity}, Total: {total}")

    assert price.strip() == 'Rs. 500'
    assert quantity.strip() == '1'
    assert total.strip() == 'Rs. 500'