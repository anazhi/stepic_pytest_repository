import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
button = None

def test_find_product (browser):
	browser.get(link)
	time.sleep(5)
	assert browser.find_elements_by_css_selector("button.btn-add-to-basket"), "There is no 'Add to cart button'"