## 폴더 알아보기
>여기에 있는 모든 폴더는 당연히 마음대로 수정하셔도 됩니당 

* **learnByDoing**: 프로젝트를 하면서 배우게 되는 것들 정리해서 적어놓는 파일


* **ai모델(참고공부용)**: aihub에서 다운받아온 ai모델


## 해야할 일 및 알아내야 할 것

>ai모델 관련
* **ai모델을 무엇을 사용할 것인지** ->efficientnet b7 사용

> 응용프로그램에 올라갈거라서 비교적 가벼운 모델이면서 좋은 성능이 필요한데
적은 Parameter 대비 압도적인 성능을 가진 efficientnet 모델 사용


그 중 헬스케어 관련이므로 600의 높은 해상도를 사용하는 모델인 b7 이용할거임 

* **학습후 만들어지는 파일을 가지고 어떻게 이미지 분류를 할 수 있는지 알아내야함**


* **학습시킬때 세팅해야하는 것들에 무엇이 있고 그것들의 값을 몇으로 해야하는지**
- batch_size
- epoch
- loss_function(손실함수)
- 옵티마이저
- 옵티마이저의 매개변수 (초기 학습률learning rate,  momentum, weight_decay 등 과적합을 막을 수 있는 방안)
- learning_rate_scheduler
> 학습과정에서 learning rate를 조정하는 learning rate scheduler를 사용할 수도 있다. 
처음엔 큰 learning rate(보폭)으로 빠르게 optimize를 하고 최적값에 가까워질수록
 learning rate(보폭)를 줄여 미세조정을 하는 것이 학습이 잘된다고 알려져있다.

>응용프로그램 관련
* **어플? 웹프로그램?**
* **무슨 언어를 사용할지**
* **응용프로그램 내에서 카메라 기능, 카메라로 찍은 사진을 ai모델 input으로 보내는 알고리즘 등**
