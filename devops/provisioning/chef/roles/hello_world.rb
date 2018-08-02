name :hello_world
description "A basic role"

run_list(
  'recipe[roivant::python]',
  'recipe[hello_world::hello]',
)
