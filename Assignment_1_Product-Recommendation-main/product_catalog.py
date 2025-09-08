from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_tags = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    return len(customer_tags.intersection(product_tags))
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    pass




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    matched_list = []
    for product in products: 
        matched_tags = count_matches(set(product['tags']), customer_tags)
        matched_list.append({'name': product['name'], 'matches': matched_tags})

    return matched_list
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    pass



# TODO: Step 7 - Call your function and print the results
print(recommend_products(products, customer_tags))



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why? 
'''
I used loops to iterate through products and put all of the tags into count matches to be intersected with customer tags. Not using a loop here would
have required a lot more code and been less efficient. The intersection operation was also perfect because I already was using a set and it made comparing
data much easier. All that was left to do for count matches was to get the length so that it would return as an interger and not a list.
'''
# 2. How might this code change if you had 1000+ products?
'''
If I had 1000+products I would likely want to look into optimizing the code further to improve efficiency and reduce processing time. The code is scalable so
it will function regardless of the number of products, but a larger dataset might require more effiecent data handling. Also for practical use, I would want to
reduce the returned list to only the top matches rather than all products.
'''