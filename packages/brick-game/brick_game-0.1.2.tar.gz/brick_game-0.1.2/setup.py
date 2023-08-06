from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
        name='brick_game',
        version='0.1.2',
        packages=find_packages(where="src"),
        url='https://github.com/AstrophysicsAndPython/brick_game',
        license='MIT',
        author='Astrophysics and Python, Syed Ali Mohsin Bukhari',
        author_email='astrophysicsandpython@gmail.com, syedali.b@outlook.com',
        description='An old brick game that I played as a child.',
        long_description=readme,
        long_description_content_type="text/markdown",
        python_requires=">=3.7.*, <3.10.*",
        install_requires=["pygame~=2.1.2", "setuptools~=59.6.0"],
        include_package_data=True,
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9"
            ],
        entry_points={
            "gui_scripts": [
                "brick_game = brick_game.main_file:main"
                ]
            }
        )
