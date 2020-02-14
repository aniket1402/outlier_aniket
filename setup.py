from distutils.core import setup
setup(
  name = 'outlier_aniket',
  packages = ['outlier_aniket'],
  version = '0.4',
  license='MIT',
  description = 'Outlier Removal using Z-score or IQR',
  author = 'Aniket Gupta',
  author_email = 'aniketgupta1495@gmail.com',
  url = 'https://github.com/aniket1402/outlier_aniket.git',
  download_url = 'https://github.com/aniket1402/outlier_aniket/archive/v_04.tar.gz',
  keywords = ['Outlier Removal', 'Row Removal'],
  install_requires=[
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python >= 3',
  ],
)