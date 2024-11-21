###PCA PLOT - TEMP

##PCA
# Perform PCA on taxonomy subset
pca = PCA(n_components=2)
pca.fit(kaiju_subset_df)
print(pca.explained_variance_ratio_)

# Convert the "Temp" column to a sequence of floats
color_temp = df["Temp"].astype(float).tolist() 

#transform PCA
transformed_data = pca.transform(kaiju_subset_df)
x=transformed_data[:,0]
y=transformed_data[:,1]
plt.scatter(x=x, y=y, alpha=1, cmap='coolwarm', c= color_temp, edgecolors='black', linewidths=0.6, vmin= 0, vmax= 100)

#plot the name of specific points
for i in range(len(x)):
    index_value = i
    if index_value == 74 or index_value == 74 or index_value == 74:
        plt.text(x[i]*1.2, y[i]*1.2, list(kaiju_subset_df.index)[i], color="black", fontsize=5, alpha=0.8, horizontalalignment='center', verticalalignment='center', fontweight="bold")

#plt.title('PCA Biplot of Class Level Taxon Abundance')
plt.xlabel('First Principal Component (53.99%)', fontsize=8)
plt.ylabel('Second Principal Component (22.58%)', fontsize=8)

#plot colour bar
cbar = plt.colorbar()
cbar.ax.set_ylabel('Temperature (°C)', rotation=270, fontsize=8)

#set font size of labels on matplotlib plots
plt.rc('font', size=8)
plt.xlim(-40, 100)
plt.ylim(-40, 100)
plt.tick_params(axis='x', labelsize=8)
plt.tick_params(axis='y', labelsize=8)

#save
plt.savefig('PCA_temp.png', bbox_inches='tight', dpi=2000)
plt.show()

##BIPLOT
# Perform PCA on taxonomy subset
pca = PCA(n_components=2)
pca.fit(kaiju_subset_df)
print(pca.explained_variance_ratio_)

#transform PCA
transformed_data = pca.transform(kaiju_subset_df)
xs=transformed_data[:,0]
ys=transformed_data[:,1]
## visualize projections

# 0,1 denote PC1 and PC2; change values for other PCs
xvector = pca.components_[0] # see 'prcomp(my_data)$rotation' in R
yvector = pca.components_[1]    
for i in range(len(xvector)):
  # arrows project features (ie columns from csv) as vectors onto PC axes
    plt.arrow(0, 0, xvector[i]*max(xs), yvector[i]*max(ys),
              color='r', alpha=0.6, width=0.0003, head_width=0.0025)
    index_value = i
    if index_value == 0 or index_value == 1 or index_value == 2 or index_value == 3 or index_value == 4 or index_value == 5:
        plt.text(xvector[i]*max(xs)*1.04, yvector[i]*max(ys)*1.04,
             list(kaiju_subset_df.columns.values)[i], color='black', fontsize=4, alpha=1, fontweight="bold")

for i in range(len(xs)):
    # circles project documents (ie rows from csv) as points onto PC axes
    plt.plot(xs[i], ys[i], 'bo', markeredgecolor='black', markeredgewidth=0.6, alpha=1)
    index_value = i  
    if index_value == -1:
        plt.text(xs[i]*1.2, ys[i]*1.2, list(kaiju_subset_df.index)[i], color="grey", fontsize=3, alpha=0.8, horizontalalignment='right', verticalalignment='bottom', fontweight="bold")      

#plot titles
#plt.title('PCA Biplot of Relative Abundance')
plt.xlabel('First Principal Component (53.99%)', fontsize=8)
plt.ylabel('Second Principal Component (22.58%)', fontsize=8)

#set font size of labels on matplotlib plots
plt.rc('font', size=8)
plt.xlim(-40, 100)
plt.ylim(-40, 100)
plt.tick_params(axis='x', labelsize=8)
plt.tick_params(axis='y', labelsize=8)

#save
plt.savefig('biplot.png', bbox_inches='tight', dpi=2000)
