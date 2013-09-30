from urllib import urlopen
def get_page(url):
  try:return urlopen(url).read()
  except: return ''
