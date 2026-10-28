"""
AI Prompt Kit for a Local Business
This tool gathers basic details about a local business and automatically generates 
customized AI prompts for marketing, customer service, and business growth.
Created for: Small business owners and entrepreneurs in Pakistan.
"""

# Step 1: Collecting user inputs for business details
business_name = input("Enter Business Name: ")
business_type = input("Enter Business Type (e.g., bakery, clothing store): ")
city = input("Enter City: ")
main_customers = input("Enter Main Customers (e.g., students, families): ")

# Converting budget input to an integer for calculations/budgeting
monthly_budget = int(input("Enter Monthly Budget in PKR: "))

# Printing a clear header using formatting separators
print("\n" + "="*50)
print(f"       AI PROMPT KIT FOR: {business_name.upper()}")
print("="*50 + "\n")

# Step 2: Creating customized prompts using f-strings
# Comment: f-strings allow us to dynamically inject business details directly into prompt templates.

prompt_1 = f"Create 3 engaging social media post ideas for '{business_name}', a {business_type} in {city} targeting {main_customers}."

prompt_2 = f"Write a polite, professional reply to a customer who had a bad experience at '{business_name}' ({business_type} in {city})."

prompt_3 = f"Suggest 3 low-cost AI automation tools or ideas for '{business_name}' that fit within a monthly budget of PKR {monthly_budget:,}."

# Step 3: Displaying generated prompts with clean formatting
# Comment: Clean visual separators make the generated output readable and easy to copy.

print("--- PROMPT 1: Marketing (Social Media Post) ---")
print(prompt_1)
print("\n" + "-"*50 + "\n")

print("--- PROMPT 2: Customer Service (Replying to Unhappy Customer) ---")
print(prompt_2)
print("\n" + "-"*50 + "\n")

print("--- PROMPT 3: Growth (Low-Cost AI Ideas) ---")
print(prompt_3)
print("\n" + "="*50)