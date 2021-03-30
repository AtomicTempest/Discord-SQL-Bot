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


def connect(database_name):
    return sqlite3.connect(database_name)


def create_table(db_name, file_name):
    conn = connect(db_name)
    data = pd.read_csv(file_name + '.csv', header=[0],)
    data.to_sql(file_name, conn, if_exists='replace', index=False)
    conn.close()


def retrieve_data(db_name, table_name, index_col, index):
    conn = connect(db_name)
    cursor = conn.cursor()
    with cursor.connection:
        cursor.execute('SELECT * FROM ' + table_name + ' WHERE ' + index_col + '=\'' + index + '\'')
    return cursor.fetchone()
    conn.close()

# def add_data(db_name, table_name, data_line):
