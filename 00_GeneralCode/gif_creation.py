import imageio
filenames = ['you.jpg']
images = []
images.append(imageio.imread(filenames))
imageio.mimsave('movie.gif', images, 'GIF', duration = 1)