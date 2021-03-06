#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 11:15
# @Author  : wendy
# @Usage   : The predict object.Include some useful relative functions
# @File    : Predictions.py
# @Software: PyCharm
import os
import json
from model.Config import Config as C
PREDICT_RESULT_PATH = C().PREDICT_RESULT_PATH

class Predictions(object):
    '''
    Class that deal with predict train_data saving and reading
    '''

    def __init__(self,image_name,type,model_name):
        self.image_name = image_name
        self.result = self.init_prediction_result()
        self.flag = False
        self.type = type
        self.model_name = model_name
        self.save_path = PREDICT_RESULT_PATH+self.image_name+'_'+self.type+'_'+self.model_name+'.json'


    def get_predict_flag(self):
        return self.flag

    def set_predict_flag(self,flag):
        self.flag = flag

    def init_prediction_result(self):
        '''
        Init the whole prediction result dictionary
        :return:
        '''
        prediction_result = {}
        prediction_result['person'] = 0
        prediction_result['motorbike'] = 0
        prediction_result['bicycle'] = 0
        prediction_result['dog'] = 0
        prediction_result['cat'] = 0
        prediction_result['car'] = 0
        prediction_result['bus'] = 0
        return prediction_result

    def type_identify(self,label):
        '''
        Identify each type's count in each image.
        :param label: class type name
        :param prediction_result: the predictions result
        :return: the predictions result
        '''
        if label == 'person' or label == 'motorbike' or label == 'bicycle' \
                or label == 'dog' or label == 'cat' \
                or label == 'car' or label == 'bus':
           self.result[label] += 1
        else:
            print('We don\' consider other type in this program')


    def write_total_predict(self,image_numbers_or_name):

        i=0
        total_predict = {}
        if type(image_numbers_or_name) == str:
            self.save_path = PREDICT_RESULT_PATH + image_numbers_or_name+'_' + self.type + '_' + self.model_name + '.json'
            total_predict[image_numbers_or_name] = self.read_predict_result()
        else:
            while i < image_numbers_or_name:

                self.save_path =  PREDICT_RESULT_PATH+str(i+1)+'.jpg_'+self.type+'_'+self.model_name+'.json'
                single_result = self.read_predict_result()
                total_predict[str(i+1)+'.jpg'] = single_result
                i+=1

        self.result = total_predict
        self.save_path = PREDICT_RESULT_PATH + self.type +'_'+ self.model_name+'.json'
        self.write_predict_result('w')


    def write_predict_result(self,mode):
        if not os.path.exists(PREDICT_RESULT_PATH):
            os.makedirs(PREDICT_RESULT_PATH)

        preObj = json.dumps(self.result)

        fileObject = open(self.save_path, mode)
        fileObject.write(preObj)
        fileObject.close()

    def read_predict_result(self):
        with open(self.save_path, 'r') as f:
            result = json.loads(f.read())
        return result







