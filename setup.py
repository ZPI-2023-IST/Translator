import setuptools

setuptools.setup(
    name="Translator FC",
    version="0.0.1",
    author="Patryk, Mateusz, Wiktor, Kamil",
    description="A dedicated translator for Freecell game",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    py_modules=["translator"],
    install_requires=open("requirements.txt").read().splitlines(),
    package_dir={"": "."},
)
