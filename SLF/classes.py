class Categories:
    def __init__(self):
        self.standard = ["city: ", "country: ", "river: ", "name: ", "animal: ", "job: "]
        self.celeb = ["actor: ", "singer: ", "band: ", "politician: ", "sport-star: "]
        self.nerd = ["video game: ", "superhero: " , "pokemon: ", "TV-Series: ", "internet-site: "]



# ##### was ein Andre erwartet:

# from dataclasses import dataclass

# @dataclass
# class StandardCategory:
#     city: str
#     country: str
#     river: str
#     name: str
#     animal: str
#     job: str


# class CelebCategory:
# ...    


# @dataclass
# class Categories:
#     standard: StandardCategory
#     celeb: Category
#     nerd: Category



# cat_standard = Category()

# cat_standard.values

# # Empfehlung eines Andres:

# categories: dict[str,str] = {
#     'standard': ["city: ", "country: ", "river: ", "name: ", "animal: ", "job: "],
#     'celeb': ["actor: ", "singer: ", "band: ", "politician: ", "sport-star: "],
#     'nerd': ["video game: ", "superhero: " , "pokemon: ", "TV-Series: ", "internet-site: "]
# }

