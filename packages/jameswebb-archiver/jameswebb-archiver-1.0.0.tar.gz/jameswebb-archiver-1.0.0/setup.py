# setup.py

import setuptools

setuptools.setup(name='jameswebb-archiver',
      version='1.0.0',
      description='Archives James Webb Telescope\'s Near Infrared Camera (NIRCam) Images including metdata',
      author='Yair Mizrahi',
      url='https://github.com/uraid/jameswebb_archiver',
      package_dir = {"": "src"},
      packages = setuptools.find_packages(where="src"),
      classifiers = [
	    "License :: OSI Approved :: MIT License",
	    "Programming Language :: Python",
	    "Programming Language :: Python :: 3",
	],
	entry_points={
        "console_scripts": [
            "jameswebb-archiver=jameswebb_archiver.__main__:main",
        ]
     }

)