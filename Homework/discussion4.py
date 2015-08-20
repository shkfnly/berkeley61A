def make_unit(catchphrase, damage):
  return (catchphrase, damage)


def get_catchphrase(unit):
  return unit[0]

def get_damage(unit):
  return unit[1]


def battle(first, second):
  print(get_catchphrase(first))
  print(get_catchphrase(second))
  damage1 = get_damage(first)
  damage2 = get_damage(second)
  if damage2 > damage1:
    return second
  return first

  def make_resource_bundle(minerals, gas):
    return pair(minerals, gas)

  def get_minerals(bundle):
    return getitem_pair(bundle, 0)

  def get_gas(bundle):
    return getitem_pair(bundle, 1)

def make_building(unit, bundle):
  return make_pair(unit, bundle)
def get_unit(building):
  return get_pair(building, 0)
def get_bundle(building):
  return get_pair(building, 1)

def build_unit(building, bundle):
  if get_pair(bundle, 0) < get_pair(get_pair(building, 1,) , 0) || get_pair(bundle, 1) < get_pair(get_pair(building, 1,) , 1)
    print("We require more resources")
    return
  unit = get_unit(building)
  return make_unit(get_catchphrase(unit), get_damage(unit))

def make_resource_bundle(minerals, gas):
  return (minerals, gas)

def get_minerals(bundle):
  return bundle[0]

def get_gas(bundle):
  return bundle[1]

