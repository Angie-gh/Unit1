
"""
Assignment:  How Many Trees?
Write a Python program that computes your estimate of the number of trees in
Sacramento.  Be sure to use #comments to describe your computations and
appropriate/good variable names.

Our results are based upon using "Google Satellite" to view a random
500 sq ft parcel from within the Sacramento city limits.
We counted the trees in this parcel and made an assumption that this parcel
contained an average of the other 500 sq ft parcels within the city limits.
"""

#Our unit of measure within Google Satellite for the tree sampling.
unitMeasuredInSqFt = 500

#Quantity of trees we visually counted within one sample unit in Google Satellite.
treesPerUnit = 6

#Visual estimated percentage of city that is open fields or rivers
PercentOpenFields_Rivers = 85

#The total square miles of the city of Sacramento (actual 100.1)
SacSqMiles =  100

#Calculating an estimate of trees that would be in a single square foot 
treesPerOneSqFt = treesPerUnit / unitMeasuredInSqFt

#Calculating estimate of trees in a square mile where 1 sq mile = 27,878,400 sq feet
treesPerSqMile = treesPerOneSqFt * 27878400

#Calculating estimate of total count of trees based on Sacramento = 100 sq miles
#Adjusting estimate based on visual observation of open fields and rivers
treesInSac = int(treesPerSqMile * ((100-PercentOpenFields_Rivers)/100)*SacSqMiles)

print ("Average number of trees in Sacramento:", format(treesInSac,",d"))

