import matplotlib.pyplot as plt
import time
import numpy as np

def blank_fig():
    fig = plt.figure()  # an empty figure with no axes
    fig.suptitle('My First Figure')  # Add a title so we know which it is

    fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
    plt.show()

def sample_fig_1():
    x = [1,2,3,4,5,6,7,8]
    y = [0.1,0.2,0.3,0.5,0.6,0.8,0.9,1.3]
    plt.plot(x,y)
    plt.show()

def sample_fig_2():
    x = np.linspace(0, 2, 100)
    print(x) # test numpy linespace function
    plt.plot(x, x, label = 'Linear')
    plt.plot(x, x**2, label = 'Quadratic')
    plt.plot(x, x**3, label = 'Cubic')

    plt.xlabel('x label')
    plt.ylabel('y label')

    plt.title(' Simple Plot')

    plt.legend()

    plt.show()

def np_test():

    x = np.arange(0,10,0.2)  #test numpy arrange function
    print(x)

def fig_sample_3():

    x = np.arange(0, 10, 0.2)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    plt.show()

def my_plotter(ax, data1, data2, param_dict):
    """
        A helper function to make a graph

        Parameters
        ----------
        ax : Axes
            The axes to draw to

        data1 : array
           The x data

        data2 : array
           The y data

        param_dict : dict
           Dictionary of kwargs to pass to ax.plot

        Returns
        -------
        out : list
            list of artists added
        """
    out = ax.plot(data1, data2, **param_dict)
    # plt.show()
    return out

def spec_plotter_ford_white(ax, param_dict):

    datax = [0.355, 0.354, 0.353, 0.351, 0.350 ,0.349 ,0.347 ,0.346 ,0.344 ,0.343 ,0.341 ,0.339 ,0.338 ,0.336 ,0.334 ,0.333 ,0.331 ,0.330 ,0.328 ,0.327 ,0.325 ,0.324 ,0.323 ,0.322 ,0.321 ,0.320 ,0.320 ,0.319 ,0.319 ,0.319 ,0.319 ,0.319 ,0.319 ,0.319 ,0.320 ,0.321 ,0.321 ,0.322 ,0.323 ,0.325 ,0.326 ,0.327 ,0.329 ,0.330 ,0.332 ,0.333 ,0.335 ,0.337 ,0.338 ,0.340 ,0.342 ,0.343 ,0.345 ,0.346 ,0.348 ,0.349 ,0.351 ,0.352 ,0.353 ,0.354 ,0.355 ,0.356 ,0.356 ,0.357 ,0.357 ,0.357 ,0.357 ,0.357 ,0.357 ,0.357 ,0.356 ,0.355 ,0.355 ]
    datay = [0.356 ,0.357 ,0.357 ,0.357 ,0.357 ,0.356 ,0.356 ,0.355 ,0.355 ,0.354 ,0.353 ,0.351 ,0.350 ,0.349 ,0.347 ,0.346 ,0.344 ,0.342 ,0.340 ,0.338 ,0.336 ,0.335 ,0.333 ,0.331 ,0.329 ,0.327 ,0.325 ,0.324 ,0.322 ,0.321 ,0.319 ,0.318 ,0.317 ,0.316 ,0.315 ,0.314 ,0.314 ,0.313 ,0.313 ,0.313 ,0.313 ,0.314 ,0.314 ,0.315 ,0.315 ,0.316 ,0.317 ,0.319 ,0.320 ,0.321 ,0.323 ,0.324 ,0.326 ,0.328 ,0.330 ,0.332 ,0.334 ,0.335 ,0.337 ,0.339 ,0.341 ,0.343 ,0.345 ,0.346 ,0.348 ,0.349 ,0.351 ,0.352 ,0.353 ,0.354 ,0.355 ,0.356 ,0.356 ]


    out = ax.plot(datax, datay, **param_dict)


    return out

def spec_plotter_ford_iceblue(ax, param_dict):


    datax = [0.168, 0.1791, 0.2077, 0.1956, 0.168]
    datay = [0.2527, 0.3, 0.3, 0.2504, 0.2527]

    out = ax.plot(datax, datay, **param_dict)


    return out

def shiyanlou_1():

    # out = plt.plot([1,2,3,4,1,2,3,4,5,6,5,4,3,2,1])

    out = plt.plot(np.arange(2,16,1),[1,2,3,4,5,4,3,2,1,5,4,3,7,8])

    return out

def shiyanlou_2():

    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    y = np.sin(x)

    plt.plot(x, y)

def test_1():
    fig = plt.figure(num=2, figsize=(15, 8), dpi=80)
    # 使用add_subplot在窗口加子图，其本质就是添加坐标系
    # 三个参数分别为：行数，列数，本子图是所有子图中的第几个，最后一个参数设置错了子图可能发生重叠
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    # 绘制曲线
    ax1.plot(np.arange(0, 1, 0.1), range(0, 10, 1), color='g')
    # 同理，在同一个坐标系ax1上绘图，可以在ax1坐标系上画两条曲线，实现跟上一段代码一样的效果
    ax1.plot(np.arange(0, 1, 0.1), range(0, 20, 2), color='b')
    # 在第二个子图上画图
    ax2.plot(np.arange(0, 1, 0.1), range(0, 20, 2), color='r')


def main():

    # data1, data2, data3, data4 = np.random.randn(4, 100)
    # fig, (ax1, ax2) = plt.subplots(1, 2)
    # my_plotter(ax1, data1, data2, {'marker': 'x'})
    # my_plotter(ax2, data3, data4, {'marker': 'o'})
    # plt.show()


    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)


    spec_plotter_ford_white(ax1, {'marker': 'o'})

    spec_plotter_ford_iceblue(ax2, {'marker': 'o'})


    ax4.plot(['0.184'], ['0.266'], marker = 'o', markersize = 5, color = "red")

    plt.show()



if __name__ == '__main__':
     main()

