from io import StringIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import csv
# %matplotlib inline
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import padasip as pa
import glob
import os.path
def lms_algo(file):
    print("LMS ALGO CALLED")
    file_data = file.read().decode("utf-8")
    csv_data = file_data.split("\n")
    df = pd.DataFrame(csv_data)
    df.drop([0],axis=0,inplace=True)
    df = df.astype(int)
    ar = df.values.flatten()

    output_path = r'media/'

    '''folder_path = r'media/'
    file_type = r'\*csv'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime,default = 0)
    print("00000")
    lms_df = pd.read_csv(max_file)
    lms_df.drop("Date", axis=1, inplace=True)'''

    arr_main = ar
    lms_arr0 = arr_main[:1000]/max(arr_main[:])
    lms_arr1 = arr_main[1:]/max(arr_main[:])
    x_test_norm = arr_main[1001:]/max(arr_main[1001:])

    xt_max = max(arr_main[1001:])
    x_test = arr_main[1001:]

    # Implementation

    llim = 0
    ulim = 1000
    step_size = 5
    test_lim= 5
    mu = [0.01,0.05]
    error_mu = []
    plt.figure(figsize=[15,10])
    plt.ylim([0,1])
    for m in mu:
      error = []
      error_mse = []
      f = pa.filters.FilterLMS(n=1, mu=m, w="zeros")
      for k in range(llim, ulim,step_size):
        for i in range(k,k+step_size):
            f.adapt(lms_arr1[i], lms_arr0[i])
        yhat = []
        for i in range(k+test_lim):
            yhat.append(np.dot(f.w,lms_arr0[i]))
        yhat = np.array(yhat)
        error.append(mean_squared_error(lms_arr1[:k+test_lim],yhat)/test_lim)
    error = np.array(error)
    error_mu.append(error)

    fig2 = plt.figure(figsize=(12,6))
    plt.plot(error,label = "mu = {}".format(m),linewidth=3)        
    plt.axis([0,250,0,0.015])
    plt.legend(loc='upper right')
    img_data2 = StringIO()
    fig2.savefig(img_data2,format = 'svg')
    img_data2.seek(0)
    iter = img_data2.getvalue()
   # print("mu = {} completed".format(m))
    
    #iter = "iterations"+str(random.randint(1,10000))+".png"
    #plt.savefig(os.path.join(output_path,iter))
    

    # Using predict function
    y_LMS = []
    for i in range(0,216):
        y_LMS.append(f.predict(x_test_norm[i]))

    ylms = np.dot(y_LMS, xt_max)

    fig1 = plt.figure(figsize=(12,6))
    plt.plot(x_test,'b',label = 'Original Price')
    plt.plot(ylms,'r',label = 'Predicted Price')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.legend()
    #comp = 'comparisons'+str(random.randint(1,10000))+'.jpg'
    #plt.savefig(os.path.join(output_path,comp))

    imgdata = StringIO()
    fig1.savefig(imgdata,format = 'svg')
    imgdata.seek(0)
    comp = imgdata.getvalue()

    
    # Error metrics
    error_mse = mean_squared_error(x_test,ylms)
    error_mae = mean_absolute_error(x_test,ylms)
    error_r2 = r2_score(x_test,ylms)
    print("working")
    print("Errors:")
    print(error_mse)
    print(error_mae)
    print(error_r2)
    return error_mse,error_mae,error_r2,iter,comp

'''def output(file):
    file_data = file.read().decode("utf-8")
    csv_data = file_data.split("\n")
    df = pd.DataFrame(csv_data)
    df.drop([0],axis=0,inplace=True)
    df = df.astype(int)
    ar = df.values.flatten()
    lms_algo(ar)
    return '''

 

