from distutils.core import setup

setup(
    name='devialet',
    packages=['devialet'],
    version='1.5.7',
    license='MIT',
    description='Devialet API',
    long_description_content_type="text/markdown",
    long_description='Devialet API',
    author='fwestenberg',
    author_email='',
    url='https://github.com/fwestenberg/devialet',
    download_url='https://github.com/fwestenberg/devialet/releases/latest',
    keywords=['Devialet', 'Home-Assistant'],
    install_requires=[
        'aiohttp', 'async_upnp_client'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
