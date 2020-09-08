# er = row_end, ec = column_end, sr = row_start, sc = column_start
def conv2D(matrix, kernal, step=1):
  er, ec = kernal.shape[0], kernal.shape[0]
  convd = []
  range_tensor = matrix.shape[0]-(kernal.shape[0]-1)
  for sr in range(range_tensor):
      for sc in range(range_tensor)):
        temp = matrix[sr:er, sc:ec] * kernal
        convd.append(np.amax(temp))
        ec += step
        if (sc == (matrix.shape[0] - (kernal.shape[0] - 1) - 1)): 
          ec = kernal.shape[0]
          er += step

  return np.array(convd).reshape(range_tensor,range_tensor)
