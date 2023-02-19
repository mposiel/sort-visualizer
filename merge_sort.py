
def merge(canvas, arr, left, mid, right, draw_bars, delay):
    lleng = mid - left + 1
    rleng = right - mid
    L = [0] * lleng
    R = [0] * rleng
    for i in range(0, lleng):
        L[i] = arr[left + i]
    for j in range(0, rleng):
        R[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = left
    while i < lleng and j < rleng:
        draw_bars(canvas, arr, 800, 400, i + left, j + mid + 1)
        canvas.after(delay)
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < lleng:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < rleng:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(canvas, arr, left, right, draw_bars, delay):
    if left < right:
        mid = (left + (right - 1)) // 2
        merge_sort(canvas, arr, left, mid, draw_bars, delay)
        merge_sort(canvas, arr, mid + 1, right, draw_bars, delay)
        merge(canvas, arr, left, mid, right, draw_bars, delay)
        draw_bars(canvas, arr, 800, 400, red_index=None, green_index=None)
