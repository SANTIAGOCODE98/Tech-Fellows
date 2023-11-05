class MagicalOven:
  
  def __init__(self):
    self.ingredients = []
    self.output = None
   
  def add(self,item):
       self.ingredients.append(item)

  def freeze(self):
        if "water" in self.ingredients and "air" in self.ingredients:
           self.output = "snow"

  def boil(self):
        if "lead" in self.ingredients and "mercury" in self.ingredients:
           self.output = "gold"

  def wait(self,temperature):
        required_ingredients =["chese","dough","tomato"]
        if all(ingredient in self.ingredients for ingredient in required_ingredients):
           if temperature >=100:
              self.output = "pizza"

  def get_output(self):
        return self.output

def make_oven():
  return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()