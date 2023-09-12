# Data to be Compresssed
import pickle
import bz2

movie = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

ofile = bz2.BZ2File("movie_binary",'wb')
pickle.dump(movie,ofile)
ofile.close()
 
ofile = bz2.BZ2File("similarity_binary",'wb')
pickle.dump(similarity,ofile)
ofile.close()