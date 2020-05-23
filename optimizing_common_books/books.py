import time
import pandas as pd
import numpy as np

# find the common book ids in books_published_last_two_years.txt and 
# all_coding_books.txt to obtain a list of recent coding books.

with open('books_published_last_two_years.txt') as f:
    recent_books = f.read().split('\n')
    
with open('all_coding_books.txt') as f:
    coding_books = f.read().split('\n')

start = time.time()
recent_coding_books = []

for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)

print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

# Use numpy's `intersect1d` method to get the intersection of the `recent_books` and `coding_books` arrays.

start = time.time()
recent_coding_books = np.intersect1d(coding_books, recent_books) # TODO: compute intersection of lists
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

# Use the set's intersection method to get the common elements in recent_books and coding_books.

start = time.time()
recent_coding_books = coding_books.intersection() # TODO: compute intersection of lists
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))