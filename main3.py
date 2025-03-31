class India:
    def capital(self):
        return "New Delhi"

    def language(self):
        return "Hindi"

    def type_of_country(self):
        return "Developing Country"

class USA:
    def capital(self):
        return "Washington, D.C."

    def language(self):
        return "English"

    def type_of_country(self):
        return "Developed Country"

# Common interface function using Polymorphism
def display_country_info(country):
    print(f"Capital: {country.capital()}")
    print(f"Language: {country.language()}")
    print(f"Type: {country.type_of_country()}\n")

# Creating objects
india = India()
usa = USA()

# Using the same function for both countries
display_country_info(india)
display_country_info(usa)
