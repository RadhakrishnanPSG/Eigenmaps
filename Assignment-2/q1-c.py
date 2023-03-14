import tensorflow
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.utils import to_categorical

def test():
    #loading the dataset
    (x_train,y_train),(x_test,y_test) = mnist.load_data()
    
    #data reshaping and categorization
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    
    
    #Architecture
    model = Sequential()
    model.add(Conv2D(32,kernel_size=(3, 3),activation='relu',input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64,kernel_size=(3, 3),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128,activation='relu'))
    model.add(Dense(10,activation='softmax'))
    
    
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    
    model.fit(x_train,y_train,batch_size=128,epochs=20,validation_data=(x_test,y_test))
    loss,accuracy = model.evaluate(x_test,y_test, verbose=0)
    assert accuracy>0.9
    print("Test accuracy : ",accuracy)
test()