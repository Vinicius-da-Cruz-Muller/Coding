# You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.

# Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
# Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
# Spaces and punctuation are counted as engraved units.
# Write a function cost_of_project() that takes two arguments:

# engraving - a Python string with the text of the engraving
# solid_gold - a Boolean that indicates whether the ring is solid gold

def cost_of_project(engraving, solid_gold):
    cost = 50 + (7 * len(engraving)) + (50 * solid_gold) + (3 * solid_gold * len(engraving))
    return cost

#Solução do Kaggle:
def cost_of_projectb(engraving, solid_gold):
    costb = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return costb