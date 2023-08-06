import csv
import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup


class SheetsDownloader:
    """
    Author: Bohdan Salamakha
    email: allen.avanheim@gmail.com
    -------------------------------------------------------------------------------------
    The class is used for downloading the Google Sheet spreadsheets by its link.
    When creating an object, it is necessary to pass the Google Sheet URL to the class.
    Also, as the second optional parameter,
    you can pass the format in which you want to download the spreadsheet.
    Supported formats: 'xlsx', 'ods', 'pdf', 'html', 'csv', 'tsv'.
    -------------------------------------------------------------------------------------
    It's 'download_file' method to download the spreadsheet.
    It's 'get_downloaded_file_name' method to get the name of the downloaded spreadsheet.
    """

    __last_downloaded_file = ''
    __extensions = (
        'xlsx',
        'ods',
        'pdf',
        'html',
        'csv',
        'tsv',
    )

    def __init__(self, sheet_url: str, extension='csv'):
        self.__url = self.__get_valid_url(url=sheet_url)
        self.__sheet_id = self.__get_id(url=self.__url)
        self.__extension = self.__get_extension(extension)
        self.__export_format = f'/export?format={self.__extension}&id='
        self.__download_url = self.__url + self.__export_format + self.__sheet_id

    def __get_extension(self, extension: str) -> str:
        if extension in self.__extensions:
            return 'zip' if extension == 'html' else extension
        else:
            message = f'It\'s impossible to convert this sheet into \'{extension}\' file\n' \
                      f'Use some of the next extensions {self.__extensions}'
            raise TypeError(message)

    @staticmethod
    def __get_name(url: str) -> str:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.find(id='docs-title-input-label-inner').text
        except AttributeError:
            return 'Sheet'

    @staticmethod
    def __get_valid_url(url: str) -> str:
        if not isinstance(url, str):
            raise TypeError('sheet_url must be str type')
        edit_ending = '/edit#gid=0'
        if url.endswith(edit_ending):
            url = url.replace(edit_ending, '')
        return url

    @staticmethod
    def __get_id(url: str) -> str:
        sheet_id = url[url.rfind('/') + 1:]
        if sheet_id == -1:
            raise ValueError(f'{url}\nIt isn\'t a Google Sheets URL')
        return sheet_id

    def get_downloaded_file_name(self) -> str:
        return self.__last_downloaded_file

    def get_extension(self):
        return self.__extension

    def download_file(self, folder_name='sheets') -> None:
        print('Downloading the spreadsheet...')

        if not Path(folder_name).exists():
            Path(folder_name).mkdir()

        filename = self.__get_name(url=self.__url)
        number = 1
        full_filename = Path(folder_name, f'{filename}.{self.__extension}')
        true_filename = full_filename.name

        while Path.is_file(full_filename):
            number += 1
            full_filename = Path(folder_name, f'{filename} ({str(number)}).{self.__extension}')

        self.__last_downloaded_file = full_filename.name

        with open(full_filename, 'wb') as file:
            file.write(requests.get(url=self.__download_url).content)
            print(f'The download of the {true_filename} file is complete')


class CsvParser:
    """
    Author: Bohdan Salamakha
    email: allen.avanheim@gmail.com
    -----------------------------
    The class is used for parsing the Google Sheet spreadsheets by its link.
    It's working exactly for .csv files.
    You can get the data in both list and json formats.
    """

    def __init__(self, url: str):
        self.__sheet = SheetsDownloader(sheet_url=url)
        self.__download_dir = None
        self.__file_abs_path = None

    def __create_download_path(self, path: str):
        project_dir = Path(__file__).resolve().parent
        for path in path.split('\\'):
            project_dir = Path(project_dir, path)
            if not project_dir.exists():
                project_dir.mkdir()
        self.__download_dir = project_dir.__str__()

    def __get_data(self, sheet_type: str) -> list:
        self.download_csv_sheet()
        self.__file_abs_path = Path(self.__download_dir, self.__sheet.get_downloaded_file_name())
        error = f"Invalid sheet_type '{sheet_type}'\n" \
                f"parameter 'sheet_type' can only be (list, json)"
        if sheet_type not in ('list', 'json'):
            self.__delete_files()
            raise TypeError(error)
        with open(self.__file_abs_path, encoding='utf-8') as csvfile:
            csv_list = list(self.__get_output_type(csvfile, sheet_type))
        self.__delete_files()
        print('Data collection completed!')
        return csv_list

    def __delete_files(self):
        os.remove(self.__file_abs_path)
        if not os.listdir(self.__download_dir):
            os.rmdir(self.__download_dir)

    @staticmethod
    def __get_output_type(file, sheet_type):
        output_types = {
            'list': csv.reader(file),
            'json': csv.DictReader(file)
        }
        return output_types.get(sheet_type)

    def get_csv_data(self, sheet_type='list') -> (list, dict):
        return self.__get_data(sheet_type)

    def download_csv_sheet(self, path='csv_files'):
        self.__create_download_path(path)
        self.__sheet.download_file(self.__download_dir)
