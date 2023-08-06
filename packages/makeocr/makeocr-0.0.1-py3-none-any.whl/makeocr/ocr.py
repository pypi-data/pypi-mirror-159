import numpy as np
import os
from paddleocr import PaddleOCR
from statistics import mode
import time


def inference(img_path, lang):
    try:
        ocr = PaddleOCR(use_angle_cls=True, lang=lang,use_gpu=True)
        result = ocr.ocr(img_path, cls=True)
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        for i,j in enumerate(scores):       # if scores are lesser then 85 %
            if float(j)>0.70:
                pass
            else:
                scores.pop(i)
                txts.pop(i)
        if len(txts)==0:          #no object detected
            return "Object not found",float(0.0)
        try:                          # most repeating txts
            txts=[mode(txts)]
            scores=[max(scores)]
        except:
            pass       
        if len(txts)>1:           # if both txts are different
            case=np.argmax(scores)
            scores=[scores[case]]
            txts=[txts[case]]
        for i in txts:                    # if txts >20
            if float(i)>=20.0:
                return "could Not process",float(0.0)
        return str(txts[0]),float(scores[0])
    except:
        return "could Not process,exception",float(0.0)
    

'''if __name__ == "__main__":
    txts,scores=inference("img.jpg","en")
    print(txts," ",type(txts)," ",scores," ",type(scores))'''