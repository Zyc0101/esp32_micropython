import ujson


with open('data.json', 'r') as file:
    json_data = file.read()
    
data = ujson.loads(json_data)#将数据序列化为PY对象
print(data['name'])

data['name']='zyc'
json_data = ujson.dumps(data)#将py数据序列化为json格式

with open('data.json', 'w') as file:
    file.write(json_data)


#程序入口
if __name__=="__main__":

    while True:
        pass
    