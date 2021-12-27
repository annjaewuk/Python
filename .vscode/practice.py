age = 4;
is_adult =  age >= 3;

print (is_adult);
print (age);

languages = ['python', 'perl', 'c', 'java', 'c#']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")
