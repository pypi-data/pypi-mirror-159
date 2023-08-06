from setuptools import setup

setup(
		name='smapi',
		version='0.0.1',
		description='Fetching and parsing info from Steam Community Market and CSGO Float Apis',
		license='MIT',
		author='Mefgner',
		author_email='mefgner@gmail.com',
		packages=['smapi', 'smapi/data_handlers', 'smapi/info'],
		zip_safe=False
)
