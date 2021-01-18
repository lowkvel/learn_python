from setuptools import setup, find_packages

setup(
    name='typeidea',
    version='v0.1',
    description='Blog System based on Django',
    author='cy2333',
    author_email='test@test.com',
    url='www.test.com',
    license='MIT',

    packages=find_packages('typeidea'),
    package_dir={'':'typeidea'},
    include_package_data=True,      # used with MANIFEST.in

    install_requires=['diango~=3.1.4', ],
    extras_require={'ipython': ['ipython==6.2.1']},
    scripts=['typeidea/manage.py'],
    entry_points={'console_scripts': ['typeidea_manage = manage:main'], }, 

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Licence :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7.6',
    ],
)
