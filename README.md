# NevermoreCompile
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/edf91b9620424cb9bd320449b735abe6)](https://app.codacy.com/gh/NevermoreKatana/NevermoreCompile/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
# Install
```make
make install
````

# Usage
``` make compile ``` - исполняет команду ```python compiler.py -f input.txt``` исходный код берется из input.txt, всё выходные файлы сохраняются в output_files, вывод происходит в консколь

# Грамматика и синтаксис

### Вход в программу - функция main 
```
void main(){
    ...
};
```

## Объявление переменных
### Может принимать в названии буквы русского-английского алфавита, заглавные и строчные буквы + цифра. Цифра должна стоять последней в названии переменной!

````
type ID = Число|Дробь|Другая переменная;
````
type может принимать значения только int и double.

example:
````
int x = 15;
````
````
double y = 15.15;
````
### Глобальные переменные(должны указывать в самом начале программы)

```
global: type:ID;
```
```
example:
global: int:y
    int:x;
```


## Математические действия(выполняются в математическом порядке)
example:
````
int x = 15+15;
````
````
int x = 2;
int y = x*15;
````
````
double z = 15.3 * 2;
````

## Вывод поддерживает только переменные|числа|дроби
example:
```
int z = 15;
print(z);
````
````
print(1);
print(2.3);
````

## Операторы сравнения 
example:
````
> < != ==
````

## Цикл For
example:
```
for (int i=0; i<10; i++){
  print(123);
};
```

## Цикл while/doWhile (Левая переменная автоматически инкрементируется)
example:
````
int x = 0;
int y = 15;
while(x<y){
print(15);
};
````
````
int x =0;
int y = 5;
do {
print(15);
}
while (x<y);
````
## Условные операторы if|ifelse. Можно сравнивать дроби и целые числа.
example:
````
if 1>2{
print(15);
};
````
````
if 1>2{
print(15);
}
else{
print(25);
};
````
````
int x =1;
int y =2;
if x>y{
print(15);
}
else{
print(25);
};
````
````
int x =1;
int y =2;
if x>y{
print(15);
};
````

### Создание функций. Функции int и void
example:
```
void `name` (){
    ...
};
int `name` (){
    ...
};
int `name`(int x, double y){
    ...
};

void second(){};
example:
```
### Вызов функции 
```
call `type` `name`();

call void second();

call int second();
call int second(2, 3);
Если переменный объявлены 
call int second(x,y);
```

### Оператор возвращения значения
```
return ID|int
```
example:
```
return x

return 123;
```
### Комментарии
```
// `comment`
//Данная функция прибавляет 1 к x
```

### Пример программы 
```
global: int:x;
void main(){
  int i = 0;
  int z = 2;
  int c = 10;
  int x = 1;
    void plus(){
      int x = x+1;
    };
    void mult(){
      int x = x*10;
    };

  while (i < c){
    if i < z {
      call void mult();
    }
    else{
      call void plus();
    };
  print(x);
  };

};
```
