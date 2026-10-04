products = 157
box_size = 12

complete_boxes = products // box_size
remaining_items = products % box_size
print(f"complete_boxes= {complete_boxes}")
print(f"remaining_items = {remaining_items}")