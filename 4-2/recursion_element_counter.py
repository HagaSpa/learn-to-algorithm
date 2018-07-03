#与えられたlistの要素の個数を数える再帰関数
def recursion_element_counter(list, count):
    # 要素数が1より少ないなら、表示する。
    if len(list) < 1:
        print(count)
        return
    #要素を後ろから一つ取り除く
    list.pop()
    #カウントをインクリメント
    count += 1
    #再帰的にrecursion_element_counterを呼び出す
    recursion_element_counter(list, count)

#対象のリスト
list = [0, 1, 2, 3]
#最初のカウントは0
count = 0
#呼び出し実施
recursion_element_counter(list, count)