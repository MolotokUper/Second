Как создать ssh-ключ
1)Установаить git bash
2)Следовать по порядку по следующим пунктам
	ssh-keygen -t ed25519 -C "zakharov.ra@phystech.edu"
	*соглашаться со всем, что есть предлагает*
	eval $(sh-agent)
	ssh-add .ssh/<имя файла>
Готово
------
Как добавить ключ в аккаунт на GitHub
1) Создать аккаунт на GitHub (имя, nickcname)
2) Перейти в Settings
3) SSH and GPG keys
4) Кнопочка New SSH key.Скопировать текст из файла с расширеним .pub и добавить на сайт.
Готово
------
Как сколнировать репозиторий в папку
0) Выбрать папку, в которую быудем клнировать репрозиторий 
1) В git bash:
	git clone git@github.com:MolotokUper/Second.git
	где  git@github.com:MolotokUper/Second.git копируем с GitHub (заходим на вновь созданный репрозиторий, и выбираем 
	ssh ссылку на репрозиторий)////
------