class Countparquetrows:
  def __init__(self,directory,folder):
    self.directory = directory
    self.folder = folder

  @execution_time
  def count_rows_pd_np(self):
    total_rows = 0
    for file_name in os.listdir(self.directory):
      if file_name.endswith('.parquet'):
        file_path = os.path.join(self.directory, file_name)

        df = pd.read_parquet(file_path)
        total_rows += len(df)
        #print(f"Total number of rows in {file_name} = {len(df)}")
    return f"Total number of rows in {self.folder} dataset = {total_rows}"


  @execution_time
  def count_rows_pd_pa(self):
    total_rows = 0
    for file_name in os.listdir(self.directory):
      if file_name.endswith('.parquet'):
        file_path = os.path.join(self.directory, file_name)
        table = pa.parquet.read_table(file_path)
        total_rows += table.num_rows
        #print(f"Total number of rows in {file_name} = {table.num_rows}")
    return f"Total number of rows in {self.folder} dataset = {total_rows}"

  @execution_time
  def count_rows_pl_pa(self):
    total_rows = 0
    for file_name in os.listdir(self.directory):
      if file_name.endswith('.parquet'):
        file_path = os.path.join(self.directory, file_name)
        df = pl.read_parquet(file_path)
        total_rows += df.shape[0]
        #print(f"Total number of rows in {file_name} = {df.shape[0]}")
    return f"Total number of rows in {self.folder} dataset = {total_rows}"

###
  @execution_time
  def count_rows_pl_pa_gpu(self):
    total_rows = 0
    for file_name in os.listdir(self.directory):
      if file_name.endswith('.parquet'):
        file_path = os.path.join(self.directory, file_name)
        df = pl.scan_parquet(file_path)
        #total_rows += df.
        #print(f"Total number of rows in {file_name} = {df.shape[0]}")
    return f"Total number of rows in {self.folder} dataset = {total_rows}"
###
  @execution_time
  def count_rows_cudf_pa(self):
    total_rows = 0
    for file_name in os.listdir(self.directory):
      if file_name.endswith('.parquet'):
        file_path = os.path.join(self.directory,file_name)
        df = cudf.read_parquet(file_path)
        total_rows += df.shape[0]
        print(f"Total number of rows in {file_name} = {df.shape[0]}")
    return f"Total number of rows in {self.folder} dataset = {total_rows}"

