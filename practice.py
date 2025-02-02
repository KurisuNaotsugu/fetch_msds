
import requests
from bs4 import BeautifulSoup


res = requests.get('https://www.orangepage.net/insite_search_results?q=%E3%81%AB%E3%82%93%E3%81%98%E3%82%93#gsc.tab=0&gsc.q=%E3%81%AB%E3%82%93%E3%81%98%E3%82%93&gsc.page=1') # html取得


soup = BeautifulSoup(res.text, 'html.parser') # パース

recipes = soup.find('div', id= 'recipe_list',class_='reciesList')
p_tit_tags = recipes.find_all('p', class_='tit')
p_tit_str = [x.string for x in p_tit_tags]
print(p_tit_str)

'''
h2_tags = soup.find_all('h2')
h2_strings = [x.string for x in h2_tags]
print(h2_strings)

#tag_obj = soup.タグ名 # タグ名の取得
# tag_obj = soup.title
# text = tag_obj.string # テキストの取得

# print(text)
'''