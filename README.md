# ellipsoid-overlap-metric
Ellipsoid Overlap Metric measures the area of overlap between covariance ellipses of two 2d data clusters.

The package takes two 2d arrays of data and forms covariance ellipses of the clusters.
Then it measures the overlap of the ellipses asa fraction of the area of he smaller ellipse.
This provides a visual measure of how mixed two clusters of data are so that stochastic feature reduction methods can be optimised over multiple runs.

