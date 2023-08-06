from setuptools import setup, find_packages
import codecs
import os


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()



VERSION = '0.0.1'
DESCRIPTION = 'Yolov5 Shape Detector'
# Setting up
setup(
    name="shapedetector",
    version=VERSION,
    author="Mehdi Hosseini Moghadam",
    author_email="<m.h.moghadam1996@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=["numpy",
                      "tqdm"
                      ],
    keywords=['python', 
              'Yolov5',
              'Yolo',
              'Shape Detector',
              'shape object detection', 
],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)










