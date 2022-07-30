import numpy as np
import cv2
import utils

FILE_NAME = "trained.npz"

with np.load(FILE_NAME) as data:
    train = data['train']
    train_labels = data['train_labels']
    knn = cv2.ml.KNearest_create()
    knn.train(train,cv2.ml.ROW_SAMPLE, train_labels)

def check(test,train, train_labels):
    ret, result, neighbours, dist = knn.findNearest(test,k=1)
    print(result)
    return result


def get_result(file_name):
    image = cv2.imread(file_name)
    chars = utils.extract_char(image)
    result_string = ""
    for char in chars:
        matched = check(utils.resize20(char[1]),train,train_labels)
        if matched <10:
            print(matched)
            result_string = result_string + str(int(matched))
            continue
        if matched == 10:
            matched= '+'
        elif matched == 11:
            matched ="-"
        elif matched == 12:
            matched ="*"
        result_string = result_string + matched
    return result_string

import requests
import shutil
import time

host =  "http://localhost:10000"
url = '/start'

with requests.session() as s:
    answer = ''
    for i in range(0,100):
        start_time = time.time()
        params = {'ans' : answer}

        response = s.post(host+url,params)
        print('Servuer Return:'+response.text)
        if i ==0:
            returned =response.text
            image_url = host + returned
            url = '/check'
        else:
            returned = response.json()
            image_url = host+returned['url']
        print('problem'+str(i) +":" + image_url)

        response = s.get(image_url,stream=True)
        target_image = './target_images/'+str(i)+'.png'
        with open(target_image,'wb') as out_file:
            shutil.copyfileobj(response.raw,out_file)
        del response

        answer_string = get_result(target_image)
        print('string = '+ answer_string)
        answer_string = utils.remove_first_0(answer_string)
        answer = str(eval(answer_string))
        print('answer:' + answer)
        print("----%s seconds---" %(time.time()-start_time))