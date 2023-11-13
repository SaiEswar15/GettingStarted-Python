#sets has vast number of methods to explore 
#lets start one by one 

#create a empty set
sampleSet = set({})

#adding elements into set #can have both int and str
sampleSet.add(10)
sampleSet.add('eswar')

#remove elements from the set
sampleSet.remove('eswar')
sampleSet.pop()

sampleSet = {1,2,3}
sampleSet2 = {1,2,3,4,5,6}

unionSet = sampleSet.union(sampleSet2)
print(unionSet, 'union')

inersectionSet = sampleSet.intersection(sampleSet2)
print(inersectionSet, 'intersection')

subtractionSet = sampleSet.difference(sampleSet2)
print(subtractionSet, 'subtraction 1')

subtractionSet1 = sampleSet2.difference(sampleSet)
print(subtractionSet1, 'subtraction 2')

subtractionSet2 = sampleSet.symmetric_difference(sampleSet2)
print(subtractionSet2, 'subtraction 3')

subsetValid = sampleSet.issubset(sampleSet2)
print(subsetValid, 'subset 1')

subsetValid2 = sampleSet2.issubset(sampleSet)
print(subsetValid2, 'subset 2')

superValid = sampleSet.issuperset(sampleSet2)
print(superValid, 'super 1')

superValid2 = sampleSet2.issuperset(sampleSet)
print(superValid2, 'super 2')

disjointSet = sampleSet.isdisjoint(sampleSet2)
print(disjointSet, 'disjoint')

print(type(sampleSet), 'sample set')
print(sampleSet, 'sample set')

#uptill now they dont effect our original sets sampleSet and sampleSet2

#if we want them to effect we update functionality

'''
sampleSet.update(sampleSet2)
print(sampleSet, 'update')

'''
#similarly we use for all operation done above

'''
sampleSet.intersection_update(sampleSet2)
print(sampleSet, 'intersection update')
'''

'''
sampleSet.difference_update(sampleSet2)
print(sampleSet, 'diff update')
'''

'''
sampleSet2.difference_update(sampleSet)
print(sampleSet2, 'diff update')
'''

sampleSet.symmetric_difference_update(sampleSet2)
print(sampleSet, 'diff synnm update')

#its not good idea to change the sets to true or false 
#better use them in different variables only