from setuptools import setup, find_packages

setup(
    name='wallpaper',
    version='0.2.3.dev0',
    description='Generate wallpapers with Pillow and Palettable.',
    long_description=open('README.rst').read() + '\n' +
            open('HISTORY.rst').read(),
    url='https://github.com/mitakas/wallpaper',
    author='Dimitar Dimitrov',
    author_email='admin@mitakas.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        ],
    keywords='wallpaper',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'Pillow',
        'palettable',
        ],
    setup_requires=[
        'pytest-runner',
        ],
    tests_require=[
        'pytest',
        ],
    entry_points={
        'console_scripts': [
            'wallpaper=wallpaper.console_script:create_wallpaper',
            ],
        },
    include_package_data=True,
    zip_safe=False,
)
