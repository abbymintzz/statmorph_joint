import setuptools

setuptools.setup(
    name="statmorph_joint",
    version="1.0",
    author="Abby Mintz",
    author_email="abby.mintz@princeton.edu",
    description="A modified version of statmorph for jointly fitting multiple bands",
   packages=setuptools.find_packages(include=['statmorph_joint','statmorph_joint.*'])

)