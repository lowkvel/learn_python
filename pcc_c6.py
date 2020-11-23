# dict

# initialization
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

# adding kv pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# delete kv pair
del alien_0['points']
print(alien_0)

# get
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# loop for items, keys, values
for k, v in alien_0.items():
    print(k, ":", v)
for k in alien_0.keys():
    print(k)
for v in alien_0.values():
    print(v)

