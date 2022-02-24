# decidionTreeクラスを実装
# 以下の5つのメソッドを用意
    # __init__: 決定木の各種初期化
    # computeEntropy: エントロピーの計算
    # computeGini: ジに不純度の計算
    # selectX: 最大の利得を持つ説明変数を選択
    # deleteColmun: 説明変数の削除
    # train: 学習データを用いて再帰的にselectXとdelColumnを実行し、決定木を作成

def __init__(self, X, Y, version=2):
    self.X = X
    self.Y = Y
    self.version = version
    
    if self.version == 1: 
        self.functionInfo = self.computeEntropy
    elif self.version == 2:
        self.functionInfo = self.computeGini
        
def computeEntropy (self, Y):
    probs = [np.sum(Y == y) / len(Y) for y in np.unique(Y)]

    return -np.sum(probs*np.log2(probs))
    
def computeGini (self, Y):
    probs = [np.sum(Y == y) / len(Y) for y in np.unique(Y)]
    
    return -np.sum(np.square(probs))

def deleteColumn(self, X, Y, column, value):
    subX = X[x[column] == value]
    subX = subX.drop(column, axis = 1)
    
    subY = Y[X[column] == value]
    
    return subX, subY

def train(self, X = [], Y = [], layer = 0):
    if not len(X): X = self.X
    if not len(Y): Y = self.Y
        
    if self.functionInfo(Y) == 0:
        print(f" --> {Y[0][0]}")
        return Y[0][0]
    else:
        print("\n", end = "")

        columnIndex, allInfo = self.select(X, Y)

        column = X.columns[columnIndex]

        for value in np.unique(X[column]):
            subX, subY = self.deleteColumn(X, Y, column, value)

            if self.lineFlag:
                print(f"{self.space*(layer - 1)}|")
            self.lineFlag = True

            if layer > 0:
                print(f"{self.space*(layer - 1)} +- ", end = "")

            print(f"{column} ({round(allInfo, 2)}) = '{value}' ({round(self.functionInfo(subY), 2)})", end = "")

            self.train(subX, subY, layer + 1)