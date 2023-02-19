def selection_sort(canvas, bars, delay, draw_bars):
    n = len(bars)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            canvas.delete("all")
            draw_bars(canvas, bars, 800, 400, j, [i])
            canvas.update()
            canvas.after(delay)
            if bars[j] < bars[min_index]:
                min_index = j
        if min_index != i:
            bars[i], bars[min_index] = bars[min_index], bars[i]
            canvas.delete("all")
            draw_bars(canvas, bars, 800, 400, i)
            canvas.update()
            canvas.after(delay)
    canvas.delete("all")
    draw_bars(canvas, bars, 800, 400)
    canvas.update()
    canvas.after(delay)
