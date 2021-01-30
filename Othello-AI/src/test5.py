# import numpy as np
# import time
# b = b'\xd7\x00\xd8\x00\xda\x00\xd9\x00\xd8\x00'
# begin = time.time()
# for n in range(0,28672):
#     a = np.frombuffer(b, dtype=np.uint8)
#
#
# end = time.time()
# bytes()
# print(a)
# print("花费时间：", end - begin)
import numpy as np

bitmaps=np.frombuffer(b'U\x02p\x03',dtype=np.int16)

print(bitmaps)

	#[215   0 216   0 218   0 217   0 216   0]
	# 时间大概是  0.017，这里没有计算，只有转换。方法二不计算，只转换的话同样的数据要0.12秒