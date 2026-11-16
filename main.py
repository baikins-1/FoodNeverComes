
from drafter import *
from dataclasses import dataclass, field



# DATA CLASSES
# need to add debug stuff???
# need to unit test as well


@dataclass
class Food:
    id: int
    name: str
    meal_type: str
    cuisine: str
    price: float
    description: str
    image: str


@dataclass
class CartItem:
    food_id: int
    quantity: int = 1


@dataclass
class State:
    foods: list
    cart: list = field(default_factory=list)
    selected_category: str = "All"
    selected_cuisine: str = "All"
    selected_food_id: int = 0
    message: str = ""


# FOOD MENU used chat...


def create_foods():
    return [
        Food(1, "Classic Cheeseburger", "Main Dishes", "American",
             12.99, "A juicy burger with cheese, lettuce, tomato, and sauce.",
             "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=700"),

        Food(2, "Double Smash Burger", "Main Dishes", "American",
             14.99, "Two smashed beef patties with melted cheese.",
             "https://plus.unsplash.com/premium_photo-1683619761492-639240d29bb5?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D"),

        Food(3, "Pepperoni Pizza", "Main Dishes", "Italian",
             15.99, "Classic pizza topped with mozzarella and pepperoni.",
             "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=700"),

        Food(4, "Cheese Pizza", "Main Dishes", "Italian",
             13.99, "Freshly baked pizza with extra mozzarella.",
             "https://images.unsplash.com/photo-1579751626657-72bc17010498?w=700"),

        Food(5, "Chicken Tenders", "Main Dishes", "American",
             11.99, "Crispy golden chicken tenders with dipping sauce.",
             "https://images.unsplash.com/photo-1562967914-608f82629710?w=700"),

        Food(6, "Chicken Sandwich", "Main Dishes", "American",
             12.49, "Crispy chicken with lettuce and a creamy sauce.",
             "https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=700"),

        Food(7, "French Fries", "Sides", "American",
             4.99, "Golden crispy fries with a little sea salt.",
             "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=700"),

        Food(8, "Mac and Cheese", "Sides", "American",
             6.99, "Creamy macaroni covered in melted cheese.",
             "https://images.unsplash.com/photo-1543339494-b4cd4f7ba686?w=700"),

        Food(9, "Chocolate Brownie", "Desserts", "American",
             5.99, "Rich chocolate brownie with a soft center.",
             "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=700"),

        Food(10, "Strawberry Cheesecake", "Desserts", "American",
             7.49, "Creamy cheesecake topped with fresh strawberries.",
             "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=700"),

        Food(11, "Iced Coffee", "Drinks", "American",
             4.99, "Cold coffee served over ice.",
             "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=700"),

        Food(12, "Strawberry Smoothie", "Drinks", "American",
             5.99, "A refreshing smoothie made with strawberries.",
             "https://images.unsplash.com/photo-1553530666-ba11a7da3888?w=700"),

        Food(13, "Loaded Nachos", "Sides", "Mexican",
             9.99, "Tortilla chips loaded with cheese, salsa, and toppings.",
             "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?w=700"),

        Food(14, "Chicken Alfredo", "Main Dishes", "Italian",
             15.49, "Creamy Alfredo pasta with grilled chicken.",
             "https://images.unsplash.com/photo-1645112411341-6c4fd023714a?w=700"),

        Food(15, "Sushi Rolls", "Main Dishes", "Japanese",
             13.99, "Fresh sushi rolls served with soy sauce.",
             "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=700"),

        Food(16, "Chocolate Milkshake", "Drinks", "American",
             6.49, "A thick chocolate milkshake topped with whipped cream.",
             "https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=700"),

        Food(17, "Pancakes", "Breakfast", "American",
             9.99, "Fluffy pancakes served with syrup and butter.",
             "https://images.unsplash.com/photo-1528207776546-365bb710ee93?w=700"),

        Food(18, "Chicken Wings", "Sides", "Korean",
             10.99, "Crispy chicken wings tossed in a flavorful sauce.",
             "https://images.unsplash.com/photo-1527477396000-e27163b481c2?w=700"),

        Food(19, "Strawberry Donut", "Desserts", "American",
             3.99, "A soft donut covered in strawberry icing.",
             "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=700"),

        Food(20, "Caesar Salad", "Main Dishes", "Italian",
             10.99, "Fresh lettuce with parmesan, croutons, and Caesar dressing.",
             "https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=700"),
        
        Food(21, "BBQ Bacon Burger", "Main Dishes", "American",
             14.99, "Beef burger with crispy bacon, BBQ sauce, and cheddar.",
             "https://images.unsplash.com/photo-1553979459-d2229ba7433a?w=700"),

        Food(22, "Buffalo Chicken Wrap", "Main Dishes", "American",
             11.49, "Chicken tossed in buffalo sauce with lettuce and ranch.",
             "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=700"),

        Food(23, "Chicken Quesadilla", "Main Dishes", "Mexican",
             12.99, "Grilled tortilla filled with chicken and melted cheese.",
             "https://images.unsplash.com/photo-1618040996337-56904b7850b9?w=700"),

        Food(24, "Beef Tacos", "Main Dishes", "Mexican",
             10.99, "Three tacos filled with seasoned beef and fresh toppings.",
             "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=700"),

        Food(25, "Chicken Burrito", "Main Dishes", "Mexican",
             13.49, "Rice, chicken, beans, cheese, and salsa in a tortilla.",
             "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=700"),

        Food(26, "Shrimp Tacos", "Main Dishes", "Mexican",
             14.99, "Seasoned shrimp tacos with fresh slaw.",
             "https://images.unsplash.com/photo-1512838243191-e81e8f66f1fd?w=700"),

        Food(27, "Chicken Parmesan", "Main Dishes", "Italian",
             16.99, "Breaded chicken with marinara and melted mozzarella.",
             "https://images.unsplash.com/photo-1632778149955-e80f8ceca2e8?w=700"),

        Food(28, "Spaghetti and Meatballs", "Main Dishes", "Italian",
             15.49, "Spaghetti with homemade-style meatballs and tomato sauce.",
             "https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=700"),

        Food(29, "Margherita Pizza", "Main Dishes", "Italian",
             14.49, "Pizza topped with tomato, mozzarella, and basil.",
             "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=700"),

        Food(30, "Lasagna", "Main Dishes", "Italian",
             16.49, "Layers of pasta, cheese, and rich tomato sauce.",
             "https://images.unsplash.com/photo-1574894709920-11b28e7367e3?w=700"),

        Food(31, "Chicken Teriyaki Bowl", "Main Dishes", "Japanese",
             13.99, "Grilled chicken with teriyaki sauce and steamed rice.",
             "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=700"),

        Food(32, "Ramen", "Main Dishes", "Japanese",
             14.99, "Warm noodles in a flavorful broth with toppings.",
             "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=700"),

        Food(33, "Chicken Fried Rice", "Main Dishes", "Chinese",
             12.49, "Fried rice with chicken, vegetables, and egg.",
             "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=700"),

        Food(34, "Orange Chicken", "Main Dishes", "Chinese",
             13.99, "Crispy chicken coated in a sweet orange sauce.",
             "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=700"),

        Food(35, "Beef and Broccoli", "Main Dishes", "Chinese",
             14.49, "Tender beef and broccoli in a savory sauce.",
             "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=700"),

        Food(36, "Bibimbap", "Main Dishes", "Korean",
             14.99, "Korean rice bowl with vegetables, egg, and sauce.",
             "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=700"),

        Food(37, "Korean BBQ Bowl", "Main Dishes", "Korean",
             15.49, "Sweet and savory Korean-style beef over rice.",
             "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=700"),

        Food(38, "Chicken Katsu", "Main Dishes", "Japanese",
             14.99, "Crispy breaded chicken with rice and katsu sauce.",
             "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=700"),

        Food(39, "Garlic Bread", "Sides", "Italian",
             4.49, "Toasted bread with garlic butter and herbs.",
             "https://plus.unsplash.com/premium_photo-1711752902734-a36167479983?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D"),

        Food(40, "Mozzarella Sticks", "Sides", "American",
             6.49, "Crispy mozzarella sticks with marinara sauce.",
             "https://images.unsplash.com/photo-1531749668029-2db88e4276c7?w=700"),

        Food(41, "Onion Rings", "Sides", "American",
             5.49, "Golden fried onion rings.",
             "https://images.unsplash.com/photo-1639024471283-03518883512d?w=700"),

        Food(42, "Guacamole and Chips", "Sides", "Mexican",
             7.49, "Fresh guacamole served with crunchy tortilla chips.",
             "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=700"),

        Food(43, "Spring Rolls", "Sides", "Chinese",
             5.99, "Crispy vegetable spring rolls with dipping sauce.",
             "https://images.unsplash.com/photo-1548507200-3c8c7a3f2b0e?w=700"),

        Food(44, "Chocolate Lava Cake", "Desserts", "American",
             7.99, "Warm chocolate cake with a gooey chocolate center.",
             "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=700"),

        Food(45, "Tiramisu", "Desserts", "Italian",
             7.49, "Coffee-soaked cake layered with creamy mascarpone.",
             "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=700"),

        Food(46, "Churros", "Desserts", "Mexican",
             6.49, "Crispy cinnamon sugar churros with chocolate dip.",
             "https://images.unsplash.com/photo-1624371414361-e670edf4898d?w=700"),

        Food(47, "Mochi Ice Cream", "Desserts", "Japanese",
             6.99, "Soft rice dough filled with sweet ice cream.",
             "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=700"),

        Food(48, "Chocolate Chip Cookies", "Desserts", "American",
             3.99, "Soft cookies filled with chocolate chips.",
             "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=700"),

        Food(49, "Matcha Latte", "Drinks", "Japanese",
             5.49, "Creamy iced matcha latte.",
             "https://images.unsplash.com/photo-1515823064-d6e0c04616a7?w=700"),

        Food(50, "Mango Smoothie", "Drinks", "American",
             5.99, "Sweet mango blended into a refreshing smoothie.",
             "https://images.unsplash.com/photo-1502741224143-90386d7f8c82?w=700")

    ]



# DESIGN used chat also


SITE_CSS = """
body {
    background-color: #FCE8EF;
    color: #54283A;
    font-family: Arial, sans-serif;
}

button {
    cursor: pointer;
    border-radius: 12px;
    border: none;
    padding: 12px 18px;
    font-weight: bold;
    background-color: #C65D82;
    color: white;
    transition: background-color 0.2s ease;
}

button:hover {
    background-color: #A94368;
}

h1, h2, h3 {
    color: #54283A;
}

a {
    color: #A94368;
}
"""


def make_page(state, content):
    return Page(state, content, css=SITE_CSS)



# HELPER FUNCTIONS


def find_food(state, food_id):
    for food in state.foods:
        if food.id == food_id:
            return food
    return None


def cart_total(state):
    total = 0

    for item in state.cart:
        food = find_food(state, item.food_id)
        if food:
            total += food.price * item.quantity

    return total


def cart_count(state):
    count = 0

    for item in state.cart:
        count += item.quantity

    return count


def get_filtered_foods(state):
    results = []

    for food in state.foods:
        category_matches = (
            state.selected_category == "All"
            or food.meal_type == state.selected_category
        )

        cuisine_matches = (
            state.selected_cuisine == "All"
            or food.cuisine == state.selected_cuisine
        )

        if category_matches and cuisine_matches:
            results.append(food)

    return results


def navigation():
    return Div(
        Button("Home", "index"),
        Button("View Cart", "view_cart"),
        style="display:flex; gap:12px; margin-bottom:25px;"
    )



# FOOD CARDS


def food_card(food, state):

    card_style = (
        "background-image: linear-gradient("
        "to top, rgba(20,35,25,0.90), "
        "rgba(20,35,25,0.02)), "
        "url('" + food.image + "');"
        "background-size: cover;"
        "background-position: center;"
        "color: white;"
        "display: flex;"
        "flex-direction: column;"
        "justify-content: flex-end;"
        "box-sizing: border-box;"
        "width: 360px;"
        "height: 380px;"
        "min-width: 360px;"
        "flex: 0 0 360px;"
        "border-radius: 22px;"
        "border: none;"
        "padding: 20px;"
        "white-space: pre-line;"
        "text-align: left;"
        "font-size: 18px;"
        "font-weight: bold;"
        "margin: 5px;"
    )

    return Button(
        food.name
        + "\n$" + str(food.price)
        + "\nView Details →",
        "index",
        [
            Argument("selected_food_id", food.id),
            Argument("selected_category", state.selected_category),
            Argument("selected_cuisine", state.selected_cuisine)
        ],
        style=card_style
    )



# CATEGORY BUTTONS


def category_buttons(state):

    categories = [
        "All",
        "Main Dishes",
        "Sides",
        "Desserts",
        "Drinks",
        "Breakfast"
    ]

    buttons = []

    for category in categories:
        buttons.append(
            Button(
                category,
                "index",
                [
                    Argument("selected_category", category),
                    Argument("selected_cuisine", state.selected_cuisine)
                ]
            )
        )

    return Div(
        *buttons,
        style="display:flex; flex-wrap:wrap; gap:10px; margin-bottom:20px;"
    )


def cuisine_buttons(state):

    cuisines = [
    "All",
    "American",
    "Italian",
    "Mexican",
    "Japanese",
    "Korean",
    "Chinese"
]

    buttons = []

    for cuisine in cuisines:
        buttons.append(
            Button(
                cuisine,
                "index",
                [
                    Argument("selected_cuisine", cuisine),
                    Argument("selected_category", state.selected_category)
                ]
            )
        )

    return Div(
        *buttons,
        style="display:flex; flex-wrap:wrap; gap:10px; margin-bottom:25px;"
    )



# FOOD POP-UP dont know how this works wow


def food_popup(state, food):

    if food is None:
        return Div()

    overlay_style = (
        "position:fixed;"
        "top:0;"
        "left:0;"
        "width:100%;"
        "height:100%;"
        "background:rgba(0,0,0,0.65);"
        "z-index:9999;"
        "display:flex;"
        "justify-content:center;"
        "align-items:center;"
        "padding:20px;"
        "box-sizing:border-box;"
    )

    popup_style = (
        "background:#fffdf7;"
        "color:#26382d;"
        "width:90%;"
        "max-width:650px;"
        "max-height:90vh;"
        "overflow-y:auto;"
        "border-radius:25px;"
        "padding:25px;"
        "box-sizing:border-box;"
        "box-shadow:0 10px 40px rgba(0,0,0,0.3);"
    )

    image_style = (
        "width:100%;"
        "height:280px;"
        "object-fit:cover;"
        "border-radius:18px;"
    )

    return Div(
        Div(
            Div(
                Button(
                    "✕",
                    "index",
                    [
                        Argument("selected_food_id", 0),
                        Argument("selected_category", state.selected_category),
                        Argument("selected_cuisine", state.selected_cuisine)
                    ],
                    style="float:right; background:#F7C7D8; color:#54283A;"
                ),
                style="display:flex; justify-content:flex-end;"
            ),

            Image(food.image, style=image_style),

            Header(food.name, size=2),

            Paragraph(food.description),

            Paragraph(
                "Cuisine: " + food.cuisine
                + "  |  Category: " + food.meal_type
            ),

            Header("$" + str(food.price), size=2),

            Button(
                "Add to Cart",
                "add_to_cart",
                [Argument("food_id", food.id)],
                style="background:#C65D82; color:white; width:100%;"
            ),

            style=popup_style
        ),
        style=overlay_style
    )



# HOME PAGE


@route
def index(state: State,
          selected_food_id: int = 0,
          selected_category: str = "All",
          selected_cuisine: str = "All"):

    state.selected_category = selected_category
    state.selected_cuisine = selected_cuisine
    state.selected_food_id = selected_food_id

    content = [
        navigation(),

        Header("FoodNeverComes", size=2),

        Paragraph(
            "Your favorite food, all in one place."
        ),

        Header("Explore Food", size=2),

        Paragraph("Browse by meal type"),

        category_buttons(state),

        Paragraph("Explore different cuisines"),

        cuisine_buttons(state),

        Header("Popular Food", size=2)
    ]

    filtered_foods = get_filtered_foods(state)

    if len(filtered_foods) == 0:
        content.append(Paragraph("No food found in this category."))
    else:
        cards = []

        for food in filtered_foods:
            cards.append(food_card(food, state))

        content.append(
            Div(
                *cards,
                style=(
                    "display:flex;"
                    "flex-direction:row;"
                    "overflow-x:auto;"
                    "overflow-y:hidden;"
                    "gap:18px;"
                    "padding:15px 5px 25px;"
                    "width:100%;"
                    "scroll-snap-type:x mandatory;"
                    "scrollbar-width:none;"
                    "-ms-overflow-style:none;"
                )
            )
        )

    content.append(
        Header("A little something for everyone", size=2)
    )

    
    # Show the pop-up only when a food item is selected idk how this works
    if selected_food_id != 0:
        selected_food = find_food(state, selected_food_id)

        if selected_food:
            content.append(food_popup(state, selected_food))

    return make_page(state, content)



# ADD TO CART


@route
def add_to_cart(state: State, food_id: int):

    found = False

    for item in state.cart:
        if item.food_id == food_id:
            item.quantity += 1
            found = True
            break

    if not found:
        state.cart.append(CartItem(food_id, 1))

    state.message = "Added to your cart!"

    return make_page(
        state,
        [
            navigation(),
            Header("Added to Cart!", size=1),
            Paragraph(state.message),
            Button("Continue Shopping", "index"),
            Button("View Cart", "view_cart")
        ]
    )



# VIEW CART


@route
def view_cart(state: State):

    content = [
        navigation(),
        Header("Your Cart", size=1)
    ]

    if len(state.cart) == 0:
        content.append(Paragraph("Your cart is empty."))
        content.append(Button("Browse Food", "index"))

    else:
        for item in state.cart:
            food = find_food(state, item.food_id)

            if food:
                content.append(
                    Div(
                        Header(food.name, size=3),
                        Paragraph(
                            "$" + str(food.price)
                            + " x " + str(item.quantity)
                        ),
                        Paragraph(
                            "Subtotal: $"
                            + format(food.price * item.quantity, ".2f")
                        ),
                        Button(
                            "Remove",
                            "remove_from_cart",
                            [Argument("food_id", food.id)]
                        ),
                        style=(
                            "background:white;"
                            "padding:18px;"
                            "border-radius:15px;"
                            "margin-bottom:15px;"
                        )
                    )
                )

        content.append(
            Header(
                "Total: $" + format(cart_total(state), ".2f"),
                size=2
            )
        )

        content.append(Button("Checkout", "checkout"))
        content.append(Button("Continue Shopping", "index"))

    return make_page(state, content)



# REMOVE FROM CART


@route
def remove_from_cart(state: State, food_id: int):

    new_cart = []

    for item in state.cart:
        if item.food_id != food_id:
            new_cart.append(item)

    state.cart = new_cart

    return view_cart(state)



# CHECKOUT PREVIEW need to add actual checkout dont know how it works either


@route
def checkout(state: State):

    content = [
        navigation(),
        Header("Checkout", size=1),
    ]

    if len(state.cart) == 0:
        content.append(Paragraph("Your cart is empty."))
        content.append(Button("Browse Food", "index"))

    else:
        for item in state.cart:
            food = find_food(state, item.food_id)

            if food:
                content.append(
                    Paragraph(
                        food.name + " x " + str(item.quantity)
                        + " — $"
                        + format(food.price * item.quantity, ".2f")
                    )
                )

        content.append(
            Header(
                "Order Total: $" + format(cart_total(state), ".2f"),
                size=2
            )
        )

        content.append(
            Paragraph(
                "No payment will be collected and no food will be delivered."
            )
        )

        content.append(Button("Back to Cart", "view_cart"))
        content.append(Button("Back to Home", "index"))

    return make_page(state, content)



# START WEBSITE


start_server(
    State(foods=create_foods()),
    site_title="FoodNeverComes"
)


