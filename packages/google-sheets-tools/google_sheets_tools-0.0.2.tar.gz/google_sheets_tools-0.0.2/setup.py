# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['google_sheets_tools']
install_requires = \
['bs4>=0.0.1,<0.0.2', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'google-sheets-tools',
    'version': '0.0.2',
    'description': 'The package is used for work with the Google Sheet spreadsheets using their URL.',
    'long_description': "A package for downloading data from Google Sheets with spreadsheet URL.\n\npip install google-sheets-tools - install the module\n\nimport google_sheets_tools - import the module to your project\n\n--------------------------\nclass SheetsDownloader:\n--------------------------\nobj = SheetsDownloader(sheet_url, extension='csv') - create a constructor\n\n- sheet_url - url of the Google sheet\n- extension - extension of the downloaded file ('xlsx', 'ods', 'pdf', 'html', 'csv', 'tsv')\n\nobj.download_file(folder_name='sheets') - download a sheet\n\n- folder_name - to what folder download a spreadsheet; default value='sheets'\n\nget_downloaded_file_name() - get a name of your downloaded spreadsheet\n\nget_extension() - get the extension constructor works with\n\n--------------------------\nclass CsvParser:\n--------------------------\ndownload_csv_sheet(path='csv_files') - download the spreadsheet as a csv file\n\n- path - path to downloaded spreadsheet, can be structural '1\\2\\3'; default value='csv_files'\n\nget_csv_data(sheet_type='list') - returns a data from the csv file\n\n- sheet_type - type of the returned data, can be ('list', 'json'); default value='list'\n",
    'author': 'Bohdan Salamakha',
    'author_email': 'allen.avanheim@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
