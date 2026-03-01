#Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr [min_index]:
                min_index = j

def test_build_array():
    sol = Solution()

    assert sol.buildArray([0,2,1,5,3,4]) == [0,1,2,4,5,3]
    assert sol.buildArray([5,0,1,2,3,4]) == [4,5,0,1,2,3]
    assert sol.buildArray([0]) == [0]

    print("1920 passed ✅")


test_build_array()