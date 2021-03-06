from ork.task import task


@task()
def flour():
    print('Producing flour')
    return 'flour'


@task()
def water():
    print('Producing water')
    return 'water'


@task()
def yeast():
    print('Producing yeast')
    return 'yeast'


@task()
def pepperoni():
    print('Producing pepperoni')
    return 'pepperoni'


@task()
def tomato_sauce():
    print('Producing tomato sauce')
    return 'tomato sauce'


@task()
def cheese():
    print('Producing cheese')
    return 'cheese'


@task()
def prepare_dough(*ingredients):
    print('Preparing dough from {}'.format(', '.join(ingredients)))
    return 'dough'


@task()
def cook_pizza(*ingredients):
    print('Cooking pizza from {}'.format(', '.join(ingredients)))
    return 'pizza'


@task()
def eat(food):
    print('Eating {}'.format(food))


dough = prepare_dough.delay(flour.delay(), water.delay(), yeast.delay())
cooked_pizza = cook_pizza.delay(dough, tomato_sauce.delay(), cheese.delay(),
                                pepperoni.delay())
eat.delay(cooked_pizza)
