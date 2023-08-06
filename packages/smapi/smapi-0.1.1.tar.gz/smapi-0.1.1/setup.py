from setuptools import setup, find_packages
import smapi
setup(
		name='smapi',
		version=smapi.__version__,
		description='Fetching and parsing info from Steam Community Market and CSGO Float Apis',
		long_description=open('README.md', encoding='utf-8').read(),
		long_description_content_type='text/markdown',
		license='MIT',
		author='Mefgner',
		author_email='mefgner@gmail.com',
		url='https://github.com/Mefgner/SteamMarketAPI',
		packages=['smapi', 'smapi/data_handlers', 'smapi/info'],
		install_requires=['requests', 'bs4'],
		zip_safe=False
)
