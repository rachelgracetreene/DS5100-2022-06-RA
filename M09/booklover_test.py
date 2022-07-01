import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        booklover1 = BookLover('Rachel', 'myemail@email.com', 'mystery')
        booklover1.add_book('Harry Potter', 5)
        actual = booklover1.book_list.to_dict()
        
        expected = {'book_name':{0: 'Harry Potter'}, 'book_rating':{0: 5}}
        self.assertEqual(actual, expected)
        
    def test_2_add_book(self):
        booklover2 = BookLover('Eve', 'eve@email.com', 'mystery')
        booklover2.add_book('Harry Potter', 5)
        booklover2.add_book('Harry Potter', 5)
        actual = booklover2.book_list.to_dict()
        
        expected  = {'book_name':{0: 'Harry Potter'}, 'book_rating':{0: 5}}
        self.assertEqual(actual, expected)
        
    def test_3_has_read(self):
        booklover3 = BookLover('Josh', 'josh@email.com', 'mystery')
        booklover3.add_book('Harry Potter', 5)
        actual = booklover3.has_read('Harry Potter')
        
        expected = True
        
        self.assertEqual(actual, expected)
    
    def test_4_has_read(self):
        booklover4 = BookLover('Neil', 'neil@email.com', 'mystery')
        expression = booklover4.has_read('Harry Potter')
        
        self.assertFalse(expression)
        
    def test_5_num_books_read(self):
        booklover5 = BookLover('Matt', 'matt@email.com', 'mystery')
        booklover5.add_book('Harry Potter', 5)
        booklover5.add_book('War and Peace', 3)
        booklover5.add_book('Les Miserables', 2)
        
        actual = booklover5.num_books_read()
        expected = 3
        
        self.assertEqual(actual, expected)
        
    def test_6_fav_books(self):
        booklover6 = BookLover('Connor', 'connor@email.com', 'mystery')
        booklover6.add_book('Harry Potter', 5)
        booklover6.add_book('War and Peace', 3)
        booklover6.add_book('Les Miserables', 2)
        booklover6.add_book('A Tale of Two Cities', 4)
        booklover6.add_book('Percy Jackson', 5)
        
        new_df = booklover6.fav_books()
        
        actual = new_df[new_df.book_rating > 3].to_dict()
        
        expected = {'book_name':{0: 'Harry Potter', 3: 'A Tale of Two Cities', 4: 'Percy Jackson'},
                    'book_rating':{0: 5, 3: 4, 4: 5}}
        
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)