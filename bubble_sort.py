def bubble_sort(canvas, bars, delay, draw_bars):

    n = len(bars)
    for i in range(n):
        for j in range(0, n - i - 1):
            draw_bars(canvas, bars, 800, 400, j + 1, [j, j + 1]) # podświetlenie czerwone
            if bars[j] > bars[j + 1]:
                bars[j], bars[j + 1] = bars[j + 1], bars[j]
            canvas.after(delay)
        draw_bars(canvas, bars, 800, 400, i + 1) # podświetlenie zielone
    draw_bars(canvas, bars, 800, 400, green_index=None, red_index=None) # wyświetlenie końcowe
