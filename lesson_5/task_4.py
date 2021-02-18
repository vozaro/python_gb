with open('task_4.txt', 'r') as file_in:
    text = file_in.read()

text = text.replace('One', 'Один')
text = text.replace('Two', 'Два')
text = text.replace('Three', 'Три')
text = text.replace('Four', 'Четыре')

with open('file_4.1.txt', 'w') as file_out:
    file_out.write(text)
