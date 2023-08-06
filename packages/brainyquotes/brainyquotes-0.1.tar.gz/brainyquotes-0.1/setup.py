from distutils.core import setup
setup(
  name = 'brainyquotes',         
  packages = ['brainyquotes'],   
  version = '0.1',      
  license='MIT',       
  description = 'Small scrappers to pull quotes from brainyquotes.com',   
  author = 'Andrew Weatherman',                   
  author_email = 'taw38@duke.edu',     
  url = 'https://github.com/andreweatherman/brainyquotes', 
  download_url = 'https://github.com/andreweatherman/brainyquotes/archive/v_01.tar.gz', 
  keywords = ['quotes', 'scraping', 'small'],  
  install_requires=[            
          'requests',
          'bs4',
          'lxml'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',         
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10'
  ],
)