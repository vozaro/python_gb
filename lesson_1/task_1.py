a = 3
b = 3.5
c = 'Привет'
print(a, b, c)
a = input('Введите ваше имя - ')
b = int(input('Введите, пожалуйста свой возраст - '))
print(c, a, 'В 2030-ом году Вам будет -', b+9)
b = int(input('Сколько часов Вы играете на своем мобильном телефоне? '))
if b > 2:
    print(a, 'Вы играете слишком много! По возможности сократите своё время работы со смартфоном.')
if b <= 2:
    print('Хорошо! Не увлекайтесь сильно игрой на мобильных устройствах. Это влияет на вашу продуктивность.')
c = input('Введите город, в котором Вы проживаете - ')
print('В скором будущем,', a, c, "станет столицей планетарного масштаба!=)")
