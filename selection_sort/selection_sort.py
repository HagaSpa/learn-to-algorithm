# 選択ソートを行う
def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        # 最小値のindexを取得
        smallest_index = find_smallest_index(arr)
        # 最小値のindexを持つ要素を取り出して、sorted_arrに追加
        sorted_arr.append(arr.pop(smallest_index))
    return sorted_arr

# 配列の中で最も小さい値を持つ、要素のindexを返却する
def find_smallest_index(arr):
    smallest = arr[0]  # 先頭の値を取得。最小値の仮。
    smallest_index = 0 # 返却用index
    for i in range(1, len(arr)): # 1 ~ arr.lenghの長さまでの値をもつ、range型オブジェクトを生成して、すべて回す
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(selection_sort([5, 3, 6, 2, 10])) # [2, 3, 5, 6, 10]に昇順ソートして表示する