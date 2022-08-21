import json
from PIL import Image
#토치랑 torchvision 서버구축할때 삭제했다 제대로 된걸로 다시 설치 해야한다.
import torch
from torchvision import transforms

from efficientnet_pytorch import EfficientNet


def executeAImodel(ImgUrl):
    #model = EfficientNet.from_pretrained('efficientnet-b0')




    model_path = "./dupi/AI/trainedAiModel/aram_model5.pt"
    # map_location은 나중에 수정하장
    model = torch.load(model_path, map_location='cpu')

    # Preprocess image
    tfms = transforms.Compose([transforms.Resize(224), transforms.ToTensor(),
                           transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]), ])
    img = tfms(Image.open('.'+ImgUrl)).unsqueeze(0)
    print(img.shape)  # torch.Size([1, 3, 224, 224])

    # Load Image class names
    labels_map = json.load(open('./dupi/AI/labels_map.txt'))
    labels_map = [labels_map[str(i)] for i in range(4)]

    # Classify
    model.eval()
    with torch.no_grad():
        outputs = model(img)

    # # Print predictions
    # print('-----')
    # for idx in torch.topk(outputs, k=1,largest=True).indices.squeeze(0).tolist():
    #     prob = torch.softmax(outputs, dim=1)[0, idx].item()
    #     print('{label:<75} ({p:.2f}%)'.format(label=labels_map[idx], p=prob*100))

    # 여기서부터 테스트
    idx = torch.topk(outputs, k=1, largest=True).indices.squeeze(0)
    res = labels_map[idx]  # string임

    return res


