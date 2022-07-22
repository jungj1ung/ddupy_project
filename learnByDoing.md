# GIT


## **git 기본 명령어**

* **연결된 원격저장소 확인**
~~~
git remote -v
~~~

* **원격저장소에 있는 프로젝트의 변경사항을 그대로 로컬저장소에 옮겨와 자동으로 병합**
~~~
git pull
~~~
혹은
~~~
git pull origin master
~~~

* **커밋하기**
~~~
git commit -m "메모"
~~~
> 메모를 적어줘야 변경사항을 알수가 있다

* **변경사항 staging이랑 commit 동시에하기**
>add로 stage하고 commit하기 귀찮으니까 한번에
~~~
git commit -am "commit message"
~~~


* **파일 상태확인**
~~~
git status
~~~

* **원격저장소에 push하기**
~~~
git push origin main
~~~
> origin은 원격저장소 main은 branch



## **원격저장소와 내 파일이 다를때 push하려고 하면 오류가 남**

* 동기화하는 방법
~~~
git pull --rebase origin main
~~~

* 강제로 push하는 방법(이건 쓰지 말자)
~~~
git push origin +main
~~~

## **코랩에서 빈폴더가 아닌 폴더 삭제하기**

~~~
import shutil
shutil.rmtree('/content/drive/MyDrive/ddupy_project')
~~~

