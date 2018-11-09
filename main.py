import pandas as pd
import os
import time


class ReadFileRealTime():

    def read_file(self, path):
        df = pd.read_csv(path, sep=";")
        print("Leitura: " + path)
        ###Chamar as próximas functions
        return True

    def drop_file(self, path):
        os.remove(path)
        print("DROP: " + path)
        return True

    def search_files_in_path(self, path):
        for filename in os.listdir(path):
            if len(os.listdir(path)) >= 1:
                path1 = path + "\\" + str(os.path.join(filename))
                print(os.path.join(filename))
                time.sleep(5)
                if self.read_file(path1):
                    self.drop_file(path1)

    def execute(self, path):
        while True:
            self.search_files_in_path(path)


execute = ReadFileRealTime()
path = ##informar o path
execute.execute(path)
