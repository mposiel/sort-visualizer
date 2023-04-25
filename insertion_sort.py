def insertion_sort(canvas, bars, draw_bars, delay):
    for i in range(1, len(bars)):
        current_value = bars[i]
        current_index = i
        while current_index > 0 and bars[current_index - 1] > current_value:
            bars[current_index] = bars[current_index - 1]
            current_index -= 1
            draw_bars(canvas, bars, 800, 400, red_index=current_index, green_index=i)
            canvas.after(delay)
        bars[current_index] = current_value
        draw_bars(canvas, bars, 800, 400, red_index=None, green_index=i)
        canvas.after(delay)