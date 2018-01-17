# ellipsoid-overlap-metric
Commonly, the ellipses formed from the covariance matrix of clusters of data and their associated multivariate Gaussian distribution are used to visualise the difference in classes
of data. The EOM assesses the visual distinction of these ellipses clusters of data to help automate the process of choosing visualisations without rendering when using covariance ellipses. 

Stochastic feature reduction methods such as t-Distributed Stochastic Neighbour Embedding (TSNE) can sometimes take multiple re-runs to arrive at an instructive visualisation due to their random nature. Ideally, there should be a numerical measure that assesses the visual distinction of these ellipses to help automate the process of choosing visualisations without rendering. This problem is what the Ellipsoid Overlap Metric (EOM) aims to address. It measures the area of overlap between ellipses formed using the covariance matrices of clusters of data-points in 2D. This area reflects how closely mixed two clusters are and hence how visually useful the plot is.

Pretend your goal is to visualise two distinct clusters of data. Visualisation techniques, such as t-Distributed Stochastic Neighbour Embedding (tSNE) use stochastic processes to reduce the feature dimensions in order to visualise the data. This does mean, however, that sometimes the visualisation is poor because of the inherent randomness of the pro- cess. This results in multiple runs of the process to find a suitable visualisation. Ideally, to aid automation of the process, it would be useful if we had a metric which measured how visually distinct two clusters of data are so that, ahead of time, we could say how useful a visualisation is going to be.

Commonly, scientists use the covariance matrix of clusters of data after dimension reduction to reflect the spread of their data in a visualisation. We can visualise this 2D covariance matrix as an ellipse in the 2D space.

We can model the data using a 2D Gaussian distribution on the mean of the cluster with the covariance matrix of the points. If we randomly draw a sample from this distribution, that sample has 95% chance of falling in the 95% confidence level ellipse.

The eigenvectors of the covariance matrix can be calculated and used to form the ellipse that represents the data. The eigenvectors will be orthogonal and will point along the axes of the ellipse.

So for an EOM of 0.9, the ellipses are very closely overlapping, indicative of a poor visualisation. An EOM score of 0.0 means the ellipses are not overlapping at all, so the clusters are visually distinct. This does all of course depend of your confidence level chosen.

## Example Use
Pretend you have two 2D NumPy arrays, A and B, representing clusters of data. The following code will output out the EOM score:
```python
from ellipsoid_overlap_metric import score as eom
print(eom(A,B))
```

Free free to submit pull requests or clone the package if you want.
The Python package is also live on PyPi and can be installed from the command line with:
pip install ellipsoid_overlap_metric.

Any resemblance this method has to existing methods is coincidental and unintended, those existing methods are likely to be more instructive and well-tested than the ellip- soid_overlap_metric currently is. Furthermore, I am not aware of any current methods that implement this feature in software packages, especially Python, but I do acknowledge that they might already exist.
