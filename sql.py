# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sqlite3
import pandas as pd


def connect(database_name: str):
    """Connects to a database and returns connection object

    :param database_name: Name/Location of database, creates database if it doesn't exist.
    """
    return sqlite3.connect(database_name)


def create_table(db_name: str, file_name: str):
    """Creates a table in a database, will create database if it doesn't exist

    :param db_name: Name/Location of Database to create table in.
    :param file_name: File name of CSV File
    """
    conn = connect(db_name)
    data = pd.read_csv(file_name + '.csv', header=[0],)
    data.to_sql(file_name, conn, if_exists='replace', index=False)
    conn.close()


def retrieve_data(db_name: str, table_name: str, search_col: str, to_search: str):
    """Retrieves data from a table in a database given search parameters

    :param db_name: Name/Location of Database to retrieve from
    :param table_name: Name of Table to retrieve data from
    :param search_col: Column to Search for Data
    :param to_search: information from rows to find
    :return: returns list of rows that match search (rows are tuples)
    :rtype: list
    """
    conn = connect(db_name)
    cursor = conn.cursor()
    with cursor.connection:
        cursor.execute('SELECT * FROM ' + table_name + ' WHERE ' + search_col + '=\'' + to_search + '\'')
    return cursor.fetchall()
    conn.close()
