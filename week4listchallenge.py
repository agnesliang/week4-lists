# Black-Owned Restaurant Finder: Lists exercises

#Part 1-

cuisines = {'Japanese', 'Korean', 'Italian', 'Mexican', 'Greek', 'Argentenian', 'French'}
cuisine = input ('What cuisine are you interested in?')

if cuisine in cuisines:
    print ('Restaurant found!')
else: 
    print ('Please choose one of these cuisines from this list {cuisines}')

#Part 2

black_owned_restaurants = ['Hard Knox Cafe', 'Bella Trattoria', 'Taqueria Los Mayas']
for i in black_owned_restaurants:
    print(black_owned_restaurants.index(i) +1, end = '')
    print('', i)

distance_from_restaurant = [2, 4, 6]

for i in range(len(distance_from_restaurant)):
    print (i +1, black_owned_restaurants[i]+ 'is' + str(distance_from_restaurant[i])+'Miles Away')
    print (f'{i+1} {black_owned_restaurants[i]} is {str(distance_from_restaurant [i])} Miles Away')