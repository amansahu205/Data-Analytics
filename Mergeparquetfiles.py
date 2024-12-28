class Mergeparquetfiles:
  def __init__(self,directory,folder):
    self.directory = directory
    self.directory = folder

  @execution_time
  def merge_parquet_files_pd_np(self):
    print(f"{self.directory}")
    parquet_files = glob.glob(os.path.join(self.directory,'*.parquet'))
    print(f"{parquet_files}")
    merged_df = pd.DataFrame()
    count = 0
    for file in parquet_files:
      df = pd.read_parquet(file)
      merged_df = pd.concat([merged_df,df],index = False)
      count += 1
      print(f"{count} files merged")
    return merged_df

    pass
  @execution_time
  def merge_parquet_files_pd_pa(self):
    pass
  @execution_time
  def merge_parquet_files_pl_pa_cpu(self):
    pass
  @execution_time
  def merge_parquet_files_pl_pa_gpu(self):
    pass
  def merge_parquet_files_cudf_pa(self):
    parquet_files = glob.glob(os.path.join(self.directory,'*.parquet'))
    merged_df = cudf.DataFrame()
    count = 0
    for file in parquet_files:
      df = cudf.read_parquet(file)
      merged_df = cudf.concat([merged_df,df],index = False)
    return merged_df

