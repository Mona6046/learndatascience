# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pyclustering.cluster.kmeans import kmeans
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
import random
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer
from pyclustering.cluster import silhouette
#from pyclustering.utils import read_sample
# Load list of points for cluster analysis.
#sample = read_sample(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS)
def read_sample(filename):
    """!
    @brief Returns data sample from simple text file.
    @details This function should be used for text file with following format:
    @code
    point_1_coord_1 point_1_coord_2 ... point_1_coord_n
    point_2_coord_1 point_2_coord_2 ... point_2_coord_n
    ... ...
    @endcode
    
    @param[in] filename (string): Path to file with data.
    
    @return (list) Points where each point represented by list of coordinates.
    
    """
    
    file = open(filename, 'r')

    sample = [[int(val) for val in line.split(",")] for line in file if len(line.strip(",")) > 0]
    
    file.close()
    return sample
filename='C:\GE\Box Sync\study\monadata\monadata\Data2.csv' 
sample=read_sample(filename)
# Prepare initial centers using K-Means++ method.
def main_fun():
	initial_centers = kmeans_plusplus_initializer(sample, 2).initialize()
	# Create instance of K-Means algorithm with prepared centers.
	kmeans_instance = kmeans(sample, initial_centers)
	# Run cluster analysis and obtain results.
	kmeans_instance.process()
	clusters = kmeans_instance.get_clusters()
	final_centers = kmeans_instance.get_centers()

	tolerance = 10
	cluster_ids = random.sample(range(0, len(sample)), 2)
	# Create instance of K-Medoids algorithm.
	kmedoids_instance = kmedoids(sample, cluster_ids,tolerance=tolerance, ccore=True)
	# Run cluster analysis and obtain results.
	kmedoids_instance.process()
	clusters1 = kmedoids_instance.get_clusters()
	final_centers1 = kmedoids_instance.get_medoids()
	print('K-Mean Centroids: '+str(final_centers))
	final_center=[]
	final_center.append(sample[final_centers1[0]])
	final_center.append(sample[final_centers1[1]])
	print('K-Medoid Medoid' +str(final_center))


	if (sample[final_centers1[0]][0]>sample[final_centers1[1]][0]):
		c3=clusters1[:1][0]
		c4=clusters1[1:][0]
	else:
		c4=clusters1[:1][0]
		c3=clusters1[1:][0]

	if (final_centers[0][0]>final_centers[1][0]):
		c1=clusters[:1][0]
		c2=clusters[1:][0]
	else:
		c2=clusters[:1][0]
		c1=clusters[1:][0]

	visualizer = cluster_visualizer()
	visualizer.append_cluster(cluster=c1,data=sample,color='red',markersize=8)
	visualizer.append_cluster(cluster=c2,data=sample,color='black',markersize=8)
	visualizer.append_cluster(cluster=c3,data=sample,color='yellow')
	visualizer.append_cluster(cluster=c4,data=sample,color='lime')
	visualizer.append_cluster(cluster=final_centers,marker='*',markersize=10,color='purple')
	visualizer.append_cluster(cluster=final_center,marker='*',markersize=10,color='pink')
	visualizer.set_canvas_title(text='k-mean vs k-medoids')
	visualizer.show(	invisible_axis=False)



	kmeoids_score = silhouette.silhouette(sample, clusters1).process().get_score()
	kmean_score = silhouette.silhouette(sample, clusters).process().get_score()
	print('K-Medoid Score:'+ str(sum(kmeoids_score)))
	print('K-Means Score:'+str(sum( kmean_score)))

for i in range(1,11):
    print(i)
    main_fun()