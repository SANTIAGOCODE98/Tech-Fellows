from question3 import alchemy_combine, make_oven

def test_alchemy_combine():

  assert alchemy_combine(
    make_oven(),
    ["lead", "mercury"],5000
  ) == "gold"

  assert alchemy_combine(
    make_oven(),
    ["water", "air"],
    -100
  ) == "snow"

  def freeze(self):
    if "water" in self.ingredients and "air" in self.ingredients:
      self.output = "snow"