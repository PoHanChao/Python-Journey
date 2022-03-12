#讀取檔案food.txt
with open('food.txt', 'r') as f:  
	for line in f:
		print(line)
#with是python獨特的功能，在離開with的架構時會自動關閉檔案
#open打開檔案/ food.txt是檔案名/ r代表read讀取模式，
#也有write(w)寫入模式
#"as f" 當作f，f可以隨便取，是一種簡稱。整個檔案簡稱為"f"
#用for loop讀取f，line是一個自己的取名，代表每一行

data=[]
with open('food.txt', 'r') as f:  
	for line in f:
		data.append(line.strip())  #strip去掉換行符號(\n)和多餘的空格
print(data)