from setuptools import setup, find_packages


setup(
    name='GSEIM',
    version='1.4',
    # license='MIT',
    # author="varun thakore",
    # author_email='vrnthakore@gmail.com',
    packages=find_packages('src'),
    # package_data={'src.grc.gui': ['icon.png']},
    package_dir={'': 'src'},
    # url='https://github.com/vrnthakore/gseim',
    data_files=[('lib/python3.8/site-packages/grc/gui',['src/grc/gui/icon.png']),
                ('lib/python3.8/site-packages/grc/core',['src/grc/core/default_flow_graph.grc'])
        ],
    keywords='gseim',
    install_requires=[
          'numpy',
          'matplotlib',
          'psutil',
          'pyyaml'
      ],
)
