import urllib2
import urllib
import json
import apikey
key=apikey.key 

def get_isbn(title):
 global key
 data={'q':'intitle:'+title,'key':key}
 enc_data= urllib.urlencode(data)
 query="https://www.googleapis.com/books/v1/volumes"
 info=json.loads(urllib2.urlopen(query+"?"+enc_data).read())
 book= info['items'][0]
 identifiers = book['volumeInfo']['industryIdentifiers']
 isbn=None
 if(book['accessInfo']['embeddable']==False):
  print "not embeddable"
  exit()
 for id in identifiers:
  if(id['type']=='ISBN_10'):
   isbn=id['identifier'] 
 return isbn

if(__name__=='__main__'):
 import sys
 print get_isbn(sys.argv[1])
