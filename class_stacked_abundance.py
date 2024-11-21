##STACKED TAXONOMY ABUNDANCE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import pandas as pd 
import numpy as np

mpl.rcParams['figure.dpi'] = 2000

# Specify the column names you want to include in the subset
kaiju_subset_columns = ["Aquificae","Thermoprotei","Alphaproteobacteria","Betaproteobacteria","Gammaproteobacteria","Deltaproteobacteria","Deinococci","Actinobacteria","Clostridia","Bacilli","Acidobacteriia","Blastocatellia","Planctomycetia","Nitrososphaeria","Nitrospira","Chloroflexia","Thermomicrobia","Cytophagia","Flavobacteriia","Gemmatimonadetes","Vicinamibacteria","Thermotogae","Epsilonproteobacteria","Anaerolineae","Bacteroidia","Methanomicrobia","Caldilineae","Halobacteria","Limnochordia","Spirochaetia","Ignavibacteria","Chlorobia","Negativicutes","Rubrobacteria","Thermodesulfobacteria","Thermococci","Ktedonobacteria","Sphingobacteriia","Dehalococcoidia","Calditrichae","Synergistia","Deferribacteres","Archaeoglobi","Ardenticatenia","Nitriliruptoria","Fimbriimonadia","Chitinophagia","Opitutae","Gloeobacteria","Coriobacteriia","Candidatus Brocadiae","Dictyoglomia","Methanobacteria","Methylacidiphilae","Oligoflexia","Thermoleophilia","Tissierellia","Fusobacteriia","Thermoplasmata","Chlamydiia","Saprospiria","Phycisphaerae","Acidimicrobiia","Mollicutes","Acidithiobacillia","Methanococci","Caldisericia","Kiritimatiellae","Erysipelotrichia","Zetaproteobacteria","Chrysiogenetes","Coprothermobacteria","Hydrogenophilalia","Verrucomicrobiae","Spartobacteria","Lentisphaeria","Endomicrobia","Elusimicrobia","Fibrobacteria","Candidatus Babeliae"]

# Subset of DataFrame
kaiju_subset_df = df[kaiju_subset_columns]

# Filter out values below 1%
kaiju_subset_df_1filt = kaiju_subset_df.apply(lambda x: x.mask(x < 1))

# Recalculate the remaining data to make up to 100%
kaiju_subset_df_1filt = kaiju_subset_df_1filt.div(kaiju_subset_df_1filt.sum(axis=1), axis=0) * 100

# Calculate the column sums
column_sums = kaiju_subset_df_1filt.sum()

# Filter out columns with zero sum
non_zero_columns = column_sums[column_sums != 0].index
zero_columns = column_sums[column_sums == 0].index

# Create a new DataFrame with the non-zero columns
filtered_df_1filt = kaiju_subset_df_1filt[non_zero_columns]

# Define colour map and the Set1 and Pastel1 colormaps
tab20_cmap = plt.get_cmap('tab20')
pastel1_cmap = plt.get_cmap('Pastel1')
tab20b_cmap = plt.get_cmap('tab20b')
Dark2_cmap = plt.get_cmap('Dark2')
Set3_cmap = plt.get_cmap('Set3')

# Combine the colormaps
combined_cmap = ListedColormap(np.concatenate((tab20_cmap.colors, tab20b_cmap.colors, Dark2_cmap.colors, Set3_cmap.colors)))

# Reverse the order of colors in the combined_cmap
reversed_combined_cmap = ListedColormap(combined_cmap.colors[::-1])

# Plotting the stacked bar chart 
ax = filtered_df_1filt.iloc[:, ::-1].plot(kind='bar', stacked=True, cmap=reversed_combined_cmap)

# Legend
ax.legend(pd.unique(non_zero_columns)).set_visible(True)

# Adding axis labels

#ax.set_xlabel("SRA Dataset")
ax.set_ylabel("Relative Abundance (%)")
ax.set_ylim([0, 100])

#ax.set_title("Global Relative abundance of Taxa in Geothermal Springs")
ax.tick_params(axis='x', labelsize=5.2)
ax.tick_params(axis='y', labelsize=8)

#reverse legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(reversed(handles), reversed(labels), frameon=False, loc=(1.01 , -0.35), prop={'size': 4})

#Save
plt.savefig('Kaiju_class_filt_1_stacked_abundance_CLASS.png', bbox_inches='tight', dpi=2000)
# Displaying the plot
plt.show()
