# 딕셔너리 자료형(순서 x, 키 중복x, 수정 o, 삭제 o)
# key 값은 어떤 자료형이든 상관 없음.
# value 값도 어떤 자료형이든 상관 없음
# initialize
a = {'name' : 'Kim', 'phone' : '01012345678', 'birth' : '123456'}
b = {0 : 'Hell Python'}
c = {0:123}
d = {'arr' : [1,2,3]}
e = {
    'name' : 'Kim',
    'phone' : '01012345678',
    'birth' : '123456',
}
f = dict(
    name = 'Kim',
    phone = '01012345678',
    Birth = '123456',
)
print(c)
print(e)
print(f)
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)




# print
print(a['name'])
print(a.get('name'))
print(e.get('name'))
# print(a['01012345678'])
# 일반 속성값 입력 : key가 없을 시 : KeyError 발생
# print(a['name0'])
# get function : key가 없을 시, None 반환
print(a.get('name0'))

# dictionary add
a['address'] = 'seoul'
print(a)
a['number'] = 1,2,3
print(a)

"""
dictionary function
keys, values, items : 반복문에서 사용 가능
"""
# len function : dictionary 길이 출력
print(len(a))
print(len(b))
print(len(c))
print(len(d))
# keys function : key의 값들만 출력
print(a.keys())
print(b.keys())
print(c.keys())
print(d.keys())
# list(a.keys()) : a dictionary의 key 값들을 list 형태로 불러옴
print(list(a.keys()))
print(list(b.keys()))
# valuew funcfion : value의 값들만 출력
print(a.values())
print(b.values())
print(c.values())
print(d.values())
# list(a.values()) : a dictionary의 value 값들을 list 형태로 불러옴
print(list(a.values()))
print(list(b.values()))
# items function : key, value의 값들을 출력. tuple 형태로 출력
print(a.items())
print(b.items())
print(c.items())
print(list(a.items()))
print(list(b.items()))
"""
pop function(key)
* 해당 key 에 대응하는 value값을 가져옴.
* value 값을 pop 불가(KeyError 발생)
* pop 이후 dictionary print : pop 적용 key, 그에 상응하는 value 제외
"""
print(a.pop('name'))
print(a)
"""
popitem function
* 일반 pop function : 내가 가져올 key 값을 알아야 함.
* popitem : 내가 지정한 dictionary의 임의의 key, value 값을 가져옴
"""
print(a.popitem())
print(a)
print(a.popitem())
print(a)

# in function : key 존재 여부 boolean 형태로 출력
print('birth' in a)
print('arr' in a)

# add & update
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '123456', 'address': 'seoul', 'number': (1, 2, 3)}
a['arr_key'] = 'arr_value'
print(a)
a['name'] = 'Lee'
print(a)
# update function
a.update(name='Park')
print(a)
var1 = {'name':'Song'}
a.update(var1)
print(a)