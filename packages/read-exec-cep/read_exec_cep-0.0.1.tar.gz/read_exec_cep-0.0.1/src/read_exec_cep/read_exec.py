import pyodbc
import pandas as pd


class ReadExecCommands:
    """
    Instantiate a read operation.    
    
    :param readType: The type of read operation.
    :type readType: string
    """
    def __init__(self,connection,query):
        self.connection = connection
        self.query = query
    
    def SqlReadExecCommand(connection,query):
        """
        Execute Sql query and return Panda Dataframe.
        
        :param connection: The Sql connection string to connect.
        :type connection: string
        
        :param query: The query to run.
        :type query: string
        """
        # connect to server
        cnxn = pyodbc.connect(connection)

        #execute sql query 

        cursor = cnxn.cursor()
        df = pd.read_sql(query, cnxn)
        return df

     



