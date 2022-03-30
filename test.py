#import scanpy as sc
import pandas as pd
import re

file = "./GSE123782_corr_HSV1GSE123782_scRNA_rawcounts_allcells.txt.gz"
columns_to_pick = [0,1,2]+list(range(3099,54622, 1))
df = pd.read_csv(file, sep='\t', nrows=10, usecols=columns_to_pick)
print(df.index.values)
print(df.head())
anti_cluster_columns = []
counter = 0
print(df.columns)
print(df.columns.size)
for col in df.columns:
	# print(col)
	if "cluster" in col:
		anti_cluster_columns.append(col)
		counter+=1
print(counter)
print(df.columns.unique().size)

# df.drop(anti_cluster_columns, axis=1, inplace=True)
#
# for col in df.columns:
# 	print(col)
# regex = ".*_br[4,5]_.*"
# df[df['cell_id'].str.match(regex)== True]