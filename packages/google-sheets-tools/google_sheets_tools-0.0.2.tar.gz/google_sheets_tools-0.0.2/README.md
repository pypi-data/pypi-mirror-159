A package for downloading data from Google Sheets with spreadsheet URL.

pip install google-sheets-tools - install the module

import google_sheets_tools - import the module to your project

--------------------------
class SheetsDownloader:
--------------------------
obj = SheetsDownloader(sheet_url, extension='csv') - create a constructor

- sheet_url - url of the Google sheet
- extension - extension of the downloaded file ('xlsx', 'ods', 'pdf', 'html', 'csv', 'tsv')

obj.download_file(folder_name='sheets') - download a sheet

- folder_name - to what folder download a spreadsheet; default value='sheets'

get_downloaded_file_name() - get a name of your downloaded spreadsheet

get_extension() - get the extension constructor works with

--------------------------
class CsvParser:
--------------------------
download_csv_sheet(path='csv_files') - download the spreadsheet as a csv file

- path - path to downloaded spreadsheet, can be structural '1\2\3'; default value='csv_files'

get_csv_data(sheet_type='list') - returns a data from the csv file

- sheet_type - type of the returned data, can be ('list', 'json'); default value='list'
