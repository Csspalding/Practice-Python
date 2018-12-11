text="a spoonfull of sugar, sugar"
word="sugar"

def censor (text, word):
	text.find(word)
		for ch in word:
   		ch ="*"
	t = text
  return t        

def product(product_lst):
  results_product = 0
  for element in product_lst:
    if (element >= 0 and element > (len(product_lst)-1):
      results_product = element * product_lst[element+1]
            
  return results_product

prod_list = [4,5,5]
print(product(prod_list))