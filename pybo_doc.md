https://wikidocs.net/book/4542



> 1. models.py : 데이터베이스를 처리 
> 2. forms.py : 서버로 전송된 폼을 처리
> 3. views 디렉터리 : 화면을 구성
> 4. static 디렉터리 : css, js, image 파일을 저장
> 5. templates 디렉터리 : html 파일을 저장
> 6. config.py : 환경설정, 데이터베이스 등의 프로젝트를 설정 



Flask 설치

```bash
pip install Flask
```



Flask-Migrate 설치

> Flask-Migrate 라이브러리를 설치하면 SQLAlchemy 도 함께 설치 된다.

```bash
pip install Flask-Migrate
```



##### Application Factory 사용

> 애플리케이션 팩토리는 쉽게 말해 app 객체를 생성하는 함수를 의미
>
> `__init__.py` 파일을 만들고 `create_app` 함수를 선언.



##### Blueprint 로 라우트 함수 관리

> 라우트 함수를 구조적으로 관리
>
> `views` 폴더 생성 > `main_views.py` 생성



##### ORM 적용

> SQLAlchemy 사용
>
> `/`루트 디렉토리에 `config.py` 생성
>
> `__init__.py` 파일에 SQLAlchemy 를 적용



##### 데이터베이스 초기화 하기

> `flask db init`
>
> ```bash
> (pybo_env) d:\GoogleDrive\Dev\python\pybo_project> flask db init
> ```
>
> 
>
> 이 명령은 DB 를 관리하는 초기 파일들을 `migrations` 라는 디렉터리에 자동으로 생성해 준다.
>
> 이때 생성되는 파일들은 `Flask-Migrate` 라이브러리에서 사용된다.
>
> 데이터베이스를 초기화 하는 `flask db init` 명령은 최초 한 번만 수행하면 된다.



##### 데이터베이스 관리 명령어 정리

> - flask db migrate : 모델을 새로 생성하거나 변경할 때 사용
> - flask db upgrade : 모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용