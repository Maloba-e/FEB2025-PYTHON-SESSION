#dictionary- ordered collection of elements in key-value pair
#key is unique and immutable
#value can be any data type
countries ={
    'USA':input('enter the country:'),
    'UK':'United Kingdom',
    'Australia':'Australia',
    'India':'India',
    'courses':['Mathematics','Science','Physics']
    
}
print(countries)
#accessing element in the dictionary

print(countries['Australia'])
#add element
countries['KEN']= 'Kenya'
print(countries['courses'][0])