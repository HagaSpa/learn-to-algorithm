result = 0 #結果用変数

#配列の要素をすべて加算する再帰関数
def sum_recursion(array):
    #配列の長さが1より小さい（0なら）。基本ケース
    if len(array) < 1:
        return
    global result 
    #arrayの0番めをpopして、globalのresultへ加算
    result += array.pop(0)
    #再帰的にこのメソッドを呼び出す
    sum_recursion(array)

#対象の配列
my_array = [1, 2, 3]
#処理実行
sum_recursion(my_array) 
#結果出力
print(result)