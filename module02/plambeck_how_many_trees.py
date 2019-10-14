# Estimates the number of trees in Sacramento

sac = 100.11    # area of Sacramento in sq. mi.

# 5 sample areas measured 200' x 200'
area1 = 7
area2 = 10
area3 = 20
area4 = 30
area5 = 27

avg = (area1 + area2 + area3 + area4 + area5) / 5   # average number of trees

sample = 200 * 200              # sample size in sq. ft.

sq_mi = 5280 * 5280             # number of sq. ft. in 1 sq. mi.

sample_mi = sample / sq_mi      # sample area in sq. mi.

# average of trees per sample area multipled by area of Sacramento
answer = (avg / sample_mi) * sac

print(int(answer))
