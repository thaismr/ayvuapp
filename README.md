# Ayvuapp

## Project setup

### Custom users app:

[Docs: startapp](https://docs.djangoproject.com/en/4.0/ref/django-admin/#startapp)

````shell
py manage.py startapp ayvuapp.users ./ayvuapp/users
````

### Style formatting

<https://github.com/google/yapf/>

```shell
yapf -r -i . --style google
```

### Pycharm shortcuts

Select all occurrences: Shift + Ctrl + Alt + J 

Toggle column selection mode: Alt + Shift + Insert

## Project Roadmap

### Pre MVP 1.0 (Team prototype)

- [x] Rename Materials as Resources
- [x] List Resources and Vocabularies
- [x] Language options list
- [x] Site text
- [x] Layout polishing
- [ ] Auto-complete fields

### MVP 1.0 (Research phase)

- [ ] Implement authorization
- [ ] Social login integration
- [ ] User profile pages and forms
- [ ] Vocabulary memorization activity V0

### Future features

- [ ] Embedded videos
- [ ] Media upload (images, audio)
- [ ] Diversified and gamified activities
- [ ] Badges and achievements
- [ ] Resources and Vocabularies provided by project team


## Python Useful

### Shell

```shell
pip freeze

pip install -r requirements.txt --upgrade

py manage.py runserver
```