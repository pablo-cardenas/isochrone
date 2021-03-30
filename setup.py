from setuptools import setup, find_packages

setup(
    name="isochrones",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
            'Fiona',
            'Click',
            'scipy',
            'pyproj',
            'shapely',
    ],
    entry_points="""
        [console_scripts]
        isochrones=isochrones.scripts:cli
    """,
)
