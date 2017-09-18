def one_hot(labels,n_class=6):
    """
    Function:One-hot encoding
    Args:
        laels   : label (numpy.array,shape=(N,))
        n_class : the number of classes(int)
    Return:
        y       : label after one-hot encoding (numpy.array,shape=(N,n_class))
    """      
    # np.eye 生成对角矩阵，此处为6×6对角阵
    expansion = np.eye(n_class)
    # labels-1(j) 对应 labels-1 中的第j个数
    # [i,labels-1(j)]对应对角阵第i行j列的取值，当且仅当i=labels-1(j)时，取值才为1，其他情况为0
    # 最终组成矩阵规模 n_class*len(labels-1)
    # 对于labels-1中的每一个数，矩阵n_class仅有一列是1.从而实现one-hot encoding,expansion矩阵仅是用来找值的工具
    y = expansion[:,labels-1].T
    ## print(y.shape)
    assert y.shape[1] == n_class,"Wrong number of labels!"
    return y
