import time
import numpy as np
start=time.perf_counter()

w=np.array([1,2,3,4,5,6,7,8,98])
x=np.array([1,2,3,4,5,6,7,8,9])
b=23
f=0

for i in range (w.shape[0]):
  f+=w[i]*x[i]
f+=b

end=time.perf_counter()

print(f"time taken by for loop (without vectorization): {end-start}")


start=time.perf_counter()
f=np.dot(w,x)+b
end=time.perf_counter()
print(f"time taken by numpy dot function (with vectorization): {end-start}")
