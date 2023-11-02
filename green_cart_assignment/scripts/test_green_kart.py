from green_cart_assignment.pom_classes.pom_green_cart import pm_cl_gk

def test_ca_items_cart_add(_driver):
    add_cart = pm_cl_gk(_driver)
    add_cart.searching_ca_items()
    add_cart.click_search()
    add_cart.fetcing_total_items()
    add_cart.adding_items_to_cart()
    add_cart.click_on_cart_button()
    add_cart.click_on_check_out_link()
    add_cart.price_validation_check_out_page()
    add_cart.click_on_place_order()
    add_cart.country_select()
    add_cart.agree_terms_conditions_check_box()
    add_cart.click_on_proceed()
    add_cart.printing_order_confirm_text()
    add_cart.taking_screen_shot_order_confirmation()
